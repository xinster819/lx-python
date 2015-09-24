import paramiko;
import MySQLdb;
import DateUtils;
from PvStat import PvStat;
yesterday = DateUtils.DateUtils.yesterday();
ssh = paramiko.SSHClient();
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('10.11.152.101', username='root', password='Bjs^T54r')
stdin,stdout,stderr = ssh.exec_command("cat /opt/logs/advert-pay-service/8077/stdout.log." + str(yesterday) + "*");
dic = {};
type = 1;
for line in stdout:
    if "ERROR" in line:
        uri = "AdService_ERROR"
        if uri not in dic.keys():
            dic[uri] = PvStat(yesterday, type, uri, "AdService error");
        dic[uri].pv += 1;
    if "RealTimePay agencyid:" in line:
        uri = "advert_daily_pay_req";
        if uri not in dic.keys():
            dic[uri] = PvStat(yesterday, type, uri, "daily pay req total amount");
        dic[uri].pv += 1;

db = MySQLdb.connect(host="10.10.85.62", # your host, usually localhost
                     user="cmt", # your username
                      passwd="cmt", # your password
                      db="cyanstat",
                      port=3306) # name of the data base
cur = db.cursor()
sql = "INSERT IGNORE INTO pv_stat (date,type,uri,pv,desp) VALUES(%s,%s,%s,%s,%s)"
for key in dic.keys():
    one = dic[key];
    param = [one.date,one.type,one.uri,one.pv,one.desp];
    cur.execute(sql, param)
cur.close()
db.close()
ssh.close()
