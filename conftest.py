import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(
            headless=False,
            slow_mo=750,
        )
        yield browser
        browser.close()
