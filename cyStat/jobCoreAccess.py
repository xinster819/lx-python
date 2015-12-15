import paramiko;
import MySQLdb;
import DateUtils;
yesterday = DateUtils.DateUtils.yesterday();
ssh = paramiko.SSHClient();
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('10.11.156.38', username='root', password='?=gQ64^d6G')
chan = ssh.get_transport().open_session()
chan.exec_command("cat /opt/logs/cmt-core-web-8080/access/access.log." + str(yesterday) + ".*");
stdout = chan.makefile('rb', -1)
dic = {};
for line in stdout:
    arr = line.split("\"\"");
    ip = arr[0];
    uri = arr[4].split(" ")[1].split("?")[0];
    if uri.startswith('/api/2/config/get/'):
        uri = '/api/2/config/get';
    if uri.startswith('/api/2/user/flush/'):
        uri = '/api/2/user/flush';
    if uri.startswith('/api/2/user/c/'):
        uri = '/api/2/user/c';
    if uri.startswith('/api/2/user/u/'):
        uri = '/api/2/user/u';
    if uri.startswith('/api/comment/'):
        uri = '/api/comment';
    if uri.startswith('/api/2%'):
        continue;
    if uri not in dic.keys():
        dic[uri] = 1;
    else:
        dic[uri] += 1;
print dic

db = MySQLdb.connect(host="10.10.85.62", # your host, usually localhost
                     user="cmt", # your username
                      passwd="cmt", # your password
                      db="cyanstat",
                      port=3306) # name of the data base
cur = db.cursor()
sql = "INSERT ignore INTO interface_stat (name, date, pv) VALUES(%s,%s,%s)"
for key in dic.keys():
    param = [key, yesterday, dic[key]];
    cur.execute(sql, param)
cur.close()
db.close()
ssh.close()
