import smtplib

# receiving number
NUMBER = 'YOUR NUMBER'
# SMS gateways for each carrier.
# the google voice is specific to the conversation between the receiving number and the GV number
carriers = {
    'att': '@mms.att.net',
    'tmobile': '@tmomail.net',
    'verizon': '@vtext.com',
    'sprint': '@page.nextel.com',
    'google_voice': 'text_thrad_code@txt.voice.google.com'
}

def send(message):
    # Replace the number with your own
    to_number = 'GOOGLE_VOICE_NUMBER.{}{}'.format(NUMBER, carriers['google_voice'])

    # authentication using specific google credentials,
    # note that if using google voice, this must be the same email used for voice number
    auth = ('romynashwood', 'Lunafazes15')

    # Establish a secure session with gmail's outgoing SMTP server using your gmail account
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(auth[0], auth[1])
    # Send text message through SMS gateway of destination number
    server.sendmail(auth[0], to_number, message)
