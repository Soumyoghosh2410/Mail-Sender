#getting introduced to automated mail system
'''import smtplib

my_email = "soumyo.ghosh24102003@gmail.com"
password = "odvfdiylqtwqfydw"

connection = smtplib.SMTP("smtp.gmail.com")
#making the connection secure
connection.starttls()
connection.login(user = my_email, password = password)
connection.sendmail(from_addr = my_email, to_addrs="soumyo.ghosh2021@vitstudent.ac.in", msg="Hello")
connection.close()

#using vit wifi causes connection error
import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(day_of_week)

date_of_birth = dt.datetime
'''

import smtplib
import datetime as dt
import random

my_email = "soumyo.ghosh24102003@gmail.com"
my_password = " "

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 1:  #weekday = 1 means monday, weekday = 2 means tuesday
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("SMTP.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email, msg = f"subject: Monday Motivation\n\n{quote}")

