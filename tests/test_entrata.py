import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logger = logging.getLogger(__name__)

# Test 1: Verify the homepage title contains 'Entrata'
def test_homepage_title(setup):
    logger.info("Navigating to the homepage")
    setup.get("https://www.entrata.com")
    logger.info(f"Page title: {setup.title}")
    assert "Entrata" in setup.title, "Title does not contain 'Entrata'!"

# Test 2: Navigate to the Careers page and verify the title contains 'Careers'
def test_careers_page_navigation(setup):
    logger.info("Navigating to the Careers page")
    setup.get("https://www.entrata.com")
    
    careers_link = WebDriverWait(setup, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href*='careers']"))
    )
    careers_link.click()

    logger.info(f"Page title: {setup.title}")
    
    WebDriverWait(setup, 10).until(EC.title_contains("Entrata Career"))
    logger.info(f"Page title: {setup.title}")
    assert "Entrata Career" in setup.title, "Title does not contain 'Entrata Career'!"

# Test 3: Verify dynamic content by checking Resident Login button visibility
def test_dynamic_content(setup):
    logger.info("Verifying Resident Login button visibility")
    setup.get("https://www.entrata.com")
    
    resident_login_btn = WebDriverWait(setup, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//a[@class='footer-link black'][normalize-space()='ResidentPortal']"))
        )
    logger.info("Resident Login button is visible")
    assert resident_login_btn.is_displayed(), "Resident Login button is not visible!"

