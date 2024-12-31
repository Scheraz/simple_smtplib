import smtplib
import datetime as dt
import random

quote_list = []
with open("quotes.txt", "r") as file:
    for quote in file:
        quote_list.append(quote)

random_quote = random.choice(quote_list)

now = dt.datetime.now()
weekday = now.weekday()

email = "test@gmail.com"
password = "xxxxxxxxxxxxxx"
out_email = "test@outlook.com"

if weekday in range(0,5):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email, to_addrs=out_email, msg=f"Subject: Motivation Quotes\n\n{random_quote}")






















# import smtplib
# import datetime as dt
# # my_email = "sherazkhanpk.sk@gmail.com"
# # password = "ftjv vqur bdnx gulr"
# # rec_email = "heysheraz@outlook.com"
# # with smtplib.SMTP("smtp.gmail.com") as connection:
# #     connection.starttls()
# #     connection.login(user=my_email, password=password)
# #     connection.sendmail(from_addr=my_email,
# #                         to_addrs=rec_email,
# #                         msg="Subject:Hello\n\nThis is the body of my email")
#
#
# time = dt.datetime.now()
# print(time)

