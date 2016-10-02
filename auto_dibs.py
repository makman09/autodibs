import os
import datetime
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helpers import time_table, barcodes

# variable initialization
# driver = webdriver.Chrome('chromedriver')
driver = webdriver.PhantomJS()

'''
	@params barcode {string} - used to authenticate you into the system
	@params email {string} - used to confirm your reservation
	@params number {string} - used to confirm your reservation
'''
def auto_dibs(barcode, email, number):
	''' 
		Load into the login page and authenticate
	'''
	print 'authenticating into the page'
	driver.get('http://ucsd.evanced.info/dibs/login')
	driver.find_element_by_id('tbxPatronLibCard').send_keys(barcode)

	'''
		Confirm the page loaded
	'''
	driver.implicitly_wait(20) # seconds
	driver.find_element_by_id('btnLoginSubmit').click()
	driver.find_element_by_id('SelectedTime')

	'''
		Fill out the custom criteria
	'''
	print 'selecting the time range of room reservation'
	driver.find_element_by_css_selector("#SelectedTime > option[value='3']").click()
	driver.find_element_by_css_selector("#SelectedTimeSort > option[value='AnyTime']").click()

	# choose how many days in advance your want to reserve a room
	current_date = datetime.datetime.now()
	future_date = current_date + datetime.timedelta(days=10)
	future_date_formatted = future_date.strftime('%Y/%m/%d')

	element = WebDriverWait(driver, 20).until(
		EC.presence_of_element_located((By.CSS_SELECTOR, "#SelectedSearchDate > option[value='" + future_date_formatted + "']"))
	)
	element.click()

	driver.find_element_by_css_selector("input.btn-block").click()

	'''
		Confirm the library location page has loaded and load giesel rooms
	'''
	print 'selecting the library to reserve the room'
	elements = WebDriverWait(driver, 20).until(
		EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.item-link"))
	)

	# 0 for biomedical library, 1 for giesel library
	driver.find_elements_by_css_selector("div.item-link")[1].click()

	'''
		Load the times of rooms available 
	'''
	print 'choosing a room time'
	elements = WebDriverWait(driver, 20).until(
		EC.presence_of_element_located((By.CSS_SELECTOR, "form#frmTimes"))
	)

	# TODO better room selection from user input

	elements = driver.find_elements_by_css_selector("div.item-link")
	elements[len(elements)/2].click()

	'''
		Select the room
	'''
	print 'selecting the room'
	elements = WebDriverWait(driver, 20).until(
		EC.presence_of_element_located((By.CSS_SELECTOR, "form#frmRooms"))
	)

	elements = driver.find_elements_by_css_selector("div.item-link")
	elements[len(elements)/2].click()

	'''
		Confirm the room reservation
	'''
	print 'confirming the room reservation'
	element = WebDriverWait(driver, 20).until(
		EC.presence_of_element_located((By.CSS_SELECTOR, "input#EmailAddress"))
	)
	element.send_keys(email)
	driver.find_element_by_css_selector("input#Phone").send_keys(number)

	driver.find_element_by_css_selector("button#btnCallDibs").click()

for barcode in barcodes():
	auto_dibs(barcode["barcode"], barcode["email"], barcode["number"])

driver.quit()