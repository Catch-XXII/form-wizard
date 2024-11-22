from pages.base_page import BasePage
from playwright.sync_api import Page


class PracticeFormPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.first_name = page.locator("id=firstName")
        self.last_name = page.locator("id=lastName")
        self.email = page.locator("id=userEmail")
        self.gender = page.locator("id=gender-radio-1")
        self.mobile_phone_number = page.locator("id=userNumber")
        self.dob = "#dateOfBirthInput"
        self.subjects = "#subjectsInput"
        self.picture = "id=uploadPicture"
        self.address = "id=currentAddress"
        self.state = "#state svg"
        self.city = "#city svg"
        self.submit_button = "id=submit"
        self.close_button = "id=closeLargeModal"
        self.validation_table = "tbody"

    def is_valid(self):
        self.page.evaluate(
            """
         document.querySelector("#userForm").checkValidity()
        """
        )
