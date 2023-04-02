import smtplib

EMAIL, PASSWORD = "email@gmail.com", "Th1s-!s-RandomPassw06d"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=EMAIL, password=PASSWORD)
connection.sendmail(from_addr=EMAIL, to_addrs='receiver@gmail.com', msg="Subject:Hello\n\nthis is trail")
connection.close()

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=EMAIL, password=PASSWORD)
    connection.sendmail(from_addr=EMAIL, to_addrs='receiver@gmail.com', msg="Subject:Hello\n\nthis is trail")