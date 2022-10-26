from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import FirefoxProfile, ChromeOptions
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from time import sleep
from webdriver_setup import get_webdriver_for
from autopilot.input import Mouse
import profiles

from config import logger
import random


class SearchController:

    site = int(random.randint(1,10))
    if site >= 6:
        URL = "https://www.hackanything.net"
    elif site == 5:
        URL = "https://www.hackanything.net/post/beating-video-games-by-hacking"
    elif site == 4:
        URL = "https://www.hackanything.net/post/chapter-1"
    elif site == 3:
        URL = "https://www.hackanything.net/post/setting-up-kali-linux-in-the-cloud-for-free"
    else:    
        URL = "https://www.hackanything.net/post/2021_kringlecon"
        

    def __init__(self, query, browser="firefox", ad_visit_time=4):

        self.s_search_query = query
        self._ad_visit_time = ad_visit_time

        self._driver = self._create_driver(browser.lower())
        self._load()

    def act_human(self):

        activity = random.randint(1,20)
        while activity != 1:
            activity = random.randint(1,20)
            print("Activity is "+ str(activity))
            if activity <= 11:
                profiles.delay()
                profiles.scroller(self._driver)
        
            elif activity <= 15:
                profiles.delay()
                profiles.browser(self._driver)
                
            else:        
                profiles.delay()
                activity = profiles.clicker(self._driver)
               
        self._driver.quit()


    def _create_driver(self, browser):
        """Create Selenium webdriver instance for the given browser

        Setup proxy if the browser is Firefox or Chrome

        :type browser: str
        :param browser: Browser name
        :rtype: selenium.webdriver
        :returns: Selenium webdriver instance
        """

        try:
            proxy = self._setup_proxy(browser)

            if browser == "firefox":
                driver = get_webdriver_for(browser, firefox_profile=proxy)
            elif browser == "chrome":
                driver = get_webdriver_for(browser, chrome_options=proxy)
            else:
                driver = get_webdriver_for(browser)

        except ValueError:
            logger.error(f"{browser} is not installed on your system!")
            raise SystemExit()

        return driver

    def _setup_proxy(self, browser):
        """Setup proxy for Firefox or Chrome

        :type browser: str
        :param browser: Browser name
        :rtype: selenium.webdriver.FirefoxProfile or selenium.webdriver.ChromeOptions
        :returns: Proxy settings
        """

        host = "127.0.0.1"
        port = "9050"

        if browser == "firefox":
            firefox_profile = FirefoxProfile()
            # Direct = 0, Manual = 1, PAC = 2, AUTODETECT = 4, SYSTEM = 5
            firefox_profile.set_preference("network.proxy.type", 1)
            firefox_profile.set_preference("network.proxy.socks", host)
            firefox_profile.set_preference("network.proxy.socks_port", int(port))
            firefox_profile.update_preferences()

            return firefox_profile

        elif browser == "chrome":
            proxy = f"socks5://{host}:{port}"
            chrome_options = ChromeOptions()
            chrome_options.add_argument(f"--proxy-server={proxy}")

            return chrome_options

        else:
            logger.info(f"No proxy setting was done for {browser}")

    def _load(self):

        self._driver.get(self.URL)
