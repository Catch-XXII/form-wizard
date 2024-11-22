from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate_to_url(self, url: str):
        self.page.goto(url)

    def fill_text(self, selector: str, text: str):
        self.page.locator(selector).fill(text)

    def upload_file(self, selector: str, file_path: str):
        self.page.set_input_files(selector, file_path)

    def select_from_radio_button(self, value: str):
        self.page.get_by_text(value, exact=True).click()

    def submit_form(self, selector: str):
        self.page.locator(selector).click()

    def retrieve_and_click_by(self, text):
        self.page.get_by_text(text, exact=True).click()

    def has_title(self, title):
        expect(self.page).to_have_title(title)

    def expect_contain_text(self, selector, text):
        expect(self.page.locator(selector)).to_contain_text(text)

    def fill_calendar(self, selector, year, dob):
        self.page.locator(selector).click()
        self.page.get_by_role("combobox").nth(1).select_option(year)
        self.page.get_by_label(dob).click()

    def multiple_selection(self, selector, option1, option2):
        self.page.locator(selector).fill(option1)
        self.retrieve_and_click_by("Computer Science")
        self.page.locator(selector).fill(option2)
        self.retrieve_and_click_by("English")

    def drop_down_selection(self, selector, value):
        self.page.locator(selector).click()
        self.page.get_by_text(value, exact=True).click()
