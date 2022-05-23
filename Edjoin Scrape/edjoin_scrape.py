from pandas.io import json
import requests
import urllib.request
import json
import pandas as pd
import http.client


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
        'salaryInfo',
        'beginningSalary',	
        'endingSalary',
        'countyName',
        'districtName',
        'city',
        'zip',
        'numberOpenings',
        'postingInformation',
        'State',
        'fullCountyName',
    ]]
    df1.to_csv('output')

