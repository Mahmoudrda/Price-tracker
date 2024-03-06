#libraries_used
from bs4 import BeautifulSoup
import requests
import pandas
import csv
import os
from datetime import date
from datetime import datetime
import time
import smtplib
#Getting the html from the website
url='https://www.noon.com/egypt-en/airpods-3rd-generation-with-lightning-charging-case-white/N53349332A/p/?o=fbb38064656b8f1c'
headers=({"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36","Accept-Language":"en-US,en;q=0.5"})
page=requests.get(url,headers=headers)
soup1=BeautifulSoup(page.text,'html.parser')
##Finding the data that we need
name=soup1.find("h1").text
price=soup1.find('div',class_='priceNow').text
price=price[4:9]
##Creating the csv file on the cwd
date_and_time=datetime.now()
date_and_time=date_and_time.strftime("%d/%m/%y %H:%M:%S")
hearders=['name','price','date and time']
data=[name,price,date_and_time]
with open('airpods price.csv','w',newline='',encoding='UTF8') as file:
    ##using .writer to create the file and insert the data for the first time
    writer=csv.writer(file)
    writer.writerow(hearders)
    writer.writerow(data)
## Creating a function to loop through
def check_price():
    url = 'https://www.noon.com/egypt-en/airpods-3rd-generation-with-lightning-charging-case-white/N53349332A/p/?o=fbb38064656b8f1c'
    headers = ({
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.5"})
    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.text, 'html.parser')
    name = soup1.find("h1").text
    price = soup1.find('div', class_='priceNow').text
    price = price[4:9]
    date_and_time = datetime.now()
    date_and_time = date_and_time.strftime("%d/%m/%y %H:%M:%S")
    hearders = ['name', 'price', 'date and time']
    data = [name, price, date_and_time]
    with open('airpods price.csv', 'a+', newline='', encoding='UTF8') as file:
        writer = csv.writer(file)
        writer.writerow(data)
def send_mail():
    ##defining the variables
    sender = 'mahmoud.reda.acc@gmail.com'
    password = 'ejdc yqbo tyel gmit'
    receiver = 'mahmoud.reda1277.hr@gmail.com'
    subject = 'IT IS A GOOD TIME TO GET AN AIRPODS'
    body = """ Go and check your apple airpods 3 on noon"""
    ## Creating the message using the subject and the body
    msg = f'subject:{subject}\n\n{body}'
    ## connecting to the server and logining in and then sending the message
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(sender, password)
        smtp.sendmail(sender, receiver, msg)
##looping through the function every 86400 seconds
while (True):
    check_price()
    if int(price) < 10000:
        send_mail()
    time.sleep(86400)





