import smtplib


# Get the "To" emails you will send to. Currently hardcoded.
def get_emails():
    emails = {"joelsfoster@gmail.com": "Joel", "dwangerin35@gmail.com": "my wifey, Diana"}
    return emails


# Send emails to recipients
def send_emails(emails, forecast):
    # Connect to the Gmail's SMTP server, using the TLS port (not the SSL port)
    server = smtplib.SMTP('smtp.gmail.com', '587')
    
    # Start TLS encryption
    server.starttls()
    
    # Login
    from_email = input("Please input your 'From' Gmail address.")
    password = input("Please input your Gmail password.")
    server.login(from_email, password)

    # Send to entire email list
    for to_email, first_name in emails.items():
        message = "Subject: Today's weather\n"
        message += "Hi " + first_name + "!\n\n"
        message += forecast + "\n\n"
        message += "Have a wonderful day!\n\n"
        message += "Sincerely,\n"
        message += "The Weatherman"
        server.sendmail(from_email, to_email, message)

    server.quit()

    # Confirmation
    confirmation = "Email sent!"
    print(confirmation)

 
