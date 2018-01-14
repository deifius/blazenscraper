#!/usr/bin/env python3

import smtplib
import os

def sendemail (frm, to, cc, subject, message, login, password, smtpserver):
	header ='From: %s\n' % frm
	header += 'To: %s\n' % ','.join(to)
	header += 'Cc: %s\n' % ','.join(cc)
	header += 'Subject: %s\n\n' % subject
	message = header + message
	server = smtplib.SMTP(smtpserver,587)
	server.starttls()
	server.login(login, password)
	problems = server.sendmail(frm, to, message)
	print(message)
	server.quit()

frm = ""
to = ['']
cc = []
subject = 'New Rough Montana Sapphires'
message = 'https://blaze-n-gems.myshopify.com/collections/rough-montana-sapphires?page=2&sort_by=created-descending'
login = ''
password = ''
smtpserver = 'smtp.gmail.com'

newstuffcheck = open('difflog','r').read()
print(newstuffcheck)
if newstuffcheck != "Files urls/newfile and oldfile are identical\n":
	sendemail (frm, to, cc, subject, message, login, password, smtpserver)
	os.rename('urls/newfile','oldfile')
else:
	print("nothing new")
