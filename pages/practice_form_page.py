from playwright.sync_api import Page
from base import BasePage


class PracticeFormPage(BasePage):
    # Variables
    _URL = "https://demoqa.com/"
    _TITLE = "DEMOQA"
    _PAGE_TITLE = "Practice Form"
    _FORM_TITLE = "Student Registration Form"
    _FIRST_NAME = "John"
    _LAST_NAME = "Doe"
    _EMAIL = "b@b"
    _GENDER = "Male"
    _YEAR = "2000"
    _DATE_OF_BIRTH = "Choose Saturday, November 4th,"
    _SUBJECT_1 = "Computer"
    _SUBJECT_2 = "Eng"
    _SPORTS = "Sports"
    _READING = "Reading"
    _MUSIC = "Music"
    _FILE_NAME = "../base/image/cuneyd.jpg"
    _ADDRESS = "Jonquil, Grandchild Center, Big Stream Avenue Shishli/İstanbul"
    _STATE = "Haryana"
    _CITY = "Panipat"

    def __init__(self, page: Page):
        super().__init__(page)
        self.first_name = "id=firstName"
        self.last_name = "id=lastName"
        self.email = "id=userEmail"
        self.mobile_phone_number = "id=userNumber"
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
