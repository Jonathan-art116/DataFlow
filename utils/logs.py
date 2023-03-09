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
import logging
import os



def setup_logger(logger_name, log_file=None, level=logging.INFO, mode='w', stream=True):
    """setup  logger"""
    logger = logging.getLogger(logger_name)
    logger.setLevel(level)

    formatter = logging.Formatter(
        '[%(asctime)s] %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s'
    )

    if log_file:
        log_dir = os.path.dirname(log_file)
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        file_handler = logging.FileHandler(log_file, mode=mode)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    if stream:
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger


log = setup_logger('DataFlow', log_file=None, level=logging.INFO, mode='a', stream=True)
log.info('这是一条INFO级别的日志')
log.warning('这是一条WARNING级别的日志')
log.error('这是一条ERROR级别的日志')
