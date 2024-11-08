import time, os
from selenium import webdriver
import pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager as CM
from selenium.common.exceptions import NoSuchElementException
from linkedin_scraper import Person
from pywinauto.keyboard import send_keys
import mysql.connector
import os
import img2pdf
import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import keyboard
import numpy as np
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
ins_usr=input('enter insta username- ')
tw_usr=input('enter twitter username- ')
ins_idd='qwrt4278'
tw_idd='sksskstcs'
passs='1@TESTPASS'
ins_data=[]
tw_data=[]
fb_data=[]
tw_po_url=[]
fb_po_url=[]
ins_po_url=[]
driver = webdriver.Chrome()
driver.get('https://www.instagram.com/accounts/login/')
try:
    driver.find_element(By.XPATH,"/html/body/div[4]/div/div/div[3]/div[2]/button").click()
except:
    pass
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']"))).send_keys(ins_idd)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']"))).send_keys(passs)
WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
time.sleep(10)
driver.get('https://www.instagram.com/{}'.format(ins_usr))
time.sleep(5)
for ii in range(0,10):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(5)
x=driver.find_elements(By.TAG_NAME,'a')
for i in x:
    z=i.get_attribute('href')
    if 'https://www.instagram.com/p/' in z:
        if z not in ins_po_url:
            ins_po_url.append(z)
driver.quit()
options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument("--log-level=3")
mobile_emulation = { "deviceName": "Samsung Galaxy S20 Ultra" }
options.add_experimental_option("mobileEmulation", mobile_emulation)
driver = webdriver.Chrome(options=options)
driver.get('https://www.instagram.com/accounts/login/')
try:
    driver.find_element(By.XPATH,"/html/body/div[4]/div/div/div[3]/div[2]/button").click()
except:
    pass
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']"))).send_keys(ins_idd)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']"))).send_keys(passs)
WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
time.sleep(10)
for ln in range(0,len(ins_po_url)):
    link=ins_po_url[ln]
    driver.get(link+'comments/')
    time.sleep(5)
    #driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div[3]/div/div[1]/div/div[1]/span[2]/div').click()
    #time.sleep(5)
    for i in range(0,1):
        #driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        x=driver.find_elements(By.CLASS_NAME,'xurb0ha')
        for i in x:
            try:
                z=i.text
                z=z.split('\n')
                if z not in ins_data:
                    ins_data.append(['instagram',link,z[0],z[1]])
            except:
                pass
driver.quit()

driver = webdriver.Chrome()
driver.get('https://twitter.com/i/flow/login')
time.sleep(10)
driver.find_element(By.XPATH,'/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input').send_keys(tw_idd)
driver.find_element(By.XPATH,'/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]').click()
time.sleep(10)
driver.find_element(By.XPATH,'/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input').send_keys(passs)
driver.find_element(By.XPATH,'/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div').click()
time.sleep(10)
driver.get(f'https://twitter.com/{tw_usr}')
for i in range(0,2):
    er=i
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(3)
    ee=driver.find_elements(By.TAG_NAME,"a")
    zz=[]
    for i in ee:
        zz.append(i.get_attribute('href'))
    for i in zz:
        if '/status/' in i:
            if 'analytics' in i:
                pass
            elif 'photo' in i:
                pass
            elif 'video' in i:
                pass
            else:
                if i not in link:
                    tw_po_url.append(i)
tem_data=[]
for i in tw_po_url:
    lc=i
    driver.get(i)
    time.sleep(10)
    for i in range(0,10):
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(10)
        x=driver.find_elements(By.CLASS_NAME,'css-901oao.css-16my406.r-poiln3.r-bcqeeo.r-qvutc0')
        for i in x:
            try:
                tem_data.append(i.text)
            except:
                pass
        index=[]
        for i in range(0,len(tem_data)):
            if tem_data[i]=='·':
                index.append(i)
        
        for i in index:
            if ['twitter',lc,tem_data[i-1],tem_data[i+1]] not in tw_data:
                tw_data.append(['twitter',lc,tem_data[i-1],tem_data[i+1]])

driver.quit()
#driver = webdriver.Chrome()
#driver.get('https://twitter.com/i/flow/login')
pw=[]
nw=[]
t_point=[]
x=pd.read_excel('keywords.xlsx')
for i in x[0]:
    pw.append(i)
for i in x[1]:
    nw.append(i)
for i in ins_data:
    point=0
    para=i[-1]
    word_tokenize(para)
    sentense = word_tokenize(para)
    word_features = []
    for i,j in nltk.pos_tag(sentense):
        if j in ['JJ', 'JJR', 'JJS', 'RB', 'RBR', 'RBS']:
            word_features.append(i)
    for wd in pw:
        if wd in word_features:
            point=point+1
    for wd in nw:
        if wd in word_features:
            point=point-1
    
    if point<0:
        t_point.append('neg')
    elif point>0:
        t_point.append('pos')
    else:
        t_point.append('neu')
insta=[t_point.count('pos'),t_point.count('neg')]
ins_full=[len(ins_data),t_point.count('pos'),t_point.count('neg'),t_point.count('neu')]
print('total comments read- ',len(ins_data))
print('total positive comments- ',t_point.count('pos'))
print('total negative comments- ',t_point.count('neg'))
print('total neutral comments- ',t_point.count('neu'))
t_point=[]
for i in tw_data:
    point=0
    para=i[-1]
    word_tokenize(para)
    sentense = word_tokenize(para)
    word_features = []
    for i,j in nltk.pos_tag(sentense):
        if j in ['JJ', 'JJR', 'JJS', 'RB', 'RBR', 'RBS']:
            word_features.append(i)
    for wd in pw:
        if wd in word_features:
            point=point+1
    for wd in nw:
        if wd in word_features:
            point=point-1
    
    if point<0:
        t_point.append('neg')
    elif point>0:
        t_point.append('pos')
    else:
        t_point.append('neu')
twitter=[t_point.count('pos'),t_point.count('neg')]
tw_full=[len(tw_data),t_point.count('pos'),t_point.count('neg'),t_point.count('neu')]
print('total comments read- ',len(tw_data))
print('total positive comments- ',t_point.count('pos'))
print('total negative comments- ',t_point.count('neg'))
print('total neutral comments- ',t_point.count('neu'))
#df=pd.DataFrame(data)
#df.to_excel('comments.xlsx')

barWidth = 0.25
fig = plt.subplots(figsize =(12, 8))
y = np.array([insta[0]+twitter[0],insta[1]+twitter[1]])
mylabels = ["positive", "negative"]
plt.pie(y, labels = mylabels)
plt.savefig(f'{ins_usr} pie chart')
plt.clf()

br1 = np.arange(len(twitter))
br2 = [x + barWidth for x in br1]
plt.bar(br2, twitter, color ='g', width = barWidth,edgecolor ='grey', label ='positive')
plt.bar(br1, insta, color ='r', width = barWidth,edgecolor ='grey', label ='negative')       
plt.xlabel('sites', fontweight ='bold', fontsize = 15)
plt.ylabel('comments', fontweight ='bold', fontsize = 15)
plt.xticks([r + barWidth for r in range(len(insta))],[ 'twitter','insta'])
plt.legend()
plt.savefig(f'{ins_usr} bar graph')
image_files = [f'{ins_usr} pie chart.png',f'{ins_usr} bar graph.png']
pdf_data = img2pdf.convert(image_files)
with open("graps.pdf", "wb") as file:
    file.write(pdf_data)
f_data=[['no of comments','positive','negative','neutral'],ins_full,tw_full]
df=pd.DataFrame(f_data)
df.to_excel('all data.xlsx')