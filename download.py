import time

import numpy as np
from selenium import webdriver

driver = webdriver.Chrome("C:/Users/Graham/Desktop/python/terrain/chromedriver.exe")
##https://tangrams.github.io/heightmapper/#15/33.8030/-84.1453


## Gets a random heightmap from latitude and longitude between two values.
## TODO: Add ability to pass in the clamp areas based on parameters.
def coords():
    lat = np.random.uniform(30.0000, 36.0000)
    lon = np.random.uniform(-82.0000, -86.0000)

    ##Format the string to fit the URL for the chromedriver on refresh.
    coords = '/' + str(round(lat, 4)) + '/' + str(round(lon, 4))

    return coords

## Loops 60 times to elegantly click a download button.
for x in range(0, 60):
    ## First we generate a new URL with a random location from coords.
    ## TODO: add ability to pass in zoom level as well.
    ## Zoom is determined by the #15 in the url string.
    url = 'https://tangrams.github.io/heightmapper/#15' + coords()

    ## For some reason, we need to assign a new webdriver every iteration.

    action = webdriver.ActionChains(driver)
    driver.get(url)
    driver.refresh()

    ## Sleep for 3 seconds so as not to overload the poor server host.
    time.sleep(3)

    ## This is clicking a "download" button which saves to the default directory.
    ## This offset is unique to my computer.
    ## I tried to get the screenshot button by xpath, but it wasn't working.
    ## TODO: add ability to pass in the offset as well.
    action.move_by_offset(985, 215)
    action.click().perform()
    action.reset_actions()

driver.quit()
