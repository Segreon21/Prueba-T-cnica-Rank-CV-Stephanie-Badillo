from pydoc import locate
import requests  
import urllib3 
from selenium import webdriver
from bs4 import BeautifulSoup
import time
from time import sleep
from random import randint
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from Intereses import Interests_Prof
from prueba2 import Profile_Inf


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')

driver = webdriver.Chrome(executable_path=r"/usr/local/share/chromedriver", options=chrome_options)
driver.get("https://www.linkedin.com/")

element_USER = driver.find_element_by_xpath('//input[@name="session_key"]')
element_USER.send_keys('Romarioajb@outlook.com')
element_PASS = driver.find_element_by_xpath('//input[@name="session_password"]')
element_PASS.send_keys('Romario1994....')
element_BUTN = driver.find_element_by_xpath('//*[@id="main-content"]/section[1]/div/div/form/button').click()

#Información personal
Profile_Inf(driver)

#Información de intereses
Interests_Prof(driver) 