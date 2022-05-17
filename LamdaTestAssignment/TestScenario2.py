from selenium import webdriver
from selenium.webdriver import ActionChains
import time

class TestScenario2():
    def test_scenario_2(self):
        driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver.exe")
        driver.maximize_window()
        driver.get("https://www.lambdatest.com/selenium-playground")

        driver.find_element_by_link_text("Drag & Drop Sliders").click()

        element = driver.find_element_by_xpath("//input[@value='15']")
        ActionChains(driver).drag_and_drop_by_offset(element, 120, 0).perform()

        text = driver.find_element_by_xpath("//*[@id='rangeSuccess']").text
        print(text)

        if text == "95":
            driver.close()
            assert True
        else:
            driver.close()
            assert False

ts2 = TestScenario2()
ts2.test_scenario_2()