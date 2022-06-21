from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://lms.umt.edu.pk/login/index.php")
driver.find_element_by_id("username").send_keys("yourID")
driver.find_element_by_id("password").send_keys("yourPassword")
driver.find_element_by_id("loginbtn").click()