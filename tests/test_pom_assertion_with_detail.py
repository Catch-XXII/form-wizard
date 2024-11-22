from utilities.phone_number_generator import generate_phone_number
from pages.practice_form_page import PracticeFormPage
from tests.base_test import TestBasePage
import os

class TestPracticeForm(TestBasePage):
    def test_assert_with_detail_pom(self, browser):
        """
        1 Go to https://demoqa.com/
        2 Assert web page title == DEMOQA
        3 Click on "Forms"
        4 Click on "Practice Form"
        5 See Form loaded and Assert Title
        6 Assert form name == Student Registration Form
        7 Fill Name fields
        8 First Name = John Last Name = Doe
        9 Email = b@b
        10 Gender = Male
        11 Mobile = 123456789
        12 Date of Birth = Choose Saturday, November 4th 2000
        13 Subjects = Computer Science, English
        14 Hobbies = Select all options
        15 Picture = Upload local picture
        16 Current Address = Jonquil, Grandchild Center, Big Stream Avenue Shishli/İstanbul
        17 State = Haryana
        18 City = Panipat
        19 Click on Submit button
            This will give you a validation error go back and fill missing fields
            Assert document.querySelector("#userForm").checkValidity() == False
            if not result:
        20 email address with .com
        21 10 digit mobile phone number
        22 Again Submit
            See Table and make assertion for every field
        """
        # This variable will be used later on for assertion
        ten_digit_phone_number = generate_phone_number(10)
        context = browser.new_context(
            viewport={"width": 1920, "height": 1200}
        )
        page = context.new_page()
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
        register.multiple_selection(
            register.subjects, self._SUBJECT_1, self._SUBJECT_2
        )
        register.retrieve_and_click_by(self._SPORTS)
        register.retrieve_and_click_by(self._READING)
        register.retrieve_and_click_by(self._MUSIC)

        project_directory = os.getcwd()
        file_path = os.path.join(project_directory, "tests", "cuneyd.jpg")
        register.upload_file("input[type='file']", file_path)

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
        register.expect_contain_text(selector=register.validation_table, text="cuneyd.jpg")

        register.expect_contain_text(
            selector=register.validation_table,
            text=f"{self._ADDRESS}",
        )
        register.expect_contain_text(
            selector=register.validation_table,
            text=f"{self._STATE} {self._CITY}",
        )
