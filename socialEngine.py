import pickle
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import os.path

global driver
driver = 0

# ------------- Controlling Functions  ------------- #
def cookieLoad(site):
    cookies = pickle.load(open("Tls/" + site + ".pkl", "rb"))
    for cookie in cookies:
        print(cookie)
        driver.add_cookie(cookie)

def loadSite(site):
    driver.get("https://www." + site + ".com")
    cookieLoad(site)
    driver.get("https://www." + site + ".com")

# ------------- Linked IN  ------------- #
def firstTimeLI(username, password):
    time.sleep(6)
    cookieBtn = driver.find_element(By.XPATH, "//button[contains(text(),'Accept')]")
    cookieBtn.click()
    time.sleep(2)
    usernameInput = driver.find_element(By.NAME, "session_key")
    usernameInput.send_keys(username)
    passwordInput = driver.find_element(By.NAME, "session_password")
    passwordInput.send_keys(password)
    time.sleep(5)
    loginBtn = driver.find_element(By.XPATH, "//*[@id='main-content']/section[1]/div/div/form/button")
    loginBtn.click()
    pickle.dump(driver.get_cookies(), open("Tls/cookies.pkl", "wb"))

def postArticleLI(title, article):
    driver.get("https://www.linkedin.com/company/91642186/admin/")
    time.sleep(5)
    firstPostBtn = driver.find_element(By.XPATH, "//span[text()='Start a post']")
    firstPostBtn.click()
    time.sleep(4)
    textArea = driver.find_element(By.XPATH, "//div[@role='textbox']")
    textArea.click()
    textArea.send_keys(title)
    textArea.send_keys(Keys.ENTER)
    textArea.send_keys(article)
    time.sleep(4)
    submitBtn = driver.find_element(By.XPATH, "//span[text()='Post']")
    submitBtn.click()

def fullScriptLI(username, password, title, article):
    global driver
    driver = webdriver.Chrome('Tls/chromedriver.exe')
    driver.get("https://www.linkedin.com")
    time.sleep(5)
    if os.path.exists('Tls/linkedIN.pkl'):
        cookieLoad("linkedIN")
    else:
        firstTimeLI(username, password)
    time.sleep(5)
    postArticleLI(title, article)

# ------------- Twitter ------------- #
def postArticleTW(title, article):
    time.sleep(5)
    textArea = driver.find_element(By.XPATH, "//div[@role='textbox']")
    textArea.click()
    time.sleep(1)
    textArea.send_keys(title)
    textArea.send_keys(Keys.ENTER)
    textArea.send_keys(article)
    submitBtn = driver.find_element(By.XPATH, "//span[text()='Tweet']")
    submitBtn.click()

def fullScriptTW(title, article):
    global driver
    driver = webdriver.Chrome('Tls/chromedriver.exe')
    loadSite("twitter")
    time.sleep(5)
    postArticleTW(title, article)

# ------------- Others ------------- #
def openArticleBrowser(url2Open):
    global driver
    driver = webdriver.Chrome('Tls/chromedriver.exe')
    driver.get(url2Open)

