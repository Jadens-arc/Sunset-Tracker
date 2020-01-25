import smtplib, time, datetime
from astral import Astral


a = Astral()
a.solar_depression = 'civil'


city = a['Las Vegas']



class EmailClient:
    def __init__(self, user_address, user_password):
        self.user_address = user_address
        self.user_password = user_password

        self.s = smtplib.SMTP('smtp.gmail.com', 587)
        self.s.starttls()
    def send(self, receiver, message):
        self.s.login(self.user_address, self.user_password)
        self.s.sendmail(self.user_address, receiver, message)


while True:
    sun = city.sun(date = datetime.datetime.now(), local = True)
    sunset  = (str(sun['sunset']))
    sunset = sunset[:-6]

    current = str(datetime.datetime.now())
    current = current[:-7]

    if current == sunset:
        gmail = EmailClient('maxtnter64@gmail.com', 'kqjmqpympfqrmhov')
        gmail.send('arceneauxjaden@gmail.com', "it's sunset")
        print('its time')
        with open('sunsets.txt', 'a') as sunFile:
            sunFile.write("it's sunsets at " + str(datetime.datetime.now()) + "\n")
    else:
        print('not time ' + str(datetime.datetime.now()))


    time.sleep(1)
