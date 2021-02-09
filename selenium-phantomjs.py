from selenium import webdriver

driver = webdriver.Phantomjs(executable_path=r"REPLACE_WITH_PATH_NAME")

driver.get('http://python.org')

html_output = driver.page_source

print(html_output)
