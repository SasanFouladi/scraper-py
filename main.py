import smtplib
import time
import array
import datetime
from email.mime.text import MIMEText
from selenium import webdriver
from email.mime.multipart import MIMEMultipart
from bs4 import BeautifulSoup
import simplejson as json

dataFile = open("data.json", "r+")
data = json.loads(dataFile.read())
dataFile.close()

# Replace the url for your desired website
url = "https://ais.usvisa-info.com/en-ir?visa_type=niv"
receiver_mails = [
    # "ehsan.foolady@gmail.com",
    # "mehrdadzomorodiyan@gmail.com",
    # "babaktaheri77@gmail.com",
    "fouladi.sasan@yahoo.com"
]


def send_mail(receiver_mail):
    sender_mail = "fouladi.sasan2@gmail.com"
    # creates SMTP session
    s = smtplib.SMTP("smtp.gmail.com", 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login(sender_mail, "3169945454sF")

    # Instance of MIMEMultipart
    msg = MIMEMultipart("alternative")

    # Write the subject
    msg["Subject"] = "Some changes with cronjob"

    msg["From"] = sender_mail
    msg["To"] = receiver_mail

    # HTML body of the mail
    html = "<h2>click on this link and watch changes.</h2><br/><a href =" + url + ">Click here to visit.</a>"

    # Attach the HTML body with the msg instance
    msg.attach(MIMEText(html, "html"))

    # Sending the mail
    s.sendmail(sender_mail, receiver_mail, msg.as_string())
    s.quit()


ankara_before = data["ankara"]
yerevan_before = data["yerevan"]
dubai_before = data["dubai"]

# Send the get request to the website
driver = webdriver.Firefox()

# Go to your page url
driver.get(url)

button_element = driver.find_element_by_name('commit')
button_element.click()
time.sleep(5)
soup = BeautifulSoup(driver.page_source, "html.parser")
driver.close()

result = []
for field in soup.find_all("li"):
    if "Student Visas:" in field.text:
        result.append(field.text)

(dubai_after, yerevan_after, ankara_after) = result

if ankara_before.strip() != ankara_after.strip() or yerevan_before.strip() != yerevan_after.strip() or dubai_before.strip() != dubai_after.strip():

    for mail in receiver_mails:
        send_mail(mail)

    dataFile = open("data.json", "w+")
    data = {
        "ankara": ankara_after.strip(),
        "yerevan": yerevan_after.strip(),
        "dubai": dubai_after.strip()
    }
    dataFile.seek(0)
    dataFile.write(json.dumps(data))
    dataFile.close()
    now = datetime.datetime.now()
    print("send email at : " + now.strftime("%Y-%m-%d %H:%M:%S"))
