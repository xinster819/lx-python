import urllib2
response = urllib2.urlopen('http://10.16.1.86/api/up/36')
html = response.read()
print html
