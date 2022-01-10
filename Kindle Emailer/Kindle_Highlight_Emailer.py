import requests
import datetime
import pandas as pd
import json
import gmail as gs
import smtplib
import random


def get_highlights():
    url_key = "https://readwise.io/api/v2/highlights"
    response = []
    querystring = {
        "page_size" : 1000
    }

    return requests.get(
        url=url_key,
        headers={
            "Authorization": "Token imQzpdzXmFrWM0z9EjbMteDugRXh3vBFfWkeiObptBmZyBIKVc"
        },
        params=querystring
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

def convert_to_email(data,books):
    df2 = pd.json_normalize(books, "results", max_level=0)
    
    data = data.json()
    df1 = pd.json_normalize(data, "results", max_level=0)
    df1 = df1[df1['book_id'] != 10962843]
    random1 = random.randrange(0,len(df1))
    random2 = random.randrange(0,len(df1))
    df1 = df1.iloc[[random1, random2]]
    df1 = df1.merge(
        df2, 
        left_on="book_id", 
        right_on="id", 
        how="left", 
        indicator=True)
    quote1 = df1['text'][0]
    book1 = df1['title'][0]
    quote2 = df1['text'][1]
    book2 = df1['title'][1]
    BQ = '''
    Title: {}
    Quote: {}

    Title: {}
    Quote: {}
    '''.format(book1,quote1,book2,quote2)
    return BQ

#print(convert_to_email(data,books))
text_body = convert_to_email(data,books)

def send_email(user, password, text_body):
    sent_from = user
    to = "mattromano88@gmail.com"
    body = text_body.encode('ascii', 'ignore').decode('ascii')
    print(body)
    email_text = """\
    From: %s \r\n
    Subject: \r\n
    %s
    """ % (
        sent_from,
        body,
    )

    try:
        smtp_server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        smtp_server.ehlo()
        smtp_server.login(user, password)
        smtp_server.sendmail(
            sent_from,
            to, 
            email_text 
            #mail_options=('SMTPUTF8')
        )
        smtp_server.close()
        print("Email sent successfully!")
    except Exception as ex:
        print("Something went wrong….", ex)


send_email(gs.gmail_user, gs.gmail_password, text_body)
