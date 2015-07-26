# Mega-mailer

This is a simple script that will read email subject, body and recipients from files using gmail servers.

Don't forget to enable [Allow insecure apps](https://www.google.com/settings/security/lesssecureapps) before.

# Setup

Create the following files:

- subject.txt (one line)
- body.txt (multiple lines)
- credentials.txt (one line)
- email_list.csv (multiple lines)

body.txt example
```
Hello <name>,

I am writing you because you are my representing politician.

I want to tell you about...

Best regards,
Fahime
```

credentials.txt example
```
foo@bar.com:mypassword
```

email_list.csv example
```
name,email
Alice,alice.bobson@foo.com
```

