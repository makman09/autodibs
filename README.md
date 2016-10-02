# Autodibs #

A python scripts that lets you allow to reserve rooms automatically.
It uses Selenium on PhantomJS in python to reserve room for you.

## Get it running ##

In order to use this you need to install some dependencies

'''
    pip install selenium
'''

You can choose to either use phanthomjs as the headless browser or something
easier, but slow like Chrome. 

[Install phantomjs](http://phantomjs.org/build.html)

Be sure to change the webdriver in 'autodibs.py' to phantomjs if you
plan on using phantomjs

[Install chrome driver](https://sites.google.com/a/chromium.org/chromedriver/getting-started)

Be sure to install Chrome before you install the chrome driver

Once you have those running, you can start automating reservations`

be sure to populate the barcode.json file with student barcodes found 
on the back of student ids

## Limitation of UCSD DIBS ##

You can only have upto 3 active reservation overall. You can reserve again 
if you cancel your reservation or removed it.

## Monopolize the study rooms industry ##