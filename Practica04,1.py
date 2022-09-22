from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome("./chromedriver.exe")
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
action = ActionChains(driver)

src = driver.find_element(By.XPATH, '//*[@id="box1"]')
dest = driver.find_element(By.XPATH, '//*[@id="box101"]')
action.drag_and_drop(src, dest).perform()

src = driver.find_element(By.XPATH, '//*[@id="box2"]')
dest = driver.find_element(By.XPATH, '//*[@id="box102"]')
action.drag_and_drop(src, dest).perform()

src = driver.find_element(By.XPATH, '//*[@id="box3"]')
dest = driver.find_element(By.XPATH, '//*[@id="box103"]')
action.drag_and_drop(src, dest).perform()

src = driver.find_element(By.XPATH, '//*[@id="box4"]')
dest = driver.find_element(By.XPATH, '//*[@id="box104"]')
action.drag_and_drop(src, dest).perform()

src = driver.find_element(By.XPATH, '//*[@id="box5"]')
dest = driver.find_element(By.XPATH, '//*[@id="box105"]')
action.drag_and_drop(src, dest).perform()

src = driver.find_element(By.XPATH, '//*[@id="box6"]')
dest = driver.find_element(By.XPATH, '//*[@id="box106"]')
action.drag_and_drop(src, dest).perform()

src = driver.find_element(By.XPATH, '//*[@id="box7"]')
dest = driver.find_element(By.XPATH, '//*[@id="box107"]')
action.drag_and_drop(src, dest).perform()



