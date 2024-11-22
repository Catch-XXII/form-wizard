from utilities.phone_number_generator import generate_phone_number
from pages.practice_form_page import PracticeFormPage
from tests.base_test import TestBasePage
from playwright.sync_api import Page


class TestPracticeForm(TestBasePage):
    def test_assert_with_detail_pom(self, page: Page):
        """
        # Go to https://demoqa.com/
        # Assert web page title == DEMOQA
        # Click on "Forms"
        # Click on "Practice Form"
        # See Form loaded and Assert Title
        # Assert form name == Student Registration Form
        # Fill Name fields
        # First Name = John Last Name = Doe
        # Email = b@b
        # Gender = Male
        # Mobile = 123456789
        # Date of Birth = Choose Saturday, November 4th 2000
        # Subjects = Computer Science, English
        # Hobbies = Select all options
        # Picture = Upload local picture
        # Current Address = Jonquil, Grandchild Center, Big Stream Avenue Shishli/İstanbul
        # State = Haryana
        # City = Panipat
        # Click on Submit button
        # This will give you a validation error go back and fill missing fields
        # Assert document.querySelector("#userForm").checkValidity() == False
        # if not result:
        # email address with .com
        # 10 digit mobile phone number
        # Again Submit
        # See Table and make assertion for every field
        """
        # This variable will be used later on for assertion
        ten_digit_phone_number = generate_phone_number(10)

        register = PracticeFormPage(page)
        register.navigate_to_url(self._URL)
        register.has_title(self._TITLE)
        register.retrieve_and_click_by("Forms")
        register.retrieve_and_click_by("Practice Form")
        register.expect_contain_text("h1", self._PAGE_TITLE)
        register.expect_contain_text("h5", self._FORM_TITLE)
        register.first_name.fill(self._FIRST_NAME)
        register.last_name.fill(self._LAST_NAME)
        register.email.fill(self._EMAIL)
        register.select_from_radio_button(self._GENDER)
        register.mobile_phone_number.fill(generate_phone_number(9))
        register.fill_calendar(
            register.dob, self._YEAR, self._DATE_OF_BIRTH
        )
        register.fill_multiple_selection(
            register.subjects, self._SUBJECT_1, self._SUBJECT_2
        )
        register.retrieve_and_click_by(self._SPORTS)
        register.retrieve_and_click_by(self._READING)
        register.retrieve_and_click_by(self._MUSIC)
        register.upload_file(
            "input[type='file']",
            r"C:\Users\cuneyd.kaya\dev\WebUIAutomation\tests\cuneyd.jpg",
        )
        register.fill_text(register.address, self._ADDRESS)
        register.drop_down_selection(register.state, self._STATE)
        register.drop_down_selection(register.city, self._CITY)
        # Submit
        register.submit_form(register.submit_button)
        result = register.is_valid()

        if not result:
            register.email.click()
            register.email.clear()
            register.email.fill(f"{self._EMAIL}.com")

            register.mobile_phone_number.click()
            register.mobile_phone_number.clear()
            register.mobile_phone_number.fill(ten_digit_phone_number)

        # Second Submit after correction
        register.submit_form(register.submit_button)

        # Assertion Section
        register.expect_contain_text(
            selector=register.validation_table,
            text=f"{self._FIRST_NAME} {self._LAST_NAME}",
        )

        register.expect_contain_text(
            selector=register.validation_table,
            text=f"{self._EMAIL}.com",
        )

        register.expect_contain_text(
            selector=register.validation_table,
            text=f"{self._GENDER}",
        )

        register.expect_contain_text(
            selector=register.validation_table,
            text=f"{ten_digit_phone_number}",
        )

        register.expect_contain_text(
            selector=register.validation_table,
            text="04 November,2000",
        )

        register.expect_contain_text(
            selector=register.validation_table,
            text="Computer Science, English",
        )

        register.expect_contain_text(
            selector=register.validation_table,
            text=f"{self._SPORTS}, {self._READING}, {self._MUSIC}",
        )

        register.expect_contain_text(
            selector=register.validation_table,
            text=f"{self._ADDRESS}",
        )

        register.expect_contain_text(
            selector=register.validation_table,
            text=f"{self._STATE} {self._CITY}",
        )