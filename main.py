from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3969838231&f_LF=f_AL&geoId=92000000&keywords=python"
           "%20developer&location=Worldwide&origin=JOB_SEARCH_PAGE_LOCATION_AUTOCOMPLETE&refresh=true")

time.sleep(8)
sign_in = driver.find_element(By.CLASS_NAME, value="cta-modal__primary-btn")
sign_in.click()

time.sleep(4)
username = driver.find_element(By.ID, value="username")
password = driver.find_element(By.ID, value="password")
sign_in_2 = driver.find_element(By.CLASS_NAME, value="btn__primary--large")
username.send_keys("username")
password.send_keys("pass")
sign_in_2.click()
