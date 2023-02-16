from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from random import uniform
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException


class ChatGpt:
    reply_count = 0
    reply = " "
    reply_list = []
    chat_list = {}

    def __init__(self):
        options = Options()
        options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        self.driver = webdriver.Chrome(options=options)
        # self.driver = webdriver.Chrome()
        self.init_page()

    def init_page(self):
        sleep(round(uniform(1, 2), 1))
        self.reply_list = self.get_reply_list()
        self.reply_count = len(self.reply_list)
        self.reply = " "
        self.chat_list = self.get_chat_list()

    def open(self):
        sleep(round(uniform(1, 2.5), 1))
        self.driver.get("https://chat.openai.com")
        self.wait_load()
        self.init_page()

    def wait_load(self):
        sleep(round(uniform(1, 2.5), 1))
        count = 0
        while self.driver.find_elements(By.ID, "cf-spinner-please-wait"):
            self.verify()
            count = count + 1
            if count > 20:
                print("页面刷新")
                self.open()

    def verify(self):
        sleep(round(uniform(2.5, 4), 1))
        if self.driver.find_elements(By.ID, "turnstile-wrapper"):
            self.driver.switch_to.frame(0)
            sleep(round(uniform(2, 3), 1))
            button = self.driver.find_elements(By.XPATH, "//*[@id=\"cf-stage\"]/div[6]/label/input")
            if button:
                button[0].click()
            self.driver.switch_to.default_content()
        button = self.driver.find_elements(By.XPATH, "//*[@id=\"challenge-stage\"]/div/input")
        if button:
            button[0].click()

    def send(self, message):
        message_box = self.driver.find_element(By.CSS_SELECTOR, ".m-0")
        if message_box:
            message_box.click()
            sleep(round(uniform(0.2, 0.8), 1))
            message_lines = message.split("\n")
            for line in message_lines:
                message_box.send_keys(line)
                sleep(round(uniform(0.2, 0.8), 1))
                message_box.send_keys(Keys.SHIFT, Keys.ENTER)
                sleep(round(uniform(0.2, 0.8), 1))
            message_box.send_keys(Keys.ENTER)
            return True
        else:
            return False

    def wait_reply(self):
        while self.driver.find_elements(By.CSS_SELECTOR, ".result-streaming"):
            sleep(1)
        self.reply_list = self.get_reply_list()
        if len(self.reply_list) <= self.reply_count:
            return "[Unexpected error, no valid reply received]", False
        else:
            self.reply_count = len(self.reply_list)
            return "[Request succeeded, valid reply received]", True

    def repling(self):
        sleep(2)
        reply = self.reply
        stream = self.driver.find_elements(By.CSS_SELECTOR, ".result-streaming")
        if stream:
            if reply != " ":
                reply = stream[0].text.split(reply)[1]
                self.reply = reply[1]
            else:
                reply = stream[0].text
                self.reply = reply
        else:
            if reply != " ":
                self.reply_list = self.get_reply_list()
                reply = self.get_last_reply().split(reply)[1]
                self.reply = " "
            else:
                self.reply_list = self.get_reply_list()
                reply = "The answer is over"
        return reply

    def get_reply_list(self):
        return self.driver.find_elements(By.CSS_SELECTOR, ".markdown")

    def get_all_replies(self):
        replies = {}
        if self.reply_list:
            reply_list = self.reply_list
            if reply_list:
                for index, value in enumerate(reply_list):
                    replies[index] = value.text
                return replies
        else:
            return "No reply"

    def get_last_reply(self):
        if self.reply_list:
            reply = self.reply_list[len(self.reply_list) - 1]
            return reply.text
        else:
            return "No reply"

    def regenerate(self):
        self.driver.find_element(By.CSS_SELECTOR, ".btn").click()

    def get_chat_list(self):
        chat_list = {}
        while self.driver.find_elements(By.CSS_SELECTOR, ".btn-dark"):
            self.driver.find_elements(By.CSS_SELECTOR, ".btn-dark")[0].click()
            sleep(round(uniform(1, 2.5), 1))
        sleep(1.5)
        chats = self.driver.find_elements(By.XPATH, "//*[@id=\"__next\"]/div[1]/div[2]/div/div/nav/div/div/a/div[1]")
        for index, value in enumerate(chats):
            chat_list[index] = [value, value.text]
        return chat_list

    def get_all_chat(self):
        chat_list = self.chat_list
        all_chat = {}
        for k, v in chat_list.items():
            all_chat[v[1]] = k
        return all_chat

    def choose_chat(self, ref):
        sleep(1)
        button = self.chat_list[ref][0]
        if button != "":
            button.click()
            self.init_page()
            return True
        else:
            return False

    def delete_chat(self):
        sleep(round(uniform(1, 1.5), 1))
        button = self.driver.find_elements(By.XPATH, "//*[@id=\"__next\"]/div[1]/div[2]/div/div/nav/div/div/a/div[2]/button[2]")
        if button:
            button[0].click()
            sleep(round(uniform(2, 3), 1))
            button = self.driver.find_elements(By.XPATH, "//*[@id=\"__next\"]/div[1]/div[2]/div/div/nav/div/div/a/div[2]/button[1]")
            if button:
                button[0].click()
                sleep(1)
                self.chat_list = self.get_chat_list()
                return True
            else:
                return False
        else:
            return False

    def rename_chat(self, name):
        button = self.driver.find_elements(By.XPATH, "//*[@id=\"__next\"]/div[1]/div[2]/div/div/nav/div/div/a/div[2]/button[1]")
        if button:
            button[0].click()
            sleep(round(uniform(1, 1.5), 1))
            text_input = self.driver.find_element(By.XPATH, "//*[@id=\"__next\"]/div[1]/div[2]/div/div/nav/div/div/div/input")
            text_input.send_keys(Keys.CONTROL, "A")
            sleep(round(uniform(0.5, 0.8), 1))
            text_input.send_keys(name)
            sleep(round(uniform(0.3, 0.7), 1))
            text_input.send_keys(Keys.ENTER)
            sleep(1)
            self.chat_list = self.get_chat_list()
            return True
        else:
            return False

    def new_chat(self):
        sleep(1)
        button = self.driver.find_elements(By.XPATH, "//*[@id=\"__next\"]/div[1]/div[2]/div/div/nav/a[1]")
        if button:
            button[0].click()
            return True
        else:
            return False
