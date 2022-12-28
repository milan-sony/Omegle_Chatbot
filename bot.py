# Selenium documentation
# https://selenium-python.readthedocs.io/
# https://www.geeksforgeeks.org/selenium-python-tutorial/

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from topics import topics_list
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# To stop chrome from automatically closing
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/#2-driver-management-software

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

link = 'https://www.omegle.com/'

# Maximize browser window
driver.maximize_window()
driver.get(link)
sleep(2)

# Adding topics to talk about from topics.py
def topics():
  newtopicinput = driver.find_element(By.CLASS_NAME, "newtopicinput")
  for topics in topics_list:
    newtopicinput.send_keys(topics)
    newtopicinput.send_keys(Keys.ENTER) 
    sleep(1)

# Click on text button after entering topics
def textbtn():
  textbtn = driver.find_element(By.ID, "textbtn")
  textbtn.click()
  sleep(1)

# Click on pop up checkboxes and confirm button after clicking the textbtn
def checkbox():
  # Tick on checkbox 1
  checkbox = driver.find_element(By.XPATH, "/html/body/div[7]/div/p[1]/label/input")
  checkbox.click()
  sleep(1)
  # Tick on checkbox 2
  checkbox = driver.find_element(By.XPATH, "/html/body/div[7]/div/p[2]/label/input")
  checkbox.click()
  sleep(1)
  # Click on Confirm and Continue button
  confirmbtn = driver.find_element(By.XPATH, "/html/body/div[7]/div/p[3]/input")
  confirmbtn.click()


# Function Call
topics()
textbtn()
checkbox()
