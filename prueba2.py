

import requests  
from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def Profile_Inf(driver):

    linkedIn_profile = 'https://www.linkedin.com/in/romario-julio-91a610113/'
    driver.get(linkedIn_profile)

    data = driver.page_source
    bsoup = BeautifulSoup(data, 'lxml')


    #webScraping de información personal

    name_profile = bsoup.find('h1',{'class':'text-heading-xlarge inline t-24 v-align-middle break-words'}).text
    mediumText_profile = bsoup.find('div',{'class':'text-body-medium break-words'}).text
    companyEducation_profile = bsoup.find('h2',{'class':'pv-text-details__right-panel-item-text hoverable-link-text break-words text-body-small inline'} ).text
    smallText_profile = bsoup.find('span',{'class':'text-body-small inline t-black--light break-words'}).text
    contacts_profile =bsoup.find('span',{'class':'t-bold'}).text
    #Link_profile = bsoup.find('div',{'class':'pv-contact-info__ci-container t-14'}).text

    #companyEducation_profile = companyEducation_profile.rstrip('\n')

    info_main = []
    info_main.append(linkedIn_profile)
    info_main.append(mediumText_profile)
    info_main.append(companyEducation_profile)
    info_main.append(smallText_profile)
    info_main.append(contacts_profile)

    print(info_main)