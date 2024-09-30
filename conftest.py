import pytest
import logging
from selenium import webdriver

@pytest.fixture(scope="session", autouse=True)
def configure_logging():
    logging.basicConfig(
        filename="test_log.log",        
        filemode="w",                    
        level=logging.INFO,              
        format="%(asctime)s - %(levelname)s - %(message)s", 
    )
    logger = logging.getLogger()
    logger.info("Starting test execution...")


@pytest.fixture(scope="function")
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
