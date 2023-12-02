import smtplib, ssl

port = 465  # For SSL
sender_email = "maul2821@gmail.com"
password = "gvmk xphz xfyy zoov"

# Create a secure SSL context
context = ssl.create_default_context()

def send_email(sender, report, authorities):
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_email, password)
        # TODO: Send email here
        receiver_email = "maul2821@gmail.com"
        message = f"""\
        Subject: Email from {sender} for {authorities}

        {report}"""

        # Send email here

        # TODO: Send email here
        server.sendmail(sender_email, receiver_email, message)