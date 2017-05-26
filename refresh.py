import imapclient
import pyzmail
import datetime

imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
imapObj.login('refresh.statusc9@gmail.com', 'd2z4BJxeSUVv')

imapObj.select_folder('INBOX', readonly=True)
UIDs = imapObj.search(['UNSEEN', 'FROM jake.jung@insidesales.com']) # may be set to today's date? I guess it doesn't matter if it's chroning

if not UIDs:
	print "There aren't any new emails!"
else:
	print "================================="
	for i in UIDs:
		rawMessages = imapObj.fetch([i],['BODY[]'])
		message = pyzmail.PyzMessage.factory(rawMessages[i]['BODY[]'])
		ts = message['Date']
		dt = datetime.datetime.strptime(ts, "%a, %d %b %Y %H:%M:%S +0000") - datetime.timedelta(hours=6)
		dtAdjusted = dt.strftime("%Y-%m-%d / %H:%M:%S MST")
		print "Subject: " + message.get_subject()
		print "To: " + message.get_addresses('to')[0][0]
		print "D/T: " + dtAdjusted
		if message.text_part != None:
			print "Body: " + message.text_part.get_payload().decode(message.text_part.charset)
			print "================================="

#####################################
# CODE HERE TO EXTRACT REFRESH DATA #
#####################################

# company = something
# status = something


# # Refresh object
# class Refresh(object):
# 	company = company
# 	status = status

# # 	# INITIALIZER
# 	def __init__(self, company, status):
# 		self.company = company
# 		self.status = status

# # # CONSTRUCTOR
# def make_refresh(company, status):
# 	refresh = Refresh(company, status)
# 	return refresh

# # # LIST OF REFRESHES
# my_refreshes = []

# for i in range








