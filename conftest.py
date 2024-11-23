import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(
            headless=False,
            slow_mo=750,
        )
        context = browser.new_context(viewport={"width": 1920, "height": 1200})
        page = context.new_page()
        yield page
        browser.close()
