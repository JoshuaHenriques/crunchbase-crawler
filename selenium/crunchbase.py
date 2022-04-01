import os
from selenium import webdriver
from fp.fp import FreeProxy
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.edge.options import Options
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from time import sleep
from dotenv import load_dotenv

load_dotenv()


ua = UserAgent()
# proxy = FreeProxy(country_id='US', rand = True, anonym= True).get()
# proxy = FreeProxy().get()
# ip = proxy.split("://")[1]

options = Options()
# options.add_argument('--no-sandbox')
# options.add_argument('--start-maximized')
# options.add_argument('--start-fullscreen')
# options.add_argument('--single-process')
# options.add_argument('--disable-dev-shm-usage')
# options.add_argument("--incognito")
# options.add_argument("--enable-javascript")
# options.add_argument('--disable-blink-features=AutomationControlled')
# options.add_argument('--disable-blink-features=AutomationControlled')
# options.add_experimental_option('useAutomationExtension', False)
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_argument("--disable-infobars")
# options.add_argument('--user-agent={}'.format(ua.random))
# options.add_argument('--proxy-server={}'.format(ip))

# PROXY = ip
# webdriver.DesiredCapabilities.CHROME['proxy'] = {
#     "httpProxy":PROXY,
#     "ftpProxy":PROXY,
#     "sslProxy":PROXY,
#     "noProxy":None,
#     "proxyType":"MANUAL",
#     "autodetect":False
# }
# webdriver.DesiredCapabilities.EDGE['acceptSslCerts'] = True

# path = os.path.join(os.getcwd(), 'chromedriver')

driver = webdriver.Firefox(options=options)
# driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
#     "source":
#         "const newProto = navigator.__proto__;"
#         "delete newProto.webdriver;"
#         "navigator.__proto__ = newProto;"
# })

# options = webdriver.ChromeOptions()
# options.add_argument("--enable-javascript")
#User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:98.0) Gecko/20100101 Firefox/98.0
#options.add_argument("user-agent=User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:98.0) Gecko/20100101 Firefox/98.0")
# driver = webdriver.Chrome(options=options)
driver.get("https://crunchbase.com/login")

# action = ActionChains(driver)

sleep(5)

# //*[@id="mat-input-1"]
# html body chrome div mat-sidenav-container.mat-drawer-container.mat-sidenav-container mat-sidenav-content.mat-drawer-content.mat-sidenav-content.ng-star-inserted div authentication-page.ng-star-inserted page-layout div.page-layout-body.layout-row.cb-overflow-y-only.layout-align-center-center div div.auth-page-body authentication mat-card.mat-card.mat-focus-indicator mat-tab-group.mat-tab-group.mat-primary.mat-tab-group-dynamic-height div.mat-tab-body-wrapper mat-tab-body#mat-tab-content-0-0.mat-tab-body.ng-tns-c164-13.mat-tab-body-active.ng-star-inserted div.mat-tab-body-content.ng-tns-c164-13.ng-trigger.ng-trigger-translateTab login.ng-star-inserted form.ng-pristine.ng-invalid.ng-touched mat-form-field.mat-form-field.ng-tns-c64-7.mat-primary.mat-form-field-type-mat-input.mat-form-field-appearance-legacy.mat-form-field-can-float.mat-form-field-has-label.mat-form-field-hide-placeholder.ng-pristine.ng-star-inserted.ng-invalid.ng-touched div.mat-form-field-wrapper.ng-tns-c64-7 div.mat-form-field-flex.ng-tns-c64-7 div.mat-form-field-infix.ng-tns-c64-7 input#mat-input-1.mat-input-element.mat-form-field-autofill-control.ng-tns-c64-7.ng-pristine.cdk-text-field-autofill-monitored.ng-invalid.ng-touched
# #mat-input-1
driver.find_element_by_css_selector("#mat-input-1").send_keys(os.getenv("CRUNCHBASE_USERNAME"))

sleep(5)

driver.find_element_by_css_selector("#mat-input-2").send_keys(os.getenv("CRUNCHBASE_PASSWORD"))

sleep(5)

driver.find_element_by_css_selector(".login > span:nth-child(1)").click()

# element = driver.find_element_by_xpath("//*[@id='XKUshpnrwCKnKib']")
# driver.find_element_by_xpath("/html/body/chrome/div/app-header/div[1]/div[2]/div/anon-nav-row/nav-action-item[2]/nav-header-action-item/a/span[1]/nav-action-item-header-layout/div/span").click()

# element = driver.find_element_by_xpath("//*[@id="xfyfCpukmxdcbAy"]")
# html body div div#qkpjHtIwUPyyPkx.eeEUtXHWfaHsNOL div#smjLtDykvuVasYe div#VwpICELMmZMpVvb p#QapfVeOYmHEEFMi.gLFYKbcwwtGkQNC
# element = driver.find_element_by_css_selector("html body div div#qkpjHtIwUPyyPkx.eeEUtXHWfaHsNOL div#smjLtDykvuVasYe div#VwpICELMmZMpVvb p#QapfVeOYmHEEFMi.gLFYKbcwwtGkQNC")
# action.click_and_hold(on_element = element)
sleep(5)

driver.get("https://crunchbase.com/organization/amazon/people")

# driver.find_element_by_css_selector("#mat-input-1").send_keys("Finance")
# driver.find_element_by_css_selector("mat-form-field-infix input").send_keys("Finance")

# driver.find_element_by_css_selector(".mat-option-text").click()
#mat-input-1
# class="mat-form-field-infix ng-tns-c64-7"
# html body chrome div mat-sidenav-container.mat-drawer-container.mat-sidenav-container mat-sidenav-content.mat-drawer-content.mat-sidenav-content.ng-star-inserted div ng-component.ng-star-inserted entity-v2.ng-star-inserted page-layout div.page-layout-body.layout-column.layout-align-space-between div div.ng-star-inserted page-centered-layout.ng-star-inserted div.page-centered div.content-cards-layout div.main-content row-card.ng-star-inserted profile-section.ng-star-inserted section-card.ng-star-inserted mat-card.mat-card.mat-focus-indicator.mat-elevation-z3 div.section-content-wrapper div.section-content contacts-card.ng-star-inserted contacts-card-search.ng-star-inserted contacts-search div.searchbar-row.static-search div.searchbar multi-select-input.ng-star-inserted form.component--input.component--multi-select-input.ng-untouched.ng-pristine.ng-valid div.chips-container mat-form-field.mat-form-field.ng-tns-c64-7.mat-primary.mat-form-field-type-mat-input.mat-form-field-appearance-legacy.mat-form-field-has-label.mat-form-field-hide-placeholder.ng-pristine.ng-valid.ng-star-inserted.ng-touched div.mat-form-field-wrapper.ng-tns-c64-7 div.mat-form-field-flex.ng-tns-c64-7 div.mat-form-field-infix.ng-tns-c64-7 input#mat-input-1.mat-input-element.mat-form-field-autofill-control.mat-autocomplete-trigger.ng-tns-c64-7.ng-pristine.ng-valid.cdk-text-field-autofill-monitored.ng-touched
# html body chrome div mat-sidenav-container.mat-drawer-container.mat-sidenav-container mat-sidenav-content.mat-drawer-content.mat-sidenav-content.ng-star-inserted div ng-component.ng-star-inserted entity-v2.ng-star-inserted page-layout div.page-layout-body.layout-column.layout-align-space-between div div.ng-star-inserted page-centered-layout.ng-star-inserted div.page-centered div.content-cards-layout div.main-content row-card.ng-star-inserted profile-section.ng-star-inserted section-card.ng-star-inserted mat-card.mat-card.mat-focus-indicator.mat-elevation-z3 div.section-content-wrapper div.section-content contacts-card.ng-star-inserted contacts-card-search.ng-star-inserted contacts-search div.searchbar-row.static-search div.searchbar multi-select-input.ng-star-inserted form.component--input.component--multi-select-input.ng-untouched.ng-pristine.ng-valid div.chips-container mat-form-field.mat-form-field.ng-tns-c64-98.mat-primary.mat-form-field-type-mat-input.mat-form-field-appearance-legacy.mat-form-field-has-label.mat-form-field-hide-placeholder.ng-valid.ng-star-inserted.ng-touched.ng-dirty div.mat-form-field-wrapper.ng-tns-c64-98 div.mat-form-field-flex.ng-tns-c64-98 div.mat-form-field-infix.ng-tns-c64-98 input#mat-input-21.mat-input-element.mat-form-field-autofill-control.mat-autocomplete-trigger.ng-tns-c64-98.ng-valid.cdk-text-field-autofill-monitored.ng-touched.ng-dirty
# html body chrome div mat-sidenav-container.mat-drawer-container.mat-sidenav-container mat-sidenav-content.mat-drawer-content.mat-sidenav-content.ng-star-inserted div ng-component.ng-star-inserted entity-v2.ng-star-inserted page-layout div.page-layout-body.layout-column.layout-align-space-between div div.ng-star-inserted page-centered-layout.ng-star-inserted div.page-centered div.content-cards-layout div.main-content row-card.ng-star-inserted profile-section.ng-star-inserted section-card.ng-star-inserted mat-card.mat-card.mat-focus-indicator.mat-elevation-z3 div.section-content-wrapper div.section-content contacts-card.ng-star-inserted contacts-card-search.ng-star-inserted contacts-search div.searchbar-row.static-search div.searchbar multi-select-input.ng-star-inserted form.component--input.component--multi-select-input.ng-untouched.ng-pristine.ng-valid div.chips-container mat-form-field.mat-form-field.ng-tns-c64-98.mat-primary.mat-form-field-type-mat-input.mat-form-field-appearance-legacy.mat-form-field-has-label.mat-form-field-hide-placeholder.ng-valid.ng-star-inserted.ng-touched.ng-dirty div.mat-form-field-wrapper.ng-tns-c64-98 div.mat-form-field-flex.ng-tns-c64-98 div.mat-form-field-infix.ng-tns-c64-98
# html.cookies.cors.json.queryselector.websockets.supports.no-touchevents.cssanimations.csstransforms3d.csstransitions body chrome div mat-sidenav-container.mat-drawer-container.mat-sidenav-container mat-sidenav-content.mat-drawer-content.mat-sidenav-content.ng-star-inserted div ng-component.ng-star-inserted entity-v2.ng-star-inserted page-layout div.page-layout-body.layout-column.layout-align-space-between div div.ng-star-inserted page-centered-layout.ng-star-inserted div.page-centered div.content-cards-layout div.main-content row-card.ng-star-inserted profile-section.ng-star-inserted section-card.ng-star-inserted mat-card.mat-card.mat-focus-indicator.mat-elevation-z3 div.section-content-wrapper div.section-content contacts-card.ng-star-inserted contacts-card-search.ng-star-inserted contacts-search div.searchbar-row.static-search div.searchbar multi-select-input.ng-star-inserted form.component--input.component--multi-select-input.ng-untouched.ng-pristine.ng-valid div.chips-container mat-form-field.mat-form-field.ng-tns-c64-7.mat-primary.mat-form-field-type-mat-input.mat-form-field-appearance-legacy.mat-form-field-has-label.mat-form-field-hide-placeholder.ng-pristine.ng-valid.ng-star-inserted.ng-touched div.mat-form-field-wrapper.ng-tns-c64-7 div.mat-form-field-flex.ng-tns-c64-7 div.mat-form-field-infix.ng-tns-c64-7
# html.cookies.cors.json.queryselector.websockets.supports.no-touchevents.cssanimations.csstransforms3d.csstransitions body chrome div mat-sidenav-container.mat-drawer-container.mat-sidenav-container mat-sidenav-content.mat-drawer-content.mat-sidenav-content.ng-star-inserted div ng-component.ng-star-inserted entity-v2.ng-star-inserted page-layout div.page-layout-body.layout-column.layout-align-space-between div div.ng-star-inserted page-centered-layout.ng-star-inserted div.page-centered div.content-cards-layout div.main-content row-card.ng-star-inserted profile-section.ng-star-inserted section-card.ng-star-inserted mat-card.mat-card.mat-focus-indicator.mat-elevation-z3 div.section-content-wrapper div.section-content contacts-card.ng-star-inserted contacts-card-search.ng-star-inserted contacts-search div.searchbar-row.static-search div.searchbar multi-select-input.ng-star-inserted form.component--input.component--multi-select-input.ng-untouched.ng-pristine.ng-valid div.chips-container mat-form-field.mat-form-field.ng-tns-c64-7.mat-primary.mat-form-field-type-mat-input.mat-form-field-appearance-legacy.mat-form-field-has-label.mat-form-field-hide-placeholder.ng-pristine.ng-valid.ng-star-inserted.ng-touched div.mat-form-field-wrapper.ng-tns-c64-7 div.mat-form-field-flex.ng-tns-c64-7 div.mat-form-field-infix.ng-tns-c64-7
driver.find_element(by=By.CSS_SELECTOR, value=".cb-text-transform-upper > span:nth-child(1) > span:nth-child(2)").click()
sleep(20)

# driver.quit()