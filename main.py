from selenium import webdriver
from selenium.webdriver.common.by import By


# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3969838231&f_LF=f_AL&geoId=92000000&keywords=python"
           "%20developer&location=Worldwide&origin=JOB_SEARCH_PAGE_LOCATION_AUTOCOMPLETE&refresh=true")
