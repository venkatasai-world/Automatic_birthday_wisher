import smtplib
import datetime as dt
import random
import pandas as pd

mail = "merugusai112233@gmail.com"
password = "xdphntxmdhngdilh"   # must be Gmail App Password

today = dt.datetime.now()
today_tuple = (today.month, today.day)

data = pd.read_csv(r"Automatic_email\birthdays.csv")
birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"Automatic_email\\letter_templates\\letter_{random.randint(1, 3)}.txt"
    with open(file_path) as file:
        contents = file.read()
        contents = contents.replace("[NAME]", birthday_person['name'])

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=mail, password=password)
        connection.sendmail(
            from_addr=mail,
            to_addrs=birthday_person['email'],
            msg=f"Subject: Happy Birthday!\n\n{contents}"
        )
