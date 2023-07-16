from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import sys, time
#import numpy as np
#import scipy.interpolate as si
from datetime import datetime
from time import sleep, time
from random import uniform, randint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary






#options = webdriver.FirefoxOptions()
#options.add_argument('useAutomationExtension')
#options.set_preference(options.capabilities.values())
#self.options.headless = self.headless

#capabilities = webdriver.DesiredCapabilities.FIREFOX
#capabilities['marionette'] = True










#profile_path='/home/stone/.mozilla/firefox/zi1vh5qb.default-release'
#profile = webdriver.FirefoxProfile(profile_path)
#profile.add_extension('/home/stone/.mozilla/firefox/zi1vh5qb.default-release/extensions/{e58d3966-3d76-4cd9-8552-1582fbc800c1}.xpi')

#options = Options()
#options.add_argument(options.capabilities.values())

#options.set_preference('profile', profile_path)

#service = Service('/usr/local/bin/')

driver = webdriver.Firefox()
#profile=self.setUpProfile()
#options=self.setUpOptions()
#capabilities=self.setUpCapabilities()
wait = WebDriverWait(driver, 12)
#driver = webdriver.Firefox(options=self.options, capabilities=capabilities, ) 


url="https://www.squaretrade.com/phone-protection/?gad=1&gclid=EAIaIQobChMI3sKr3L-__gIV7QGtBh1V4gA3EAAYASAAEgLAePD_BwE"
driver.get(url)
a = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@class='primary-button']")))
a.click()
b = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@class='primary-button upsell-product upsell-upgrade-now']")))
b.click()
c = wait.until(EC.presence_of_element_located((By.XPATH,"//input[@id='firstName']")))
        #c.click()
c.send_keys("Edmundo")
ad = wait.until(EC.presence_of_element_located((By.XPATH,"//input[@id='lastName']")))
ad.send_keys('Dantes')
                #sleep(2)
dirc=wait.until(EC.presence_of_element_located((By.XPATH,"//input[@id='address']")))
dirc.send_keys("171 ft fulton")
                #sleep(2)
esta=wait.until(EC.presence_of_element_located((By.XPATH,"//option[@value='6: CO']")))
esta.send_keys("Colorado")
sleep(2)
cp = wait.until(EC.presence_of_element_located((By.XPATH,"//input[@id='zipcode']")))
cp.send_keys('80010')
phone = wait.until(EC.presence_of_element_located((By.XPATH,"//input[@id='phone']")))
phone.send_keys('3026034793')
sleep(2)
email = wait.until(EC.presence_of_element_located((By.XPATH,"//input[@id='email']")))
email.send_keys('xelastone@net.org')
viv='4147097552945323'
mes='05'
ano='25'
cvc='247'
cc = wait.until(EC.presence_of_element_located((By.XPATH,"//input[@id='creditcard']")))
action = ActionChains(driver)
action.send_keys(Keys.TAB)
action.send_keys(Keys.TAB)
action.send_keys(viv[:4])
action.send_keys(Keys.SPACE)
action.send_keys(viv[4:8])
action.send_keys(viv[8:12])
action.send_keys(viv[12:16])
action.perform()
fecha = wait.until(EC.presence_of_element_located((By.XPATH,"//input[@id='mmyy']")))
fecha.send_keys(mes+'/20'+ano)
cvv = wait.until(EC.presence_of_element_located((By.XPATH,"//input[@id='cvc']")))
cvv.send_keys(cvc)
checker=wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@class='btn btn-primary btn-block btn-purchase']")))
checker.click()
#               bys=wait.until(EC.presence_of_element_localed((By.XPATH,"iframe")))
                #driver.switch_to.default_content()
iframes = driver.find_elements(By.XPATH,"/html/body/div[2]/div[2]/iframe")
driver.switch_to.frame(iframes[0])

ch=wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@id='recaptcha-audio-button']")))
ch.click()
driver.implicitly_wait(10)
driver.switch_to.default_content()
#iframes = driver.find_elements(By.XPATH,"/html/body/div[2]/div[2]/iframe")
driver.switch_to.frame(iframes[0])
pas=wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@id='solver-button']")))
pas.click()


driver.implicitly_wait(10)
driver.switch_to.default_content()
#iframes = driver.find_elements(By.XPATH,"/html/body/div[2]/div[2]/iframe")
driver.switch_to.frame(iframes[0])
pase=wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='solver-button']")))
pase.click()


#iframes = driver.find_elements(By.XPATH,"/html/body/div[2]/div[2]/iframe")
#driver.switch_to.frame(iframes[0])

#boot=wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div/div/div[8]/div[2]/div[1]/div[1]/div[4][@id='solver-button']")))
#boot.click()

#id="solver-button"
#driver.switch_to.default_content()

#d=/html/body/app-root/st-message-overlay/div/div/st-loading-indicator/div/div/st-checkout/st-global-style/div/div/div/form/st-payment-form/form/div[2]


rechazo=wait.until(EC.presence_of_element_located((By.XPATH,"//div[@class='col-md-12 paymentFailure']")))

import os
if rechazo:
	print('VIVA')
else:
	os.system('python ext.py')
