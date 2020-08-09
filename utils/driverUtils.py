import argparse
import json
import os
import sys
from pathlib import Path

from selenium import webdriver


def start_driver():
    """
    Starts a selenium web driver instance. Its necessary to set the name of the driver as command-line argument
    "--driver_name {driver_name}".

    Available drivers.

    - Linux:
        - Chrome: CHROME_LINUX
        - Firefox: FIREFOX_LINUX
        - Opera: OPERA_LINUX

    - Windows:
        - Chrome: CHROME_WINDOWS
        - Edge (Chromium): EDGE_CHROMIUM_WINDOWS
        - Firefox: FIREFOX_WINDOWS
        - Opera: OPERA_WINDOWS

    :return: Driver instance.
    """
    driver = None

    # Setting driver_name command-line argument.
    parser = argparse.ArgumentParser()
    parser.add_argument("--driver_name", type=str, choices=["CHROME_LINUX", "FIREFOX_LINUX", "OPERA_LINUX",
                                                            "CHROME_WINDOWS", "EDGE_CHROMIUM_WINDOWS",
                                                            "FIREFOX_WINDOWS", "OPERA_WINDOWS"],
                        dest="driver_name")
    driver_name = parser.parse_args().driver_name

    # Removing --driver_name optional argument and driver_name argument.
    sys.argv.remove("--driver_name")
    sys.argv.remove(driver_name)

    # Starting the chosen driver.
    if driver_name == "FIREFOX_LINUX":
        driver = webdriver.Firefox(
            executable_path=str(Path(os.path.dirname(__file__)).parent / "drivers/linux/geckodriver"))
    elif driver_name == "CHROME_LINUX":
        driver = webdriver.Chrome(
            executable_path=str(Path(os.path.dirname(__file__)).parent / "drivers/linux/chromedriver"))
    elif driver_name == "OPERA_LINUX":
        driver = webdriver.Opera(
            executable_path=str(Path(os.path.dirname(__file__)).parent / "drivers/linux/operadriver"))
    elif driver_name == "FIREFOX_WINDOWS":
        driver = webdriver.Firefox(
            executable_path=str(Path(os.path.dirname(__file__)).parent / "drivers/windows/geckodriver.exe"),
            log_path=Path(os.path.dirname(__file__)).parent / "drivers/windows/geckodriver.log")
    elif driver_name == "CHROME_WINDOWS":
        driver = webdriver.Chrome(
            executable_path=str(Path(os.path.dirname(__file__)).parent / "drivers/windows/chromedriver.exe"))
    elif driver_name == "OPERA_WINDOWS":
        driver = webdriver.Opera(
            executable_path=str(Path(os.path.dirname(__file__)).parent / "drivers/windows/operadriver.exe"))
    elif driver_name == "EDGE_CHROMIUM_WINDOWS":
        driver = webdriver.Edge(
            executable_path=str(Path(os.path.dirname(__file__)).parent / "drivers/windows/msedgedriver.exe"))
    driver.maximize_window()
    driver.get("https://duckduckgo.com")
    return driver
