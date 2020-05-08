from src import config
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

option = Options()

option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

option.add_experimental_option("prefs", { 
    "profile.default_content_setting_values.notifications": 1 
})

# Descargar el driver de chrome  ponerlo en /usr/local/bin/
# se puede descargar el driver de https://chromedriver.chromium.org/downloads
driver = webdriver.Chrome(chrome_options=option, executable_path="/usr/local/bin/chromedriver")
driver.get("https://www.facebook.com/")

email = config.EMAIL
password = config.PASSWORD

email_xpath = '//*[@id="email"]'
password_xpath = '//*[@id="pass"]'
login_button_xpath = '//*[@id="u_0_b"]'

email_element = driver.find_element_by_xpath(email_xpath)
password_element = driver.find_element_by_xpath(password_xpath)
login_button_element = driver.find_element_by_xpath(login_button_xpath)

email_element.send_keys(email)
password_element.send_keys(password)
login_button_element.click()
time.sleep(5)


search_class = '_1frb'
search_button_xpath = '//*[@id="js_1q"]/form/button'

# search_element = driver.find_element_by_xpath(search_xpath)
search_element = driver.find_element_by_class_name(search_class)
busqueda = 'Maika Makovski'
search_element.send_keys(busqueda)

search_button_element = driver.find_element_by_xpath('//*[@id="js_z"]/form/button')
search_button_element.click()


# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("py")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
#driver.close()
