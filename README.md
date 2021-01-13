# Python-Selenium-Unittest
Page Object Model pattern template using Python 3.8, unittest framework and Selenium web driver.

## Install Requirements:
Once the virtual environment for the repository is created and activated, run this command to download the project 
requirements: 
``` 
pip3 install -r requirements.txt 
```

## Running tests
Make sure to add the *"--driver_name"* command line parameter in order to set the browser where the test will be executed 
with the following values:

 - Linux:
    - **Chrome**: *CHROME_LINUX*
    - **Firefox**: *FIREFOX_LINUX*
    - **Opera**: *OPERA_LINUX*
 
 - Windows:
    - **Chrome**: *CHROME_WINDOWS*
    - **Edge (Chromium)**: EDGE_CHROMIUM_WINDOWS
    - **Firefox**: *FIREFOX_WINDOWS*
    - **Opera**: *OPERA_WINDOWS*

**Example:**
``` 
--driver_name FIREFOX_LINUX
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.