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

username.send_keys("yourlogin")
password.send_keys("yourpass")

login_form = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@value='Sign in']")))
login_form.click()


prepend = ["bloodybaker"]

for user in prepend:
    for i in range(0, 200):
        for t in range(1, 100):
            string = "https://github.com/{}?tab=following&page={}".format(user, t)
            driver.get(string)
            time.sleep(1)

            follow_button = driver.find_elements_by_xpath("//input[@aria-label='Unfollow this person']")

            try:
                for i in follow_button:
                    i.submit()
            except:
                pass
            time.sleep(1)

driver.close()
time.sleep(3)
time.sleep(3)

driver.close()
