from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import fnmatch
import argparse
import random

class InstagramBot():
    def __init__(self, password,username):
        self.browser = webdriver.Chrome()
        self.password = password
        self.ur = username

    def getIMG(self, folder):
        listOfFiles = os.listdir(folder)
        L = []
        pattern = "*.jpg"
        pattern1 = "*.jpeg"
        pattern2 = "*.png"
        for entry in listOfFiles:
            if fnmatch.fnmatch(entry, pattern) or fnmatch.fnmatch(entry, pattern1) or fnmatch.fnmatch(entry, pattern2):
             L.append(os.getcwd() + "/"+ entry)
        PATH = random.choice(L)
        return PATH

    def signIn(self):
        self.browser.get('https://www.instagram.com/accounts/login/')

        emailInput = self.browser.find_elements_by_css_selector('form input')[0]
        passwordInput = self.browser.find_elements_by_css_selector('form input')[1]

        emailInput.send_keys(self.ur)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(2)

    def Change_Pic(self,PATH):
        self.browser.get('https://www.instagram.com/' + self.ur)
        inputs = self.browser.find_elements_by_xpath("//input[@accept = 'image/jpeg,image/png']")
        for inputt in inputs:
            inputt.send_keys(PATH)




    def TerminateSession(self):
        time.sleep(2)
        self.browser.quit()



ap = argparse.ArgumentParser()
ap.add_argument("-u", "--user", required=True, help="your user name")
ap.add_argument("-p", "--pasw", required=True, help="your password")

args = vars(ap.parse_args())

bot = InstagramBot(args["pasw"],args["user"])
bot.signIn()
path = bot.getIMG(os.getcwd())
bot.Change_Pic(path)
bot.TerminateSession()
