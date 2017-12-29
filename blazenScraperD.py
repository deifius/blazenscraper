ls#!/usr/bin/env python

from BeautifulSoup import BeautifulSoup
from urllib2 import urlopen
from time import sleep
import re
from twilio.rest import TwilioRestClient 

# Twilio Authorizations	
ACCOUNT_SID = "" 
AUTH_TOKEN = "" 
#BlazenGems location
site = "https://blaze-n-gems.myshopify.com/collections/rough-montana-sapphires?page=2&sort_by=created-descending"
yourcellphone = ""
originnumber = ""

while 1==1:
	html = urlopen(site).read()
	datesadded = re.compile("Date Added: \w+ \w+ \w+, \w+").findall(html)
	lastdates = open('lastdateset.txt').read().split("\n")
	if "".join(datesadded) != "".join(lastdates):
		client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
		client.messages.create(
			to = yourcellphone, 
			from_ = originnumber, 
			body="Hey amigo! http://blazengems.com/store/index.php?main_page=products_new",)
		#print datesadded 
		#print "\n\n\n"
		#print lastdates

	newdates = open('lastdateset.txt','w')
	for date in datesadded:
		newdates.write(date +"\n")
	newdates.close()
	sleep(1200)
