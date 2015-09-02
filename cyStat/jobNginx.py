import paramiko;
import MySQLdb;
import DateUtils;
from labsStat import LabsStat;
yesterday = DateUtils.DateUtils.yesterday();
ssh = paramiko.SSHClient();
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('10.10.80.98', username='root', password='gU:zC^sdwb')
stdin,stdout,stderr = ssh.exec_command("cat /opt/logs/cmt-core-web-8080/access/access.log.20150826.2110");
ids = {};
try:
    for line in stdout:
        if "showScore=true" in line:
            arr = line.split("\"\"")
            url = arr[4];
            a = url.split("client_id=")[1].split("&")[0]
            if ids[a] > 0:
                ids[a] = ids[a] + 1
except UnicodeDecodeError as e:
    print e
print ids
ssh.close()
