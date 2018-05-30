from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from time import sleep

class SMS:
    def __init__(self,url):
        self.url=url

    def get_access(self):
        # start up a chrome with fixed Download directory
        options = Options()
        options.add_argument("--disable-notifications");
        # options.set_headless(headless=True)
        downloadDir="C:/Users/Rajnish/Downloads/Project/Master"
        prefs = {"download.default_directory": downloadDir,
     "download.prompt_for_download": False,
     "download.directory_upgrade": True,
     "safebrowsing.enabled": True,
     'safebrowsing.disable_download_protection': True
         }
        options.add_experimental_option("prefs", prefs)
        self.driver = webdriver.Chrome(chrome_options=options)
                    # driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
                    # params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': downloadDir}}
                    # command_result = driver.execute("send_command", params)

        self.driver.get(self.url)

    def login(self,username, password):
            #get snaps and recording details
        user_name= WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID,"username")))
        pass_word= WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID,"password")))

        user_name.clear()
        pass_word.clear()

        user_name.send_keys(username)
        pass_word.send_keys(password)

        # login = WebDriverWait(self.driver,20).until(EC.presence_of_element_located((By.ID,"loginBTN")))
        login = WebDriverWait(self.driver,20).until(EC.presence_of_element_located((By.XPATH,"//BUTTON[@type='submit'][text()='Login']")))
        login.click()

        # sms_button = WebDriverWait(self.driver,20).until(EC.presence_of_element_located((By.ID,"sendSMS")))
        # sms_button.click()

    def send(self,phone,msg):
        self.driver.switch_to_frame(self.driver.find_element_by_id("by2Frame"))

        mobile= WebDriverWait(self.driver,20).until(EC.presence_of_element_located((By.XPATH,'//INPUT[@type="text"][@placeholder="Enter Mobile Number or Name"]')))
        message= WebDriverWait(self.driver,20).until(EC.presence_of_element_located((By.ID,"sendSMSMsg")))
        send = WebDriverWait(self.driver,20).until(EC.presence_of_element_located((By.XPATH,"//INPUT[@id='btnsendsms']")))

        #
        # mobile= WebDriverWait(self.driver,20).until(EC.presence_of_element_located((By.ID,'mobile')))
        # message= WebDriverWait(self.driver,20).until(EC.presence_of_element_located((By.ID,"message")))
        # send = WebDriverWait(self.driver,20).until(EC.presence_of_element_located((By.ID,'Send')))

        mobile.clear()
        message.clear()

        mobile.send_keys(phone)
        message.send_keys(msg)

        mainHanlde = self.driver.window_handles
        send.click()

        allHandle = self.driver.window_handles

        for c in allHandle:
            if c !=mainHanlde[0]:
                self.driver.switch_to_window(c)
                break

        send1 = WebDriverWait(self.driver,20).until(EC.presence_of_element_located((By.XPATH,"//INPUT[@id='btnsendsms']")))
        send1.click()

    def browser_quit(self):
        sleep(5)
        self.driver.quit()


M= Master("http://www.160by2.com")
M.get_access()
M.login("9939427850", "12345678")
M.send("8722978929", "hello")

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from time import sleep

class Master:
    def __init__(self,url):
        self.url=url

    def get_access(self):
        # start up a chrome with fixed Download directory
        options = Options()
        options.add_argument("--disable-notifications");
        # options.set_headless(headless=True)
        downloadDir="C:/Users/Rajnish/Downloads/Project/Master"
        prefs = {"download.default_directory": downloadDir,
     "download.prompt_for_download": False,
     "download.directory_upgrade": True,
     "safebrowsing.enabled": True,
     'safebrowsing.disable_download_protection': True
         }
        options.add_experimental_option("prefs", prefs)
        self.driver = webdriver.Chrome(chrome_options=options)
        self.driver.get(self.url)

    def login(self,username, password):
            #get snaps and recording details
        user_name= WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID,"username")))
        pass_word= WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID,"password")))

        user_name.clear()
        pass_word.clear()

        user_name.send_keys(username)
        pass_word.send_keys(password)

        # login = WebDriverWait(self.driver,20).until(EC.presence_of_element_located((By.ID,"loginBTN")))
        login = WebDriverWait(self.driver,20).until(EC.presence_of_element_located((By.XPATH,"//BUTTON[@type='submit'][text()='Login']")))
        login.click()

        # sms_button = WebDriverWait(self.driver,20).until(EC.presence_of_element_located((By.ID,"sendSMS")))
        # sms_button.click()

    def send(self,phone,msg):
        self.driver.switch_to_frame(self.driver.find_element_by_id("by2Frame"))

        mobile= WebDriverWait(self.driver,20).until(EC.presence_of_element_located((By.XPATH,'//INPUT[@type="text"][@placeholder="Enter Mobile Number or Name"]')))
        message= WebDriverWait(self.driver,20).until(EC.presence_of_element_located((By.ID,"sendSMSMsg")))
        send = WebDriverWait(self.driver,20).until(EC.presence_of_element_located((By.XPATH,"//INPUT[@id='btnsendsms']")))

        #
        # mobile= WebDriverWait(self.driver,20).until(EC.presence_of_element_located((By.ID,'mobile')))
        # message= WebDriverWait(self.driver,20).until(EC.presence_of_element_located((By.ID,"message")))
        # send = WebDriverWait(self.driver,20).until(EC.presence_of_element_located((By.ID,'Send')))

        mobile.clear()
        message.clear()

        mobile.send_keys(phone)
        message.send_keys(msg)

        mainHanlde = self.driver.window_handles
        send.click()

        allHandle = self.driver.window_handles

        for c in allHandle:
            if c !=mainHanlde[0]:
                self.driver.switch_to_window(c)
                break

        send1 = WebDriverWait(self.driver,20).until(EC.presence_of_element_located((By.XPATH,"//INPUT[@id='btnsendsms']")))
        send1.click()

    def browser_quit(self):
        sleep(5)
        self.driver.quit()


M= SMS("http://www.160by2.com")
M.get_access()
M.login("9939427850", "12345678")
M.send("8722978929", "hello")
