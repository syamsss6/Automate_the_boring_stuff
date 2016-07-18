from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
browser=webdriver.Firefox()
browser.get('https://gabrielecirulli.github.io/2048/')
container=browser.find_element_by_class_name('game-container')
container.click()
keys=['LEFT','UP','DOWN','RIGHT']

container.send_keys(Keys.DOWN)
for i  in range(50):
	choice=random.choice(keys)
	container.send_keys('Keys.'+choice)
print(i)
