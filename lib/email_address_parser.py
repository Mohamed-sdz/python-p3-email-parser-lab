# your code goes here!
import re

class EmailAddressParser:
    def __init__(self, input_string):
        self.input_string = input_string

    @staticmethod
    def parse_email_address(email_string):
        # Regular expression to match email addresses
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        matches = re.findall(pattern, email_string)
        return matches

    def parse(self):
        # Split input string by commas and spaces
        email_strings = re.split(r',|\s', self.input_string)
        # Parse each string to extract email addresses
        email_addresses = []
        for email_string in email_strings:
            matches = self.parse_email_address(email_string)
            email_addresses.extend(matches)
        # Remove duplicates and return the final list of email addresses
        return list(set(email_addresses))