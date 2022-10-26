import os
import getpass
from argparse import ArgumentParser
import time
import random
import requests
from stem import Signal
from stem.control import Controller

from config import logger
from search_controller import SearchController
from profiles import delay

def change_ip_address(password):
    """Change IP address over Tor connection

    :type password: str
    :param password: Tor authentication password
    """

    logger.info("Changing ip address...")
    with Controller.from_port(port=9051) as controller:
        controller.authenticate(password=password)
        controller.signal(Signal.NEWNYM)
        response = requests.get("https://api.myip.com", proxies={"https": "socks5h://127.0.0.1:9050"})
        if {response.json()['country']} == "unknown":
            print("Retry Search")
            change_ip_address(password)
        else:
            print("Good Location")
            return


def main():

    os.environ["WDM_LOG_LEVEL"] = "0"
    password = os.environ.get("TOR_PWD", None)

    if not password:
        password = getpass.getpass("Enter tor password: ")

    change_ip_address(password)

    response = requests.get("https://api.myip.com", proxies={"https": "socks5h://127.0.0.1:9050"})
    logger.info(f"Connecting with IP: {response.json()['ip']} from {response.json()['country']}")

    wait = random.randint(1, 6)
    if wait > 4:
        browser = "firefox"
    else:
        browser = "chrome"
        
    logger.info(f"Using {browser} browser")

    delay()
    search_controller = SearchController("test", "chrome", 5)
    ads = search_controller.act_human()
'''
    if not ads:
        logger.info("No ads in the search results!")
    else:
        logger.info(f"Found {len(ads)} ads")
        search_controller.click_ads(ads)
        search_controller.end_search()
'''

if __name__ == "__main__":

    i = 1
    while i ==1:
        time.sleep(10)
        main()
