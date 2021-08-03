
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


message =input("Type your desired message: ")
receiver=input("Receiver: ")
driver = webdriver.Chrome()




def login(message,receiver):
    url='https://www.instagram.com/accounts/login/'
    driver.get(url)
    sleep(1)
    driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys('python_test123456789')
    driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys('pythongod')
    driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()
    sleep(5)
    DM2(message,receiver)
    

def DM2(message,receiver):
    driver.get('https://www.instagram.com/direct/inbox/')
    driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[3]/button[2]').click()
    driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button').click()
    driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/input').send_keys(receiver)
    sleep(2)
    driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div[2]/div[1]/div/div[3]/button').click()
    sleep(2)
    driver.find_element_by_xpath('/html/body/div[5]/div/div/div[1]/div/div[2]/div/button').click()
    sleep(2)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(message)
    sleep(1)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(u'\ue007')

login(message,receiver)

