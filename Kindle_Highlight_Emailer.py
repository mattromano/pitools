import requests
import datetime
import pandas as pd
import json
import gmail_stuff as gs
import smtplib


def get_highlights():
    url_key = "https://readwise.io/api/v2/highlights"
    response = []

    return requests.get(
        url=url_key,
        headers={
            "Authorization": "Token imQzpdzXmFrWM0z9EjbMteDugRXh3vBFfWkeiObptBmZyBIKVc"
        },
    )


def get_books():

    querystring = {
        "category": "books",
    }

    return requests.get(
        url="https://readwise.io/api/v2/books/",
        headers={
            "Authorization": "Token imQzpdzXmFrWM0z9EjbMteDugRXh3vBFfWkeiObptBmZyBIKVc"
        },
        params=querystring,
    )


data = get_highlights()
books = get_books().json()
df2 = pd.json_normalize(books, "results", max_level=0)
df2.to_csv("books.csv")

data = data.json()
df1 = pd.json_normalize(data, "results", max_level=0)
df1 = df1.iloc[[4, 9]]
df1 = df1.merge(df2, left_on="book_id", right_on="id", how="left", indicator=True)
print(df1)

df1.to_csv("readwise_export.csv")


def send_email(user, password, text_body):
    sent_from = user
    to = "mattromano88@gmail.com"
    subject = "Book Name 1 & 2 Quotes for u"
    body = text_body

    email_text = """\
    From: %s
    Subject: book1 and book2 for u

    %s
    """ % (
        sent_from,
        # subject,
        body,
    )

    try:
        smtp_server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        smtp_server.ehlo()
        smtp_server.login(user, password)
        smtp_server.sendmail(sent_from, to, email_text)
        smtp_server.close()
        print("Email sent successfully!")
    except Exception as ex:
        print("Something went wrong….", ex)


send_email(gs.gmail_user, gs.gmail_password, "god damn this will be cool if it works")
