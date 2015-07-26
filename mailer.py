#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import sys
import smtplib
import csv

def get_credential_from_file():
    with open('credentials.txt') as f:
        content = f.readlines()

    gmail_email = ''
    gmail_password = ''

    for line in content:
        words = line.split(":")
        print words
        if words[0] == 'gmail_email':
            gmail_email = words[1].strip()
        elif words[0] == 'gmail_password':
            gmail_password = words[1].strip()

    return gmail_email, gmail_password


def get_subject_and_body_from_files():
    with open('subject.txt') as f:
        subject_content = f.readlines()

    subject = subject_content[0]

    with open('body.txt') as f:
        body_content = f.readlines()

    body = "".join(body_content)

    return subject, body

def send_email(gmail_email, gmail_password, from_email, to_email, subject, body):
    print "Sending to: "+to_email
    # Prepare actual message
    message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (from_email, ", ".join([to_email]), subject, body)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587) #or port 465 doesn't seem to work!
        server.ehlo()
        server.starttls()
        server.login(gmail_email, gmail_password)
        server.sendmail(from_email, [to_email], message)
        server.close()
        print 'successfully sent the mail'
    except:
        print "failed to send mail"

def get_emails_and_names_from_file():
    email_dict = {}
    with open('email_list.csv', 'rb') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader: 
            name = row['name']
            email = row['email']
            email_dict[email] = name
            

    return email_dict


emails = get_emails_and_names_from_file()
print emails

gmail_email, gmail_password = get_credential_from_file()

print 'email = ' + gmail_email
print 'password = ' + gmail_password

subject, body = get_subject_and_body_from_files()

print 'subject = ' + subject
print 'body = ' + body

#sys.exit(1)

for email, name in emails.iteritems():
    print "---------------------------------------"
    formatted_body = body.replace("<name>", name)
    send_email(gmail_email, gmail_password, gmail_email, email, subject, formatted_body)

