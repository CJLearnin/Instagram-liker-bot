import selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


import time
from selenium.webdriver.chrome.options import Options


class instagram:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)

    def login(self):

        browser = self.browser
        browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)

        username = browser.find_element_by_name("username")
        # username = browser.find_element_by_xpath("//input[@name='username']")
        username.clear()
        username.send_keys(self.username)
        # password = browser.find_element_by_xpath("//input[@name='password']")

        password = browser.find_element_by_name("password")
        password.clear()
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        # Below waits for pop up notification to appear then closes it.
        ui.WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".aOOlW.HoLwm"))
        ).click()

        list_of_pics = []

        for i in range(1, 2):
            browser.execute_script(
                "window.scrollTo(0,document.body.scrollHeight)"
            )  # scrolls down to the bottom of the page twice
            time.sleep(20)

            # list_of_pics.append(pictures)
        pictures = browser.find_elements_by_class_name("fr66n")
        for pics in pictures:
            try:
                pics.click()
                print("liked picture")
                time.sleep(7)
            except:
                print("didn't like picture")
                continue


account = instagram("Enter your Username", "Enter your password")
account.login()
