from pandas.io import json
import requests
import urllib.request
import smtplib
import gmail as gs
import json
import tabulate
import pandas as pd
import http.client
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



def get_job_list():
    conn = http.client.HTTPSConnection("www.edjoin.org")

    payload = ""

    headers = {
        'cookie': "BNI_persistence=AiQgNKaoYQ5uB4348ZXiZdbbllysd6Zt7PjDzy_iPnuoFPuKuDUyYG7qp5y5XJ23fhcloMkrdT38rsqvGrAISg%3D%3D",
        'Accept': "*/*",
        'Accept-Language': "en-US,en;q=0.9",
        'Connection': "keep-alive",
        'Cookie': "BNI_persistence=AiQgNKaoYQ5uB4348ZXiZdbbllysd6Zt7PjDzy_iPnuoFPuKuDUyYG7qp5y5XJ23fhcloMkrdT38rsqvGrAISg==",
        'Referer': "https://www.edjoin.org/Home/Jobs?keywords=&searchType=all&states=24&regions=19&jobTypes=2&days=5&onlineApps=false",
        'Sec-Fetch-Dest': "empty",
        'Sec-Fetch-Mode': "cors",
        'Sec-Fetch-Site': "same-origin",
        'Sec-GPC': "1",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36",
        'X-Requested-With': "XMLHttpRequest"
        }

    conn.request("GET", "/Home/LoadJobs?rows=10&page=1&sort=postingDate&order=desc&keywords=&searchType=all&states=24&regions=19&jobTypes=2&days=14&catID=0&onlineApps=false&recruitmentCenterID=0&stateID=0&regionID=0&districtID=0&countyID=0&searchID=0&_=1653314910460", payload, headers)


    res = conn.getresponse()
    data = res.read()
    data = data.decode("utf-8")
    type(data)
    data = json.loads(data)
    #print(data)
    print(type(data))

    df1 = pd.json_normalize(data)
    #df1 = df1.transpose()
    df1 = df1['data'][0]
    df1 = pd.DataFrame(df1)
    df1 = df1[[
        'postingID',
        'positionTitle',
        # 'salaryInfo',
        # 'beginningSalary',	
        # 'endingSalary',
        'countyName',
        'districtName',
        'city',
        'zip',
        'numberOpenings',
        'postingInformation',
        'State',
        'fullCountyName',
    ]]

    return df1

def new_posting_check(df1):
    df2 = pd.read_csv('output.csv')
    df1 = df1.merge(
        df2,
        left_on='postingID',
        right_on = 'postingID',
        how = 'left',
        indicator = True
    )
    df1 = df1[df1['_merge'] != 'both']
    df1.to_csv('output2.csv')

def create_and_send_email(df1):
    new_job_count = len(df1)
    job_table_text = df1.to_string(index = False)
    job_table_html = df1.to_html()
    email_body_text = '''
    There are {} new jobs since last refresh.
    
    The new jobs are:
    {}
    '''.format(new_job_count,job_table_text)

    email_body_html = job_table_html
    #email_body = email_body.format(job_table.to_html())

    sent_from = gs.gmail_user
    to = "mattromano88@gmail.com"
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "{} New Edjoin Jobs".format(new_job_count)
    msg['From'] = sent_from
    msg['To'] = to
    text = email_body_text
    html = job_table_html

    try:
        part1 = MIMEText(text, 'plain')
        part2 = MIMEText(html, 'html')
        msg.attach(part1)
        msg.attach(part2)
        smtp_server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        smtp_server.ehlo()
        smtp_server.login(gs.gmail_user, gs.gmail_password)
        smtp_server.sendmail(sent_from, to, msg.as_string())
        smtp_server.close()
        print("Email sent successfully!")
    except Exception as ex:
        print("Something went wrong….", ex)



df1 = get_job_list()
new_posting_check(df1)
email_body = create_and_send_email(df1)
