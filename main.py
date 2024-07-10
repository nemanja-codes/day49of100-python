from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3950305564&f_AL=true&f_E=1&f_WT=2&geoId=92000000&"
           "keywords=python%20developer&location=Worldwide&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true"
           "&spellCorrectionEnabled=true")

time.sleep(8)
sign_in = driver.find_element(By.CLASS_NAME, value="cta-modal__primary-btn")
sign_in.click()

time.sleep(4)
username = driver.find_element(By.ID, value="username")
password = driver.find_element(By.ID, value="password")
sign_in_2 = driver.find_element(By.CLASS_NAME, value="btn__primary--large")
username.send_keys("username")
password.send_keys("password")
sign_in_2.click()

time.sleep(10)
easy_apply = driver.find_element(By.CSS_SELECTOR, value=".jobs-s-apply button")
easy_apply.click()

time.sleep(2)
phone_number = driver.find_element(By.CSS_SELECTOR, value="input[id*=phoneNumber]")
if phone_number.text == "":
    phone_number.send_keys("640250175")
next_btn = driver.find_element(By.CLASS_NAME, value="artdeco-button--primary")
next_btn.click()
next_btn.click()

q1 = driver.find_element(By.CSS_SELECTOR, value=".artdeco-text-input input")
q1.send_keys("0")
q2 = driver.find_element(By.XPATH, value='//*[@id="single-line-text-form-component-formElement-urn-li-jobs-'
                                         'applyformcommon-easyApplyFormElement-3950305564-1064925891-numeric"]')
q2.send_keys("0")
q3 = driver.find_element(By.XPATH, value='//*[@id="single-line-text-form-component-formElement-urn-li-jobs-'
                                         'applyformcommon-easyApplyFormElement-3950305564-1064925899-numeric"]')
q3.send_keys("1")
review_btn = driver.find_element(By.CSS_SELECTOR, value=".artdeco-button--primary")
review_btn.click()

time.sleep(1)
submit_button = driver.find_element(by=By.CSS_SELECTOR, value=".artdeco-button--primary")
submit_button.click()
