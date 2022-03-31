from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.FireFox()
driver.get("https//crunchbase.com")

driver.find_element_by_xpath("/html/body/chrome/div/app-header/div[1]/div[2]/div/anon-nav-row/nav-action-item[2]/nav-header-action-item/a/span[1]/nav-action-item-header-layout/div/span").click()

driver.quit()