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
def my_task():
    print('This is a dynamic task.')


from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from sqlalchemy import create_engine

# 创建SQLAlchemy引擎
engine = create_engine('postgresql://user:password@localhost/mydatabase')

# 创建SQLAlchemyJobStore对象
jobstore = SQLAlchemyJobStore(engine=engine)

# 创建BackgroundScheduler对象，并将jobstore作为参数传递
scheduler = BackgroundScheduler(jobstores={'default': jobstore})


from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from sqlalchemy import create_engine

# 创建SQLAlchemy引擎
engine = create_engine('postgresql://user:password@localhost/mydatabase')

# 创建SQLAlchemyJobStore对象
jobstore = SQLAlchemyJobStore(engine=engine)

# 创建BackgroundScheduler对象，并将jobstore作为参数传递
scheduler = BackgroundScheduler(jobstores={'default': jobstore})


add_dynamic_job('my_dynamic_task', my_task, 'interval', seconds=10)

from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Job(Base):
    __tablename__ = 'job'

    id = Column(Integer, primary_key=True)
    job_id = Column(String(50), unique=True)
    func = Column(String(255))
    args = Column(String(255))
    kwargs = Column(String(255))
    trigger = Column(String(50))
    trigger_args = Column(String(255))



"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.triggers.cron import CronTrigger

# 创建SQLAlchemy引擎和Session
engine = create_engine('postgresql://user:password@localhost/mydatabase')
Session = sessionmaker(bind=engine)
session = Session()

# 创建SQLAlchemyJobStore对象和BackgroundScheduler对象
jobstore = SQLAlchemyJobStore(engine=engine)
scheduler = BackgroundScheduler(jobstores={'default': jobstore})

# 循环读取数据库中的任务信息，并添加到调度程序中
for job in session.query(Job).all():
    func = eval(job.func)
    args = eval(job.args) if job.args else []
    kwargs = eval(job.kwargs) if job.kwargs else {}
    trigger_args = eval(job.trigger_args) if job.trigger_args else {}

    if job.trigger == 'cron':
        trigger = CronTrigger(**trigger_args)
    else:
        raise ValueError('Unknown trigger type: {}'.format(job.trigger))

    scheduler.add_job(func, trigger=trigger, args=args, kwargs=kwargs, id=job.job_id)

# 启动调度程序
scheduler.start()




from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.memory import MemoryJobStore
from apscheduler.triggers.cron import CronTrigger

# 创建MemoryJobStore对象和BackgroundScheduler对象
jobstore = MemoryJobStore()
scheduler = BackgroundScheduler(jobstores={'default': jobstore})

# 定义一个函数来添加新的任务
def add_job(job_id, func, trigger, args=None, kwargs=None):
    scheduler.add_job(func, trigger=trigger, args=args, kwargs=kwargs, id=job_id)

# 启动调度程序
scheduler.start()

# 添加一个初始的任务
add_job('my_job', my_function, CronTrigger(second='0,30'))

# 在稍后的时间添加一个新的任务
add_job('my_other_job', my_other_function, CronTrigger(minute='*/10'))

"""
