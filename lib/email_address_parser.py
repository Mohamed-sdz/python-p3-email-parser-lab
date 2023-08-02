import re

class EmailAddressParser:

    def __init__(self, input_string):
        self.input_string = input_string

    @staticmethod
    def parse_email_address(email_string):
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        matches = re.findall(pattern, email_string)
        return matches

    def parse(self):
        email_strings = re.split(r',|\s', self.input_string)
        email_addresses = []

        for email_string in email_strings:
            matches = self.parse_email_address(email_string)
            email_addresses.extend(matches)

        # Sort the email addresses before returning
        email_addresses.sort() 
        return email_addresses