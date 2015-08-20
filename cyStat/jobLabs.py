import paramiko;
import MySQLdb;
import DateUtils;
from labsStat import LabsStat;
yesterday = DateUtils.DateUtils.yesterday();
ssh = paramiko.SSHClient();
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('10.10.80.154', username='root', password='AkxmIUD=')
stdin,stdout,stderr = ssh.exec_command("cat /opt/logs/cmt-labs-plugins-8080/stdout/stdout.log." + str(yesterday));
dic = {};
for line in stdout:
    if "AccessInterceptor.afterCompletion" in line:
        arr = line.split(" ")
        if len(arr) ==  11:
            uri = arr[7].split("#")[1]
            type = 1
            cost = int(arr[9]);
            if uri not in dic.keys():
                dic[uri] = LabsStat(yesterday, type, uri);
            try:
                if cost > 5000:
                    dic[uri].ms_5000 += 1;
                elif cost > 2000:
                    dic[uri].ms_2000 += 1;
                elif cost > 1000:
                    dic[uri].ms_1000 += 1;
                elif cost > 500:
                    dic[uri].ms_500 += 1;
                elif cost > 200:
                    dic[uri].ms_200 += 1;
                dic[uri].req_count += 1;
            except Error as a:
                print a;

db = MySQLdb.connect(host="10.10.85.62", # your host, usually localhost
                     user="cmt", # your username
                      passwd="cmt", # your password
                      db="cyanstat",
                      port=3306) # name of the data base
cur = db.cursor()
sql = "INSERT INTO labs_stat (date,type,uri,ms_200,ms_500,ms_1000,ms_2000,ms_5000,req_count) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
for key in dic.keys():
    one = dic[key];
    param = [one.date,one.type,one.uri,one.ms_200,one.ms_500,one.ms_1000,one.ms_2000,one.ms_5000,one.req_count];
    cur.execute(sql, param)
cur.close()
db.close()
ssh.close()
