import requests  
import urllib3 
from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By



def Interests_Prof(driver):
#Entra a otro link
    linkedIn_profile = 'https://www.linkedin.com/in/romario-julio-91a610113/details/interests/?detailScreenTabIndex=0'
    driver.get(linkedIn_profile)

    time.sleep (10)

    data = driver.page_source
    bsoup = BeautifulSoup(data, 'lxml')

    #Intereses Empresas

    name_DIV = []

    name_DIV = bsoup.find('div',{'class':'artdeco-tabpanel active ember-view'}).text.replace("\n", " ")
    print(name_DIV)

#Hacer scroll hasta la última parte.

#S_PAUSE= 0.5
#last_height = driver.execute_script("return document.body.scrollHeight")


#while True:

    #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    #Espera que cargue la página
    #time.sleep(S_PAUSE)

    #calcula el nuevo scroll height

    #new_height = driver.execute_script("return document.body.scrollHeight")

    #if new_height == last_height:

       # break
    #last_height = new_height
#last_height = driver.execute_script("return document.body.scrollHeight")

#Segundo intento de scrolldown

#footer_html = driver.find_element_by_tag_name('html')

#footer_html.send_keys(Keys.END)

#time.sleep(20)



#name_div = name_DIV.find('div', {'class': 'artdeco-tabpanel artdeco-tabpanel--hidden ember-view'})
#name_li = name_div.find('li')
#button = driver.find_element_by_class_name('artdeco-button artdeco-button--muted artdeco-button--1 artdeco-button--full artdeco-button--secondary ember-view scaffold-finite-scroll__load-button')



#Intereses Instituciones educativas
#butn = driver.find_element_by_class_name('artdeco-tabpanel artdeco-tabpanel--hidden ember-view')

#print(butn)

