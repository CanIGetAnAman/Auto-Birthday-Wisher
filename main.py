import datetime as dt
import pandas
import random
import smtplib
MY_EMAIL = "parketest.email@gmail.com"
PASSWORD = "obcfyanswcedwuby"

random_letter_num = random.randint(1, 3)
now = dt.datetime.now()
month = now.month
day = now.day

birthdays_df = pandas.read_csv("birthdays.csv")

for index, row in birthdays_df.iterrows():
    if row["month"] == month:
        if row["day"] == day:
            name = row["name"]
            email = row["email"]
            with open(f"letter_templates/letter_{random_letter_num}.txt") as file:
                random_letter = file.read()
                birthday_letter = random_letter.replace("[NAME]", name)
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:Happy Birthday\n\n{birthday_letter}"
                )

