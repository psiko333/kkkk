
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import FirefoxProfile, ChromeOptions
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
from webdriver_setup import get_webdriver_for
from autopilot.input import Mouse

from config import logger
import random

def delay():
        chance = random.randint(1,10)
        if chance > 1:
                timer = int(random.randint(1, 7))
                time.sleep(timer)
                print("Sleep "+str(timer)+ " seconds")
                mouse = Mouse.create()
                x = random.randint(100,700)
                y = random.randint(200,800)
                mouse.move(x,y)
                mouse.click()
        else:
                return

def scroller(seleniums):
        chance = random.randint(1,2)
        if chance == 1:
                scroll = str(random.randint(-500, 500))
                seleniums.execute_script("window.scrollBy(0,"+scroll+");")
                print("Scrolling")
        else:
                return
     

def clicker(seleniums):
        #Clicking on an add
        print("Playing the lottery")
        clicker = random.randint(1,100)
        if clicker < 6:
                delay()
                mouse = Mouse.create()
                x = random.randint(150,400)
                mouse.move(x,1100)
                delay()
                logger.info(f"Clicking on an ad")
                mouse.click()
                delay()
                seleniums.quit()
                return 1
        else:
                logger.info(f"Failed Click")
                delay()
                scroller(seleniums)
                return 5


def browser(seleniums):
        navigate = random.randint(1,10)
        print("Looking around")
        if navigate < 3:
                element = seleniums.find_element_by_link_text("Projects")
                element.click()
                delay()
        elif navigate < 5:
                element = seleniums.find_element_by_link_text("Contact")
                element.click()
                delay()
        else:
                return
