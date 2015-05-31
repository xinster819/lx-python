import os;
import sys;
conf = "/opt/conf";
logs = "/opt/logs";
apps = "/opt/apps";
bin = "/opt/bin";
if not os.path.exists(conf):
  os.makedirs(conf);
if not os.path.exists(logs):
  os.makedirs(logs);
if not os.path.exists(apps):
  os.makedirs(apps);
if not os.path.exists(bin):
  os.makedirs(bin);