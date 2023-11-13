import smtplib
import datetime as dt
import random

my_email = ""
password = ""

now = dt.datetime.now()
weekday = now.weekday()
# 0 is for monday, 1 for Tuesday, 2 for Wednesday, and so on...
if weekday == 0:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="[enter the recipient's email here]",
                            msg=f"Subject:Did you get it\n\n{quote}")

