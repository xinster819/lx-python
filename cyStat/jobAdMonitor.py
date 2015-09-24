import paramiko;
import MySQLdb;
import DateUtils;
import urllib2, urllib;
from PvStat import PvStat;
yesterday = DateUtils.DateUtils.yesterday();
ssh = paramiko.SSHClient();
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('10.11.152.101', username='root', password='Bjs^T54r')
stdin,stdout,stderr = ssh.exec_command("cat /opt/logs/advert-pay-service/8077/stdout.log." + str(yesterday));
needMsg = 0;
type = 1;
for line in stdout:
    if "ERROR" in line:
        needMsg = needMsg + 1;
if needMsg > 0:
    value = 'advert pay server error happened. count: ' + str(needMsg);
    params = urllib.urlencode({'content' : value });
    urllib2.urlopen("http://10.10.77.142:8088/monitor/send/mailmsg", params);
print needMsg;
ssh.close()
