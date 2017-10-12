import imapclient
import pyzmail
import datetime
import re
import unicodedata
import MySQLdb


# Initialize Imap Connection
imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
imapObj.login('refreshstatusc9@gmail.com', 'd2z4BJxeSUVv')
imapObj.select_folder('Refreshes', readonly=False)
UIDs = imapObj.search(['UNSEEN', 'FROM DONOTREPLY@c9inc.com'])

# Initialize DB Connection
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="root",
                     db="refresh") 
cur = db.cursor()

# Scrape Data From Email
if not UIDs:
	print "There aren't any new emails!"
else:
	print "================================="
	for i in UIDs:

		rawMessages = imapObj.fetch([i],['BODY[]'])
		message = pyzmail.PyzMessage.factory(rawMessages[i]['BODY[]'])

		# Timestamp
		ts = message['Date']
		# dtRaw = datetime.datetime.strptime(ts, "%a, %d %b %Y %H:%M:%S +0000") - datetime.timedelta(hours=6)
		# dt = dtRaw.strftime("%Y-%m-%d %H:%M:%S MST")
		
		# Company
		companyRaw = message.get_addresses('to')
		companyString = [tuple(map(str,eachTuple)) for eachTuple in companyRaw]
		companyList = [i[0] for i in companyString]
		companyFinal = [item for item in companyList if 'refreshstatusc9' in item][0]

		# strCompany = unicodedata.normalize('NFKD', companyRaw).encode('ascii','ignore')
		company = companyFinal.split("@")[0].split("+")[-1].split("_")[0] # unicode to str

		# Status
		statusRaw = message.get_subject()
		statusEmail = unicodedata.normalize('NFKD', statusRaw).encode('ascii','ignore').split(" ")[2][1:-1] # unicode to str
		
		# change default email subject to readable str
		def f(statusEmail):
		    return {
		        'Failure': 'Failed',
		        'Success': 'Successful',
		        'Delay': 'Delayed',
		        'Start': 'Started'
		}[statusEmail]
		status = f(statusEmail)

		

		# Org ID
		orgid = companyFinal.split("@")[0].split("+")[-1].split("_")[-1]

		# Body
		bodyRaw = message.html_part.get_payload().decode(message.html_part.charset)
		body = unicodedata.normalize('NFKD', bodyRaw).encode('ascii','ignore')

		# Refresh(company, "Failed")

		print "Subject: " + message.get_subject()
		print "To: " + companyFinal
		# print "Object: " + Refresh(company, "Failed").company
		if message.text_part != None:
			print "Body: " + body
			print "================================="
		print "Dashboard Data:"
		print "Company: " + company
		print "Status: " + status
		print "D/T: " + ts
		print "OrgID: " + orgid

		# if status != "Started":
		# Insert Data 
		cur.execute("""
			INSERT INTO refresh (orgid,company,status,dt,body) 
			VALUES (%s,%s,%s,%s,%s) 
			ON DUPLICATE KEY UPDATE 
			company = VALUES (company),
			status = VALUES (status),
			dt = VALUES (dt),
			body = VALUES (body)""", (orgid,company,status,ts,body))

		db.commit()

		for row in cur.fetchall():
			print row # just print
	db.close()

		






# CONSTRUCTOR
# def make_refresh(company, status):
# 	refresh = Refresh(to, "Failed")
# 	print refresh

# LIST OF REFRESHES

# pitney = Refresh(to, "Failed")
# print pitney.company



# Refresh object
class Refresh(object):

	# Init
	def __init__(self, company, status, timestamp, orgid):
		self.company = company
		self.status = status
		self.timestamp = timestamp
		self.orgid = orgid

	def make_refresh(self):
		print self.company

#####################################
# CODE HERE TO EXTRACT REFRESH DATA #
#####################################
