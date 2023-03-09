# This program is free software: 
# you can redistribute it and/or modify it under the terms of the GNU General Public License as published 
# by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, 
# but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. 
# See the GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along with this program. 
# If not, see <https://www.gnu.org/licenses/>.
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from sqlalchemy import create_engine, Table, Column, String, Integer


class Scheduler:
    def __init__(self, db_url=None, table_name='jobs', jobstores=None, executors=None, job_defaults=None,
                 timezone=None):
        if not jobstores:
            jobstores = {'default': SQLAlchemyJobStore(engine=create_engine(db_url))}
        self.scheduler = BackgroundScheduler(jobstores=jobstores, executors=executors, job_defaults=job_defaults,
                                             timezone=timezone)

        if not self.scheduler.get_job('load_jobs_from_db'):
            self.scheduler.add_job(self.load_jobs_from_db, 'interval', seconds=60, id='load_jobs_from_db',
                                   name='Load jobs from database')

        metadata = Table(table_name, Column('id', Integer, primary_key=True), Column('name', String(255)),
                         Column('func', String(255)), Column('trigger', String(255)), Column('args', String(255)),
                         Column('kwargs', String(255)), Column('enabled', Integer))

        self.db_url = db_url
        self.table_name = table_name
        self.metadata = metadata

    def add_job(self, name, func, trigger, args=None, kwargs=None, enabled=True):
        job = {
            'name': name,
            'func': func,
            'trigger': trigger,
            'args': args,
            'kwargs': kwargs,
            'enabled': enabled
        }

        engine = create_engine(self.db_url)
        with engine.connect() as conn:
            conn.execute(self.metadata.insert(), job)

    def remove_job(self, name):
        engine = create_engine(self.db_url)
        with engine.connect() as conn:
            conn.execute(self.metadata.delete().where(self.metadata.c.name == name))

    def load_jobs_from_db(self):
        engine = create_engine(self.db_url)
        with engine.connect() as conn:
            result = conn.execute(self.metadata.select())
            jobs = result.fetchall()
            for job in jobs:
                if job['enabled']:
                    self.scheduler.add_job(
                        func=job['func'],
                        trigger=job['trigger'],
                        args=job['args'],
                        kwargs=job['kwargs'],
                        id=job['name'],
                        name=job['name']
                    )
                else:
                    self.scheduler.remove_job(job['name'])

    def start(self):
        self.scheduler.start()

    def shutdown(self, wait=True):
        self.scheduler.shutdown(wait=wait)


"""
CREATE TABLE jobs (
    id INTEGER PRIMARY KEY,
    name VARCHAR
    func VARCHAR(255),
    trigger VARCHAR(255),
    args VARCHAR(255),
    kwargs VARCHAR(255),
    enabled INTEGER




你还需要提供一个数据库连接字符串（`db_url`），该字符串指定要使用的数据库的类型和位置。你可以在初始化`Scheduler`对象时传入`db_url`参数，也可以在调用`add_job`方法时传入。如果你没有传入`db_url`参数，则默认使用SQLite数据库。

以下是一个使用示例：

```python
from datetime import datetime
from time import sleep

def hello_world():
    print('Hello, World! The time is: %s' % datetime.now())

scheduler = Scheduler(db_url='sqlite:///jobs.db')

scheduler.add_job('hello_world', hello_world, 'interval', seconds=5)

scheduler.start()

try:
    while True:
        sleep(1)
except KeyboardInterrupt:
    scheduler.shutdown()
