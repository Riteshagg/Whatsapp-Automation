from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
browser = webdriver.Chrome(executable_path="chromedriver.exe")
browser.get("https://web.whatsapp.com/")
wait = WebDriverWait(browser,600)


target = '"Shubham"'
file_path = input("Enter the File Path: ")
message = input("Enter the message: ")

# ----------------Click for message to friend name-------------------------------------

xx_paths = '//span[contains(@title,' + target +')]'
taarget = wait.until(ec.presence_of_element_located((By.XPATH, xx_paths)))
taarget.click()

# ----------------For sending image-------------------------------------

attache = browser.find_element_by_xpath("//div[@title = 'Attach']")
attache.click()
photo = browser.find_element_by_xpath("//input[@accept = 'image/*,video/mp4,video/3gpp,video/quicktime']")
photo.send_keys(file_path)
sleep(3)
send_image = browser.find_element_by_xpath("//span[@data-icon='send-light']")
send_image.click()

# -----------------For sending text---------------------------------------
input_msg = browser.find_element_by_xpath(".//*[@class='_1Plpp']")
for i in range(5):
    input_msg.send_keys(message + Keys.ENTER)


