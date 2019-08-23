from selenium import  webdriver
import os
import time
import speech_recognition as sr

class Audiofile():

    def listeningaudio(self,):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
            text = r.recognize_google(audio)
            return  text

class Automate(Audiofile):
    def Runningyoutube(self):
        path = 'D:\\Selenium_Addon_Files\\chromedriver.exe'
        os.environ['webdriver.chrome.driver']  = path
        driver =  webdriver.Chrome(path)
        driver.get('https://www.youtube.com/')
        data = driver.find_element_by_id('search')
        #data_got = data.send_keys('despacito')
        data.send_keys('despacito')
        #print('playing this in yout tube--' , data_got)
        driver.find_element_by_id("search-icon-legacy").click() # need to insert the code for playing first match
        Audiofile.listeningaudio( )
        # time.sleep(180)
        # with open('lyrics.txt', 'a') as songlyrics:
        #     songlyrics.write(Audiofile.listeningaudio())


auto = Automate()
auto.Runningyoutube()








