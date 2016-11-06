def send_mail(send_from, to, comments):
    import smtplib

    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    # me == my email address
    # you == recipient's email address
    if not send_from:
        send_from = "pretty.shivani29@tomakis.com"
    if not to:
        to = "junuarora@gmail.com"

    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Dynamic Quote Request"
    msg['From'] = send_from
    msg['To'] = to
    import ipdb
    ipdb.set_trace()

    # Create the body of the message (a plain-text and an HTML version).
    text = "Dear Abhinav,\n\nWe have received mails from our user stating that 'Mock one of Tomakis is closet to actual CAT 14 paper'.\n\nWe have Mocks open for all students.\n\nTo know more, log on www.tomakis.com\n\nSeven free Mock Tests: Know your estimated percentile for CAT'14! \n\nThanks,\nTomakis Team"
    html = """\
    <html>
        <head></head>
           <body>
                <p>Dear Abhinav,</p>
                <p>We have received mails from our user stating that "Mock one of Tomakis is closet to actual CAT 14 paper".</p>
                <p>We have Mocks open for all students</p>
                <p>To know more, log on www.tomakis.com</p>
                <p><b>Seven free Mock Tests: Know your estimated percentile for CAT'14!</b></p>
                <p>Thanks,<br/>Tomakis Team</p>
           </body>
    </html>
    """

    # Record the MIME types of both parts - text/plain and text/html.
    if not comments:
        part1 = MIMEText(text, 'plain')
        part2 = MIMEText(html, 'html')
    else:
        part1 = MIMEText(comments, 'plain')
        part2 = MIMEText(comments, 'html')
    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part1)
    msg.attach(part2)

    # Send the message via local SMTP server.
    s = smtplib.SMTP('localhost')
    # sendmail function takes 3 arguments: sender's address, recipient's address
    # and message to send - here it is sent as one string.
    s.sendmail(send_from, to, msg.as_string())
    s.quit()
