from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver, AbstractEventListener
from time import sleep
from selenium.webdriver.common.keys import Keys


class InstaBot:
    def __init__(self, username, pw):
        self.driver = webdriver.Chrome('/Program Files/chromedriver')
        self.username = username
        self.driver.get("https://instagram.com")
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(pw)
        sleep(2)
        # Due to Instagram's html obfuscation, it is difficult to use nice x_path like above
        self.driver.find_element_by_xpath("//button[@type='submit']").click()
        sleep(3)
        # Press not now for saving user info
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        sleep(2)
        # Press not now for notifications
        self.driver.find_element_by_xpath("//button[@class = 'aOOlW   HoLwm ']").click()

    def navigate(self, handle):
        self.driver.get("https://instagram.com/{}/".format(handle))
        sleep(1)
        self.driver.find_element_by_xpath("//a[@href = \"/{}/followers/\"]".format(handle)).click()

    def follow(self):
        counter = 0
        sleep(2)
        # make sure to choose the div with the scroll bar included, the element will be the pop up we scroll on
        element = self.driver.find_element_by_xpath("//div[@class=\"isgrP\"]")

        # Obtain list of all following accounts
        list = self.driver.find_elements_by_xpath("//button[contains(text(), 'Follow')]")
        sleep(2)
        self.driver.execute_script("arguments[0].scrollBy(0,3000)", element)
        sleep(2)
        self.driver.execute_script("arguments[0].scrollBy(0,1000)", element)
        counter = 12
        print(len(list))
        for i in list:
            try:
                list = self.driver.find_elements_by_xpath("//button[contains(text(), 'Follow')]")
                sleep(2)
                i.click()
                counter = counter + 1
                # Scroll down to bottom
                self.driver.execute_script("arguments[0].scrollBy(0,100)", element)
            except StaleElementReferenceException:
                print("stale bread")


my_bot = InstaBot('username', 'password')  # pass in username and password
my_bot.navigate('search_handle')  # Pass in the ig handle
my_bot.follow()
