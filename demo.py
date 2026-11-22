from turbofan_predictive_maintenance.logger import logging
from turbofan_predictive_maintenance.exception import TurbofanException
import sys

#logging.info('Welcome to our custom log')

try:
    a=2/0
except Exception as e:
    raise TurbofanException(e,sys)
