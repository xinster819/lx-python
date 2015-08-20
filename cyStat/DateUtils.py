import datetime, time;
from time import strftime, gmtime;
class DateUtils:
    @staticmethod
    def yesterday():
        return int(strftime("%Y%m%d", gmtime())) - 1;
