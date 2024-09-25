import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

class Driver:
    _instance = None

    def __new__(cls):
        """Ensure only one instance of the WebDriver is created."""
        browser="Chrome"
        if cls._instance is None:
            cls._instance = super(Driver, cls).__new__(cls)
            if browser.lower() == 'chrome':
                chrome_options = ChromeOptions()
                cls._instance.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
            elif browser.lower() == 'firefox':
                firefox_options = FirefoxOptions()
                cls._instance.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=firefox_options)
            else:
                raise ValueError(f"Unsupported browser: {browser}")
        return cls._instance

    def get_driver(self):
        """Return the WebDriver instance."""
        return self.driver

    def quit(self):
        """Quit the WebDriver instance."""
        if self.driver:
            self.driver.quit()
            Driver._instance = None  # Reset instance to allow recreation if needed
