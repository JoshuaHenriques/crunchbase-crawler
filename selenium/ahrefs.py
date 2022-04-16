import os
from selenium import webdriver
from fp.fp import FreeProxy
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import Chrome
import numpy as np
# from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.edge.options import Options
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from time import sleep
import scipy.interpolate as si
from dotenv import load_dotenv

load_dotenv()


ua = UserAgent()
# proxy = FreeProxy(country_id='US', rand = True, anonym= True).get()
# proxy = FreeProxy().get()
# ip = proxy.split("://")[1]
options = Options()
options.add_argument('no-sandbox')
options.add_argument('start-maximized')
# options.add_argument('--start-fullscreen')
options.add_argument('single-process')
options.add_argument('disable-dev-shm-usage')
options.add_argument("incognito")
options.add_argument("enable-javascript")
options.add_argument('disable-blink-features=AutomationControlled')
options.add_argument('disable-blink-features=AutomationControlled')
options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_argument("disable-infobars")
options.add_argument('user-agent={}'.format(ua.random))
# options.add_argument('--proxy-server={}'.format(ip))


driver = webdriver.Chrome(options=options)

action = ActionChains(driver)


driver.get("https://ahrefs.com/backlink-checker")

sleep(5)

# driver.find_element_by_css_selector(".css-14twyaz-input").send_keys("https://www.reuters.com/world/europe/ukraine-braces-new-russian-offensive-moscow-dismisses-rape-allegations-2022-04-12/")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".css-14twyaz-input"))).send_keys("https://www.reuters.com/world/europe/ukraine-braces-new-russian-offensive-moscow-dismisses-rape-allegations-2022-04-12/")
sleep(5)

# driver.find_element_by_css_selector(".css-x7qcwq-button").click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".css-x7qcwq-button"))).click()

# driver.find_element_by_css_selector(".#recaptcha-anchor").click()
# driver.find_element_by_css_selector(".recaptcha-checkbox-border").click()
# driver.find_element_by_css_selector(".recaptcha-checkbox-borderAnimation").click()
# driver.find_element_by_css_selector(".recaptcha-checkbox-spinner").click()
# driver.find_element_by_css_selector(".recaptcha-checkbox-spinner-overlay").click()
# driver.find_element_by_css_selector(".recaptcha-checkbox-checkmark").click()

# WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[name^='a-'][src^='https://www.google.com/recaptcha/api2/anchor?']")))

# driver.find_element_by_xpath("//*[@id='recaptcha-anchor']").click()
# driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[1]/div/div/span/div").click()
# driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[1]/div/div/span/div[2]").click()
# driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[1]/div/div/span/div[3]").click()
# driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[1]/div/div/span/div[3]/div").click()
# driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[1]/div/div/span/div[4]").click()

sleep(1)

# WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"#recaptcha-anchor")))
# WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.ID,"recaptcha-anchor")))
# WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='recaptcha-anchor']"))).click()
# WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "recaptcha-anchor"))).click()
sleep(1)

# check_box = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='recaptcha-checkbox goog-inline-block recaptcha-checkbox-unchecked rc-anchor-checkbox']/div[@class='recaptcha-checkbox-checkmark']")))
# human_like_mouse_move(action, check_box)
# check_box.click()
# action = ActionChains(driver)
# human_like_mouse_move(action, check_box)

WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[name^='a-'][src^='https://www.google.com/recaptcha/api2/anchor?']")))
driver.execute_script("arguments[0].click();", WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='recaptcha-checkbox goog-inline-block recaptcha-checkbox-unchecked rc-anchor-checkbox']/div[@class='recaptcha-checkbox-checkmark']"))))

sleep(4)
# driver.quit()