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


def sentence(string: str) -> str:
    """
    Validate a sentence comprised of specific words.

    The sentence is case-insensitive. For it to be valid:
        - the first word is Alice, Bob, or Carol
        - the second word is eats, pets, or throws
        - the third word is apples, cats, or baseballs
        - there is a period . at the end

    :param string: str, the sentence to be validated
    :return: str, a message saying whether or not the given sentence is valid
    """
    match = re.compile(r'''
        (Alice|Bob|Carol)(\s)  # first word and space after
        (eats|pets|throws)(\s)  # second word and space after
        (apples|cats|baseballs)(\.)  # last word and period
        ''', re.IGNORECASE | re.VERBOSE)

    match_object = match.search(string)
    if match_object:
        return 'A sentence was found: ' + match_object.group()
    else:
        return 'No valid sentences were found!'




def main():
    """
    Drive the program.
    """

    # Email validation
    # print(validate_email('My email is apple@abc.com'))
    # print(validate_email('My email is aaaaaaaaa'))

    # Nakamoto name validation
    # print(nakamoto('My name is Angel Nakamoto'))
    # print(nakamoto('ann Nakamoto'))

    # 3-word sentence validation
    print(sentence('The sentence is ALICE EATS APPLES.'))
    print(sentence('The sentence is ALICE EATS APPLE.'))


if __name__ == "__main__":
    main()
