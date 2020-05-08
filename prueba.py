from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Descargar el driver de chrome  ponerlo en /usr/local/bin/
# se puede descargar el driver de https://chromedriver.chromium.org/downloads
driver = webdriver.Chrome("/usr/local/bin/chromedriver")
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("py")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()
