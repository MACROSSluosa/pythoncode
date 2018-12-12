#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ftplib import FTP
import sys,getpass,os.path
host = '202.43.149.133'
password = '8U3YBoxU'
port = 21
timeout = 30 
username = 'sda' 
localfile = '/Users/mac/pythoncode/readme'
remotepath = '/shandong/test02'

f = FTP()
f.connect(host,port,timeout)
f.login(username,password)
f.set_pasv(True)
#print f.getwelcome()
f.cwd(remotepath)
fd = open(localfile,'rb')
f.storbinary('STOR %s' % os.path.basename(localfile),fd)
fd.close()
f.quit()
