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
        - Firefox: FIREFOX_WINDOWS
        - Chrome: CHROME_WINDOWS

    :return: Driver instance.
    """
    driver = None

    # Setting driver_name command-line argument.
    parser = argparse.ArgumentParser()
    parser.add_argument("--driver_name", type=str, choices=["CHROME_LINUX", "FIREFOX_LINUX", "OPERA_LINUX",
                                                            "CHROME_WINDOWS", "FIREFOX_WINDOWS"],
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
    driver.maximize_window()
    driver.get("https://duckduckgo.com")
    return driver


def open_datafile(datafile):
    """
    Opens a test datafile by its name.
    :param datafile: (string) Name of the datafile.
    :return: Datafile content.
    :rtype: dict
    """
    datafile = Path(os.path.dirname(__file__)).parent / F"data/{datafile}"
    return json.loads(datafile.read_text())
