from userinfo import username, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

class GitHub:
    def __init__(self, username, password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password

    def signIn(self):
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(1)
        self.browser.find_element("xpath","//*[@id='_R_c9d9lplkldcpbn6b5ipamH1_']").send_keys(self.username)
        self.browser.find_element("xpath", "//*[@id='_R_cdd9lplkldcpbn6b5ipamH1_']").send_keys(self.password)
        time.sleep(1)
        self.browser.find_element("xpath", "//*[@id='login_form']/div/div[1]/div/div[3]/div/div/div/div[1]/div/span/span").click()
        time.sleep(3)

    def getFollowers(self):
        self.browser.get(f"https://www.instagram.com/{self.username}")
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "main")))
        time.sleep(3)

        # Takipçi sayısını oku
        follower_span = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//span[contains(text(), 'takipçi')]")
        ))
        follower_count = int(follower_span.text.replace("takipçi", "").strip())
        print(f"Takipçi sayısı: {follower_count}")

        # Followers linkine tıkla
        followers_link = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@href, '/followers')]")
        ))
        self.browser.execute_script("arguments[0].click();", followers_link)

        wait.until(EC.presence_of_element_located((By.XPATH, "//div[@role='dialog']")))
        time.sleep(3)

        dialog = self.browser.find_element(By.XPATH, "//div[@role='dialog']")
        all_followers = []

        while len(all_followers) < follower_count:
            links = dialog.find_elements(By.TAG_NAME, "a")

            for link in links:
                href = link.get_attribute("href")
                if (href and
                    href not in all_followers and
                    "instagram.com" in href and
                    "/explore" not in href and
                    "/p/" not in href and
                    "/reel/" not in href and
                    href != f"https://www.instagram.com/{self.username}/"):
                    all_followers.append(href)
                    print(href)

                if len(all_followers) >= follower_count:
                    break

            self.browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", dialog)
            time.sleep(2)

        print(f"\nToplam {len(all_followers)} takipçi bulundu.")

        with open("followers.txt", "w") as f:
            for follower in all_followers:
                f.write(follower + "\n")

    def followuser(self,username):
        self.browser.get(f"https://www.instagram.com/{username}")
        time.sleep(3)
        followbutton=self.browser.find_element(By.TAG_NAME,"button")
        time.sleep(3)
        if followbutton.text == "Following":
            followbutton.click()

    def unfollowuser(self,username):
        self.browser.get(f"https://www.instagram.com/{username}")
        time.sleep(2)
        unfollowbutton=self.browser.find_element(By.TAG_NAME,"button")
        if unfollowbutton.text != "Following":
            unfollowbutton.click()
            time.sleep(2)   
            self.browser.find_element(By.XPATH,"//html/body/div[4]/div[2]/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/div[8]/div[1]/div/div/div[2]/div/div/span/span").click()
        # time.sleep(2)
        # self.browser.find_element(By.XPATH,"//button[contains(text(), 'Takibi bırak')]").click()
        time.sleep(3)
     
github = GitHub(username, password)
github.signIn()
time.sleep(5)
github.getFollowers()
# github.unfollowuser("zeyiremx")
# github.unfollowuser("tlg.cnar")
# github.followuser("tlg.cnar")
# time.sleep(3)
# github.unfollowuser("tlg.cnar")           

time.sleep(10)