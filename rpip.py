# -*- coding: utf-8 -*-

from smtplib import SMTP
from email.MIMEText import MIMEText
from email.Utils import formatdate
from commands import getoutput

# mail configuration
from_addr  = 'foo@example.com'
to_addr    = 'foo@example.com'
login_user = 'foo@example.com'
login_pass = 'password'

# get current IP
msg = 'My IP address is %s\n' % getoutput( 'hostname -I' )

# build mail message
mail            = MIMEText( msg )
mail['Subject'] = 'Raspberry Pi Notification'
mail['From']    = from_addr
mail['To']      = to_addr
mail['Date']    = formatdate()

# send current IP
send = SMTP( 'smtp.gmail.com', 587 )
send.ehlo()
send.starttls()
send.ehlo()
send.login( login_user, login_pass )
send.sendmail( from_addr, [ to_addr ], mail.as_string() )
send.close()
