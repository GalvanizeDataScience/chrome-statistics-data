#!/usr/bin/env python
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from random import normalvariate, choice
from time import sleep

def randomsleep():
    seconds=normalvariate(9, 3)
    if seconds>0:
        sleep(seconds)

def driver_setup():
    desired_capabilities = webdriver.DesiredCapabilities.CHROME
    desired_capabilities['name'] = 'Chrome database sprint data collection'
    driver = webdriver.Remote(desired_capabilities=desired_capabilities,command_executor="http://localhost:4444/wd/hub")
    return driver

def main():
    driver = driver_setup()
    driver.get(url)
    while True:
        choice(driver.find_elements_by_xpath('//a/@href')).click()
        randomsleep()
