# import module
from unittest import skip
import pandas as pd
import requests
from bs4 import BeautifulSoup
import json
  
HEADERS = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) \
            Chrome/90.0.4430.212 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})
  
# user define function
# Scrape the data
def getdata(url):
    r = requests.get(url, headers=HEADERS)
    return r.text
  
  
def html_code(url):
  
    # pass the url
    # into getdata function
    htmldata = getdata(url)
    soup = BeautifulSoup(htmldata, 'html.parser')
  
    # display html code
    return (soup)
  
  
url = "https://www.amazon.in/crocs-Dark-Gold-Flip-Flops-206108-277/dp/B08D8QR8KZ/ref=sr_1_19?dchild=1&pf_rd_i=15325111031&pf_rd_m=A1K21FY43GMZF8&pf_rd_p=19b7420f-03b6-40a1-8197-83afd336eb3d&pf_rd_r=SF24BH1WBMRYKHG4N0TM&pf_rd_s=merchandised-search-9&pf_rd_t=101&qid=1635456476&qsid=257-3376808-3767020&refinements=p_n_specials_match%3A21618256031&s=shoes&sr=1-19&sres=B074CZZQ8V%2CB08DXGDQF2%2CB01HQAXOWW%2CB07FDF34HD%2CB012TRTIYA%2CB0999KG1KG%2CB08YFDKPRL%2CB08T6HV71P%2CB08W5212QJ%2CB08JVZDC7Z%2CB09GKT3XS8%2CB072PXKZL2%2CB08KZQV69B%2CB089ZQPF2K%2CB085M7T95G%2CB08WKJG8WY%2CB08K73CCPX%2CB0965N8LP1%2CB08D8QR8KZ%2CB06XJ55FBC&th=1"
  
soup = html_code(url)


def cus_data(soup):
    # find the Html tag
    # with find()
    # and convert into string
    data_str = ""
    cus_list = []
  
    for item in soup.find_all("span", class_="a-profile-name"):
        data_str = data_str + item.get_text()
        cus_list.append(data_str)
        data_str = ""
    return cus_list
  
  
cus_res = cus_data(soup)
cus_len = len(cus_res)



def cus_rev(soup):
    # find the Html tag
    # with find()
    # and convert into string
    data_str = ""
  
    for item in soup.find_all("div", class_="a-expander-content reviewText review-text-content a-expander-partial-collapse-content"):
        data_str = data_str + item.get_text()
  
    result = data_str.split("\n")
    return (result)
  
  
rev_data = cus_rev(soup)
rev_result = []
for i in rev_data:
    if i is "":
        pass
    else:
        rev_result.append(i)

data = {"Name":cus_res, "Review":rev_result}






dict = json.dumps(data)
print(dict)