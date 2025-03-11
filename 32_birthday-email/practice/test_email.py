import smtplib
from os import getenv
from dotenv import load_dotenv

load_dotenv(override=True)

my_email = getenv("target_mail")
pw = getenv("my_pw2")
SMTP = getenv("SMTP")

# connection = smtplib.SMTP(SMTP, port=587)
with smtplib.SMTP(SMTP, port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=pw)
    connection.sendmail(from_addr=my_email,
                        to_addrs=my_email,
                        msg="Subject:Test email\n\n"  # 'Subject:' is key, just as the 2 new lines
                            "This is the body of the email.")
# connection.close()
