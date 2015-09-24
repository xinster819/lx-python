import datetime, time;
import urllib, urllib2;
from time import strftime, localtime, clock;
class DateUtils:
    @staticmethod
    def yesterday():
        return int(strftime("%Y%m%d", localtime())) - 1;
    @staticmethod
    def oneHourBefore():
        return int(strftime("%Y%m%d%H", localtime())) - 1;
print DateUtils.yesterday();
