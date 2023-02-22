from browser import Browser


class Base_page(Browser):

    def check_url(self, expected_url):
        actual_url = self.chrome.current_url
        assert expected_url == actual_url, f'Current url : {actual_url}; expected: {expected_url}'

    def check_error_message(self, by, selector, expected_error_message):
        actual_error_message = self.chrome.find_element(by, selector).text
        assert expected_error_message == actual_error_message, f"fError: Incorrect error message. Expected: {expected_error_message}, Actual: {actual_error_message}"