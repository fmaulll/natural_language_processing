import smtplib, ssl

port = 465  # For SSL
sender_email = "maul2821@gmail.com"
password = "gvmk xphz xfyy zoov"

# Create a secure SSL context
context = ssl.create_default_context()

def send_to(authorities):
    if authorities == 'Dinas Kependudukan dan Pencatatan Sipil Kota Bandung':
        return 'bandung.disdukcapil@gmail.com'
    
    elif authorities == 'Dinas Sumberdaya Air dan Bina Marga Kota Bandung':
        return 'bandung.dsdabm@gmail.com'
    
    elif authorities == 'Dinas Perhubungan Kota':
        return 'bdg.dishub@gmail.com'
    
    elif authorities == 'Satuan Polisi Pamong Praja Kota Bandung':
        return 'bandung.satpolpp@gmail.com'
    
    elif authorities == 'Dinas Perhubungan Kota':
        return 'bandung.satpolpp@gmail.com'
    else:
        return ''
    

def send_email(sender, report, authorities):
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_email, password)
        # TODO: Send email here
        receiver_email = send_to(authorities)
        message = f"""\
        Subject: Email from {sender} for {authorities}

        {report}"""

        # Send email here

        # TODO: Send email here
        server.sendmail(sender_email, receiver_email, message)