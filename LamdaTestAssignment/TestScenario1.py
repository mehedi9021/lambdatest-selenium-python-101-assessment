from selenium import webdriver

class TestScenario1():
    def test_scenario_1(self):
        driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver.exe")
        driver.maximize_window()
        driver.get("https://www.lambdatest.com/selenium-playground")

        driver.find_element_by_link_text("Simple Form Demo").click()

        if "simple-form-demo" in driver.current_url:
            assert True
        else:
            assert False

        message = "Welcome to LambdaTest"
        driver.find_element_by_id("user-message").send_keys(message)
        driver.find_element_by_id("showInput").click()

        text = driver.find_element_by_id("message").text
        print(text)

        if message == text:
            driver.close()
            assert True
        else:
            driver.close()
            assert False

ts1 = TestScenario1()
ts1.test_scenario_1()