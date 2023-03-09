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
import yaml

class Scheduler:
    def __init__(self, config_file=None, jobstores=None, executors=None, job_defaults=None, timezone=None):
        if not jobstores:
            jobstores = {'default': MemoryJobStore()}
        self.scheduler = BackgroundScheduler(jobstores=jobstores, executors=executors, job_defaults=job_defaults, timezone=timezone)
        self.config_file = config_file

    def add_job_from_config(self, config):
        job_id = config.get('id')
        job_func = config.get('func')
        job_args = config.get('args', [])
        job_kwargs = config.get('kwargs', {})
        job_trigger = config.get('trigger')
        job_enabled = config.get('enabled', True)

        if job_enabled:
            self.scheduler.add_job(
                func=job_func,
                args=job_args,
                kwargs=job_kwargs,
                trigger=job_trigger,
                id=job_id,
                name=job_id
            )
        else:
            self.scheduler.remove_job(job_id)

    def load_jobs_from_config_file(self):
        with open(self.config_file, 'r') as f:
            config = yaml.load(f, Loader=yaml.FullLoader)

        for job_config in config:
            self.add_job_from_config(job_config)

    def start(self):
        self.load_jobs_from_config_file()
        self.scheduler.start()

    def shutdown(self, wait=True):
        self.scheduler.shutdown(wait=wait)

"""

- id: hello_world
  func: __main__:hello_world
  trigger:
    type: interval
    seconds: 5

- id: print_message
  func: __main__:print_message
  args: ['Hello, World!']
  trigger:
    type: cron
    minute: 0
    hour: 12
    day_of_week:
"""


def hello_world():
    print('Hello, World!')

def print_message(message):
    print(message)


if __name__ == '__main__':
    scheduler = Scheduler(config_file='config.yaml')
    scheduler.start()
