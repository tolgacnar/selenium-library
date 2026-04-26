from twitterUserInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


url = "http://x.com/i/flow/login"


class twitter:
    def __init__(self, username, password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password

    def login(self):
        self.browser.get(url)
        time.sleep(4)

        # Login sayfası yüklenmediyse (yeniden dene ekranı) sayfayı yenile
        while True:
            try:
                self.browser.find_element(By.XPATH, "//input[@autocomplete='username' or @name='text']")
                print("[✓] Login sayfası yüklendi.")
                break
            except:
                print("[✗] Yeniden dene ekranı geldi, sayfa yenileniyor...")
                self.browser.refresh()
                time.sleep(5)

        self.browser.find_element(By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input").send_keys(self.username)
        time.sleep(4)
        self.browser.find_element(By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]").click()
        
        while True:
            time.sleep(2)
            try:
                self.browser.find_element(By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div/input")
                print("[✓] Şifre alanı bulundu.")
                break
            except:
                print("[✗] Şifre alanı gelmedi, tekrar deneniyor...")
                username_input = self.browser.find_element(By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input")
                username_input.clear()
                username_input.send_keys(self.username)
                self.browser.find_element(By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]").click()
                time.sleep(4)

        time.sleep(4)
        self.browser.find_element(By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div/input").send_keys(self.password)
        time.sleep(4)
        self.browser.find_element(By.TAG_NAME, "button").click()


twitterbot = twitter(username, password)
twitterbot.login()