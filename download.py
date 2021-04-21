import time

import numpy as np
from selenium import webdriver

driver = webdriver.Chrome("C:/Users/Graham/Desktop/python/terrain/chromedriver.exe")
##https://tangrams.github.io/heightmapper/#15/33.8030/-84.1453
##Stone Mountain, GA

def coords():
    lat = np.random.uniform(30.0000, 36.0000)
    lon = np.random.uniform(-82.0000, -86.0000)
    coords = '/' + str(round(lat, 4)) + '/' + str(round(lon, 4))
    print(coords)
    return coords


for x in range(0, 20):
    action = webdriver.ActionChains(driver)
    url = 'https://tangrams.github.io/heightmapper/#15' + coords()
    driver.get(url)
    driver.refresh()
    time.sleep(2)
    action.move_by_offset(985, 215)
    action.click().perform()
    action.reset_actions()

driver.quit()
