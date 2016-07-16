from bs4 import BeautifulSoup
import argparse, os, time
import urlparse, random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def send(username, password, mobile, message):
  
	driver = webdriver.Firefox()
	driver.get("http://site25.way2sms.com/content/index.html")

	driver.find_element_by_id("username").send_keys(username)
	driver.find_element_by_id("password").send_keys(password)
	driver.find_element_by_id("loginBTN").send_keys(Keys.RETURN)
	time.sleep(2)
	url = driver.current_url
	time.sleep(3)
	print url

	print "Login successfull"

	driver.execute_script("goToMain('s')")
	driver.execute_script("loadSMSPage('sendSMS')")

	frame = driver.find_element_by_id("frame")
	driver.switch_to_frame(frame)

	driver.find_element_by_id("mobile").send_keys(mobile)
	driver.find_element_by_id("message").send_keys(message)
	driver.find_element_by_id("Send").send_keys(Keys.RETURN)
	time.sleep(10)
	driver.get(url)
	time.sleep(3)

	driver.execute_script("logout()")
	time.sleep(5)
	print "logout successfull"

	driver.switch_to_default_content()
	driver.close()

def main():
	username = raw_input("Enter the username\n")
	password = raw_input("Enter the password\n")
	mobile = raw_input("Enter the mobile number\n")
	message = raw_input("Enter the message\n")

	send(username,password,mobile,message)



if __name__ == '__main__':
	main()