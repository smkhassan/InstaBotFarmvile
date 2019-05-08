from selenium import webdriver
from random import randint
import time
from selenium.webdriver.common.by import By
import accountInfoGenerator as account
from webdriver_manager.chrome import ChromeDriverManager
import random
import string
import os,sys
from selenium.webdriver.common.action_chains import ActionChains
from pyvirtualdisplay import Display
from selenium.common.exceptions import NoSuchElementException



#!/usr/bin/env python

error = 'null'

##generator for random letters
def guess_letter():
    return random.choice('abcdefghijklmnopqrstuvwxyz')
##generator for random letters
def guess_number():
    return random.choice('1234567890')
#chooses PROXY AFTER EACH OTHER
def randomproxy():
    file = open("./proxy.txt")
    for line in file:
          fields = line.split(";")
    return random.choice(fields)

def random_surname():

    Names = ('Demir', 'Bala', 'yilmaz', 'Ediz',
		'yasar', 'Ozbal', 'Aydin', 'kara',
		'Bakar', 'Zengin', 'Bilgin', 'Kilic',
		'karabulut', 'Abbas', 'Hammoud', 'Alan',
		'tilki', 'Aslan', 'Boz', 'karaeski',
		'Deniz', 'Temiz', 'Alpaslan', 'Demirci',
		'Erol', 'Guneri', 'yasin', 'yelken',
		'Elmas', 'Altin', 'guller', 'Bagci',
		'yalcin', 'yucel', 'korkmaz', 'cetin',
		'Albayrak', 'Tekin', 'Yurtkulu', 'Metin',
		'Suvari', 'Kizilay', 'Inan','tasi',
		'Albagu', 'alk', 'Acu', 'Altun',
		'Avkar', 'Ayana', 'Alagan', 'Akar')

    return random.choice(Names)
################################################################################################################################################
#checks if Instagram Ban is ON
def has_error(browser):
 try:
     browser.find_element_by_xpath(("//p[contains(.,'Sorry')]"))
     return False
 except: return True

 if not has_error(browser):
     print('Error found! , aborted!')
     browser.quit()
     os.execv(sys.executable, ['python'] + sys.argv)
##################################################################################################################################################


def insta():
    print("We are now using this proxy:" + randomproxy())

    while True:
        chrome_option = webdriver.ChromeOptions()
        #chrome_option.add_argument('--proxy-server=%s' % randomproxy())
        # #hrome_option.add_argument('--headless') ,service_args=['--verbose', '--log-path=/tmp/chromedriver.log']
        display = Display(visible=0, size=(1024, 768))
        display.start()
        browser = webdriver.Chrome("./chromedriver",options=chrome_option)
        action_chains = ActionChains(browser)
        ##checks if theres internet
        ###################################################################################################
        def has_connection(browser):
            try:
                browser.find_element_by_xpath('//span[@jsselect="heading" and @jsvalues=".innerHTML:msg"]')
                return False
            except: return True

        browser.get("https://www.instagram.com/")
        #if no internet then restart progras
        if not has_connection(browser):
            print('No Internet connection, aborted!')
            browser.quit()
            os.execv(sys.executable, ['python'] + sys.argv)
        ##################################################################################################
        time.sleep(2) #time.sleep count can be changed depending on the Internet speed.
        name = account.username()

        #Fill the email value
        email_field = browser.find_element_by_name('emailOrPhone')
        action_chains.move_to_element(email_field)
        email = random_surname() + '_' + account.generatingEmail()
        email_field.send_keys(email)
        time.sleep(2)
        print("We registered with email : "+ email )

        #Fill the fullname value
        fullname_field = browser.find_element_by_name('fullName')
        action_chains.move_to_element(fullname_field)
        fullname = account.generatingName()
        fullname_field.send_keys(fullname)
        time.sleep(2)
        print("We registered with name : " + fullname )

        #Fill username value
        username_field = browser.find_element_by_name('username')
        name2 = ( name + guess_number())
        action_chains.move_to_element(username_field)
        time.sleep(2)
        username_field.send_keys(name2)
        print("We registered using this username : " + name2 )

        #Fill password value
        password_field  = browser.find_element_by_name('password')
        action_chains.move_to_element(password_field)
        password = ('aa12345bb12345cc'+ name2 )
        time.sleep(2)
        password_field.send_keys(password) #You can determine another password here.
        ################################################################################################################################################
        #checks if submit is there and is clickable
        try:
            button = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[7]/div/button')
            if button.is_displayed() and button.is_enabled():
                print("Submit is there")
                action_chains.move_to_element(button)
                button.click()
        except NoSuchElementException:
            print('Error found in Submit! , aborted!')
            browser.quit()
            os.execv(sys.executable, ['python'] + sys.argv)
        ################################################################################################################################################
        has_error(browser)
        time.sleep(1)
        #checks if ARE YOU 18 is there and clicks it if not restarts
        try:
            el18 = browser.find_element_by_xpath(("//div[@id='ageBucketSection']/fieldset/label/input"))
            if el18.is_displayed() and el18.is_enabled():
                print("18 bar is there")
                action_chains.move_to_element(el18)
                el18.click()
        except NoSuchElementException:
            print('Error found in 18bar! , aborted!')
            browser.quit()
            os.execv(sys.executable, ['python'] + sys.argv)
        ##################################################################################################################################################

        time.sleep(5)
        #checks if next is there and clicks it if not restarts and if yes saves credentials
        try:
            next = browser.find_element_by_xpath('/html/body/div[3]/div/div[3]/div/button')
            if next.is_displayed() and next.is_enabled():
                print("Next bar is there and going to save now credentials/AccountUsernames For Follow4Follow")
                next.click()
                f = open('../instabut/examples/secret.txt','a')
                f.write( name2 + ':' + ('aa12345bb12345cc'+ name2))
                f.write('\n')
                f.close()
                ##follow4follow
                f = open('../instabut/examples/usernames.txt','a')
                f.write(name2)
                f.write('\n')
                f.close()
                ###Finish
                browser.close()
        except NoSuchElementException:
            print('Error found in next! , aborted!')
            browser.quit()
            os.execv(sys.executable, ['python'] + sys.argv)
        ##################################################################################################################################################
        time.sleep(10)


flag = True
while flag:
    insta()
