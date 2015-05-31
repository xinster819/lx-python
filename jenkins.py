import sys,os;
if len(sys.argv) == 1:
  print 'need one command: start/stop/restart...';
  sys.exit();
cmd = sys.argv[1];
if cmd == 'start':
  os.system('java -Dhudson.DNSMultiCast.disabled=true -jar /opt/apps/jenkins/jenkins.war --httpPort=8088 start')
elif cmd == 'stop':
  os.system('java -Dfile.encoding=UTF-8 -Dhudson.DNSMultiCast.disabled=true -jar /opt/apps/jenkins/jenkins.war stop')
elif cmd == 'restart':
  os.system('java -Dfile.encoding=UTF-8 -Dhudson.DNSMultiCast.disabled=true -jar /opt/apps/jenkins/jenkins.war stop')
else:
  print 'nothing happen';