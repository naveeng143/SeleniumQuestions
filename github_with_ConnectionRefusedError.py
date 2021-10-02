from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("./chromedriver")
driver.get("https://github.com")

print(driver.title)
assert "GitHub" in driver.title

elem = driver.find_element_by_name("q")
elem.send_keys("dzitkowskik")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source

driver.quit()
driver.title() # ConnectionRefusedError: [Errno 61] Connection refused

==================================================================


from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("./chromedriver")
driver.get("https://github.com")

print(driver.title)
assert "GitHub" in driver.title

elem = driver.find_element_by_name("q")
elem.send_keys("dzitkowskik")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source

driver.close() # selenium.common.exceptions.InvalidSessionIdException: Message: invalid session id
driver.title()
