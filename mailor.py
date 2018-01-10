#!/usr/bin/env python3

import smtplib

def sendemail (frm, to, cc, subject, message, login, password, smtpserver):
	header ='From: %s\n' % frm
	header += 'To: %s\n' % ','.join(to)
	header += 'Cc: %s\n' % ','.join(cc)
	header += 'Subject: %s\n\n' % subject
	message = header + message
	
	server = smtplib.SMTP(smtpserver)
	server.starttls()
	server.login(login, password)
	problems = server.sendmail(frm, to, message)
	print(message)
	server.quit()

frm = ""
to = []
cc = []
subject = 'here come dat boi'
message = 'o shit wadup'
login = ''
password = ''
smtpserver = 'smtp.gmail.com'

sendemail (frm, to, cc, subject, message, login, password, smtpserver)

