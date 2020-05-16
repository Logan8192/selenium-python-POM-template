import os
from pathlib import Path
from selenium import webdriver
import json


class Base:
    driver = None

    @staticmethod
    def start_driver():
        """
        Starts a selenium web driver instance.
        :return: Driver instance.
        """
        driver = webdriver.Firefox(
            executable_path=str(Path(os.path.dirname(__file__)).parent / "drivers/linux/geckodriver"))
        driver.maximize_window()
        driver.get("https://duckduckgo.com")
        return driver

    @staticmethod
    def open_datafile(datafile):
        """
        Opens a test datafile by its name.
        :param datafile: (string) Name of the datafile.
        :return: Datafile content.
        :rtype: dict
        """
        datafile = Path(os.path.dirname(__file__)).parent / F"data/{datafile}"
        return json.loads(datafile.read_text())
