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

def visible(a):
    return a.is_displayed() and a.is_enabled()

def main():
    SEED = 'http://blog.zipfianacademy.com/post/46864003608/a-practical-intro-to-data-science'
    driver = driver_setup()
    driver.get(SEED)
    while True:
        anchors = filter(visible, driver.find_elements_by_xpath('//a'))
        if len(anchors) > 0:
            choice(anchors).click()
        else:
            driver.get(SEED)
        randomsleep()
        print(u'Loaded ' + driver.current_url)

if __name__ == '__main__':
    main()
