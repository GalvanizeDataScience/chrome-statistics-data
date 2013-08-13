Chrome browser history database
==========

## Loading your own data



## Creating random data
Install Chrome, Selenium and the Selenium driver for Python.

If you're using a virtual framebuffer, start it like so

    Xvfb :99 -ac &
    export DISPLAY=:99seleniumrc

Run Selenium.

    java -jar selenium-server-standalone-2.35.0.jar

And run the crawler script.

    ./crawl.py
