import requests
import datetime as dt
import smtplib
from email.message import EmailMessage
import time
from dotenv import load_dotenv
import os
load_dotenv()

email = os.getenv('EMAIL')
password = os.getenv('PASSWORD')
email_to = os.getenv('EMAIL_TO')
print(f"EMAIL: {email}")
print(f"PASSWORD: {'loaded' if password else 'NOT loaded'}")
print(f"EMAIL_TO: {email_to}")


MY_LATITUDE = 17.2502
MY_LONGITUDE = 80.1760

def is_iss_overhead():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    iss_data = response.json()
    
    latitude = float(iss_data['iss_position']['latitude'])
    longitude = float(iss_data['iss_position']['longitude'])

    if abs(MY_LATITUDE - latitude) <= 5 and abs(MY_LONGITUDE - longitude) <= 5:
        return True
    return False

def is_night():
    parameters = {
        "lat": MY_LATITUDE,
        "lng": MY_LONGITUDE,
        "formatted": 0
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = dt.datetime.utcnow().hour

    if time_now >= sunset or time_now <= sunrise:
        return True
    return False

while True:
    if is_iss_overhead() and is_night():
        msg = EmailMessage()
        msg.set_content("Hey! The ISS is overhead and it's dark outside. Go take a look!")
        msg['Subject'] = "Look up! ISS is passing overhead"
        msg["From"] = email
        msg["To"] = email_to
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(email, password)
            smtp.send_message(msg)
    else:
        print("Not overhead or not dark yet.")

    time.sleep(60)
