from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

class TestScenario3():
    def test_scenario_3(self):
        driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver.exe")
        driver.maximize_window()
        driver.get("https://www.lambdatest.com/selenium-playground")

        driver.find_element_by_link_text("Input Form Submit").click()
        driver.find_element_by_xpath("//*[@id='seleniumform']/div[6]/button").click()

        driver.find_element_by_id("name").send_keys("Md. Xyz")
        driver.find_element_by_id("inputEmail4").send_keys("xyz@gmail.com")
        driver.find_element_by_id("inputPassword4").send_keys("12345")
        driver.find_element_by_id("company").send_keys("Zyx")
        driver.find_element_by_id("websitename").send_keys("xyz.com")
        driver.find_element_by_id("inputCity").send_keys("Yxz")
        driver.find_element_by_id("inputAddress1").send_keys("Abc")
        driver.find_element_by_id("inputAddress2").send_keys("Cba")
        driver.find_element_by_id("inputState").send_keys("Pqs")
        driver.find_element_by_id("inputZip").send_keys("1000")

        element = driver.find_element_by_name("country")
        dropdown = Select(element)
        dropdown.select_by_visible_text("United States")

        driver.find_element_by_xpath("//*[@id='seleniumform']/div[6]/button").click()

        message = driver.find_element_by_xpath("//*[@id='__next']/div[1]/section[3]/div/div/div[2]/div/p").text
        print(message)

        if message == "Thanks for contacting us, we will get back to you shortly.":
            driver.close()
            assert True
        else:
            driver.close()
            assert False

ts3 = TestScenario3()
ts3.test_scenario_3()