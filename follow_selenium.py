import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://github.com/login")
wait = WebDriverWait(driver, 10)

username = wait.until(EC.presence_of_element_located((By.ID, "login_field")))
password = wait.until(EC.presence_of_element_located((By.ID, "password")))

username.send_keys("login")
password.send_keys("password")

login_form = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@value='Sign in']")))
login_form.click()

prepend = ["andrewsyc"]

for user in prepend:
    for t in range(1, 50):
        string = "https://github.com/{}?page={}&tab=followers".format(user, t)
        driver.get(string)
        time.sleep(1)

        follow_button = driver.find_elements_by_xpath("//input[@aria-label='Follow this person']")

        try:
            for i in follow_button:
                i.submit()
        except:
            pass
        time.sleep(1)

driver.close()
