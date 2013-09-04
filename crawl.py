#!/usr/bin/env python
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from random import normalvariate, choice
from time import sleep

def randomsleep():
    seconds = normalvariate(10, 20)
    seconds = min(max(2, seconds), 60)
    sleep(seconds)

def driver_setup():
    desired_capabilities = webdriver.DesiredCapabilities.CHROME
    desired_capabilities['name'] = 'Chrome database sprint data collection'
    driver = webdriver.Remote(desired_capabilities=desired_capabilities,command_executor="http://localhost:4444/wd/hub")
    return driver

def main():
    driver = driver_setup()
    driver.get('http://zipfianacademy.com')
    while True:
        choice(driver.find_elements_by_xpath('//a')).click()
        randomsleep()
        print(u'Loaded ' + d.current_url)

if __name__ == '__main__':
    main()
