import smtplib, ssl

port = 465  # For SSL
sender_email = "maul2821@gmail.com"
password = "gvmk xphz xfyy zoov"

# Create a secure SSL context
context = ssl.create_default_context()

def send_to_name(authorities):
    if authorities == 'dinas-kependudukan-dan-pencatatan-sipil-Kota-bandung':
        return 'Dinas Kependudukan dan Pencatatan Sipil Kota Bandung'
    
    elif authorities == 'dinas-sumber-daya-air-dan-bina-marga-kota-bandung':
        return 'Dinas Sumber Daya Air dan Bina Marga Kota Bandung'
    
    elif authorities == 'dinas-perhubungan-kota-bandung':
        return 'Dinas Perhubungan Kota Bandung'
    
    elif authorities == 'satuan-polisi-pamong-praja-Kota-bandung':
        return 'SATPOL PP Kota Bandung'
    
    else:
        return ''

def send_to(authorities):
    if authorities == 'dinas-kependudukan-dan-pencatatan-sipil-Kota-bandung':
        return 'bandung.disdukcapil@gmail.com'
    
    elif authorities == 'dinas-sumber-daya-air-dan-bina-marga-kota-bandung':
        return 'bandung.dsdabm@gmail.com'
    
    elif authorities == 'dinas-perhubungan-kota-bandung':
        return 'bdg.dishub@gmail.com'
    
    elif authorities == 'satuan-polisi-pamong-praja-Kota-bandung':
        return 'bandung.satpolpp@gmail.com'
    
    else:
        return ''
    

def send_email(sender, report, authorities):
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_email, password)
        # TODO: Send email here
        receiver_email = send_to(authorities)
        message = f"""\
        Subject: 

        Email from {sender} for {send_to_name(authorities)}

        {report}"""

        # Send email here

        # TODO: Send email here
        server.sendmail(sender_email, receiver_email, message)
        print('Sent!')