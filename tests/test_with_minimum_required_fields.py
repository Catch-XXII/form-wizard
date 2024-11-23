from pages.practice_form_page import PracticeFormPage
from base.utils import generate_phone_number
from base.utils import formatted_date


class TestPracticeForm:
    def test_with_minimum_required_fields(self, browser):
        """
        1 Go to https://demoqa.com/
        2 Assert web page title == DEMOQA
        3 Click on "Forms"
        4 Click on "Practice Form"
        5 See Form loaded and Assert Title
        6 Assert form name == Student Registration Form
        7 First Name = John
        8 Submit form and check with is_valid and return back
        9 Last Name = Doe
        10 Submit form and check with is_valid and return back
        11 Gender = Male
        13 Submit form and check with is_valid and return back
        14 Mobile = 1234567890
        15 Submit form and check with is_valid and return back
        16 Click on Submit button

        Expected Result
        # See Table and make assertion for each field accordingly
        """
        ten_digit_phone_number = generate_phone_number(10)

        register = PracticeFormPage(browser)
        register.navigate_to_url(register._URL)
        register.has_title(register._TITLE)
        register.retrieve_and_click_by("Forms")
        register.retrieve_and_click_by("Practice Form")
        register.expect_contain_text("h1", register._PAGE_TITLE)
        register.expect_contain_text("h5", register._FORM_TITLE)
        register.fill_text(register.first_name, register._FIRST_NAME)

        register.submit_form(register.submit_button)
        result = register.is_valid()
        if not result:
            register.fill_text(register.last_name, register._LAST_NAME)

        register.submit_form(register.submit_button)
        result = register.is_valid()
        if not result:
            register.select_from_radio_button(register._GENDER)

        register.is_checked(register._GENDER)

        register.submit_form(register.submit_button)
        result = register.is_valid()

        if not result:
            register.fill_text(register.mobile_phone_number, ten_digit_phone_number)

        register.submit_form(register.submit_button)
        result = register.is_valid()

        if result:
            # Assertion Section
            register.expect_contain_text(
                selector=register.validation_table,
                text=f"{register._FIRST_NAME} {register._LAST_NAME}",
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
                text=formatted_date,
            )
