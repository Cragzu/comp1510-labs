"""Module containing regex code for practice."""
import re


def validate_email(string: str) -> str:
    """
    Validate an email.

    For an email to be valid:
        - the username is 1+ characters, can be anything
        - there is an @ after the username
        - the domain name is 1+ characters, only letters and numbers
        - the top-level domain is a . followed by 2-4 characters

    :param string: str, the string to be validated
    :return: str, the result of whether or not string is valid
    """
    match = re.compile(r'''
        (\w+@)  # username and separator
        ([a-zA-Z0-9]+)  # domain name
        ([.]\w{2,4})  # top-level domain (such as .com)
        ''', re.VERBOSE)

    match_object = match.search(string)
    if match_object:
        return 'That was valid! The email is: ' + match_object.group()
    else:
        return 'No email found.'


def nakamoto(name: str) -> str:
    """
    Validate a name with the surname Nakamoto.

    For the name to be valid:
        - the first name must be only letters, starting with a capital letter
        - there should be a space between first and last names
        - the last name should be Nakamoto

    :param name: str, the name to be validated
    :return: str, a message saying whether or not the given name is valid
    """
    match = re.compile(r'[A-Z][a-z]+\s(Nakamoto)')

    match_object = match.search(name)
    if match_object:
        return 'You are a valid member of the Nakamoto family, ' + match_object.group()
    else:
        return 'That is no family member of ours!'



def main():
    """
    Drive the program.
    """

    # Email validation
    # print(validate_email('My email is apple@abc.com'))
    # print(validate_email('My email is aaaaaaaaa'))

    # Nakamoto name validation
    print(nakamoto('My name is Angel Nakamoto'))
    print(nakamoto('ann Nakamoto'))


if __name__ == "__main__":
    main()