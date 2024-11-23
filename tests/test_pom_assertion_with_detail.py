from pages.practice_form_page import PracticeFormPage
from base.utils import generate_phone_number
import os


class TestPracticeForm:
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
        register = PracticeFormPage(browser)
        register.navigate_to_url(register._URL)
        register.has_title(register._TITLE)
        register.retrieve_and_click_by("Forms")
        register.retrieve_and_click_by("Practice Form")
        register.expect_contain_text("h1", register._PAGE_TITLE)
        register.expect_contain_text("h5", register._FORM_TITLE)
        register.first_name.fill(register._FIRST_NAME)
        register.last_name.fill(register._LAST_NAME)
        register.email.fill(register._EMAIL)
        register.select_from_radio_button(register._GENDER)
        register.mobile_phone_number.fill(generate_phone_number(9))
        register.fill_calendar(register.dob, register._YEAR, register._DATE_OF_BIRTH)

        # Subjects
        register.multiple_selection(
            register.subjects, register._SUBJECT_1, register._SUBJECT_2
        )

        # Hobbies
        register.retrieve_and_click_by(register._SPORTS)
        register.retrieve_and_click_by(register._READING)
        register.retrieve_and_click_by(register._MUSIC)

        # Upload Picture
        project_directory = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(project_directory, register._FILE_NAME)
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        register.upload_file("input[type='file']", file_path)

        # Address
        register.fill_text(register.address, register._ADDRESS)

        # State and City
        register.drop_down_selection(register.state, register._STATE)
        register.drop_down_selection(register.city, register._CITY)

        # Submit
        register.submit_form(register.submit_button)
        result = register.is_valid()

        if not result:
            register.email.click()
            register.email.clear()
            register.email.fill(f"{register._EMAIL}.com")

            register.mobile_phone_number.click()
            register.mobile_phone_number.clear()
            register.mobile_phone_number.fill(ten_digit_phone_number)

        # Second Submit after correction
        register.submit_form(register.submit_button)

        # Assertion Section
        register.expect_contain_text(
            selector=register.validation_table,
            text=f"{register._FIRST_NAME} {register._LAST_NAME}",
        )

        register.expect_contain_text(
            selector=register.validation_table,
            text=f"{register._EMAIL}.com",
        )

        register.expect_contain_text(
            selector=register.validation_table,
            text=f"{register._GENDER}",
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
            text=f"{register._SPORTS}, {register._READING}, {register._MUSIC}",
        )
        register.expect_contain_text(
            selector=register.validation_table, text="cuneyd.jpg"
        )

        register.expect_contain_text(
            selector=register.validation_table,
            text=f"{register._ADDRESS}",
        )
        register.expect_contain_text(
            selector=register.validation_table,
            text=f"{register._STATE} {register._CITY}",
        )
