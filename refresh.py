import imapclient
import pyzmail
import datetime
import re
import unicodedata

imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
imapObj.login('refresh.statusc9@gmail.com', 'd2z4BJxeSUVv')

imapObj.select_folder('INBOX', readonly=True)
UIDs = imapObj.search(['UNSEEN', 'FROM jake.jung@insidesales.com']) # may be set to today's date? I guess it doesn't matter if it's chroning



# Refresh object
class Refresh(object):

	# INITIALIZER
	def __init__(self, company, status):
		self.company = company
		self.status = status

	def make_refresh(self):
		print self.company



if not UIDs:
	print "There aren't any new emails!"
else:
	print "================================="
	for i in UIDs:

		rawMessages = imapObj.fetch([i],['BODY[]'])
		message = pyzmail.PyzMessage.factory(rawMessages[i]['BODY[]'])

		# Timestamp
		ts = message['Date']
		dt = datetime.datetime.strptime(ts, "%a, %d %b %Y %H:%M:%S +0000") - datetime.timedelta(hours=6)
		dtAdjusted = dt.strftime("%Y-%m-%d / %H:%M:%S MST")
		
		# Company
		companyRaw = message.get_addresses('to')[0][0]
		strCompany = unicodedata.normalize('NFKD', companyRaw).encode('ascii','ignore')
		company = strCompany.split("@")[0].split("+")[-1] # unicode to str

		# Status
		statusRaw = message.get_subject()
		statusEmail = unicodedata.normalize('NFKD', statusRaw).encode('ascii','ignore').split(" ")[3][1:-1] # unicode to str
		# change default email subject to readable str
		def f(statusEmail):
		    return {
		        'Failure': 'Failed',
		        'Success': 'Successful',
		        'Delay': 'Delayed'
		}[statusEmail]
		status = f(statusEmail)

		# Refresh(company, "Failed")

		print "Subject: " + message.get_subject()
		print "To: " + strCompany
		# print "Object: " + Refresh(company, "Failed").company
		print "Company: " + company
		print "Status: " + status
		print "D/T: " + dtAdjusted
		if message.text_part != None:
			print "Body: " + message.text_part.get_payload().decode(message.text_part.charset)
			print "================================="

#####################################
# CODE HERE TO EXTRACT REFRESH DATA #
#####################################



# CONSTRUCTOR
# def make_refresh(company, status):
# 	refresh = Refresh(to, "Failed")
# 	print refresh

# LIST OF REFRESHES

# pitney = Refresh(to, "Failed")
# print pitney.company





