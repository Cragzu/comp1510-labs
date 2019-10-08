"""
Module to demonstrate functions and create a D&D character.
"""
from lab05 import choose_inventory
from lab05 import create_character
from lab05 import print_character


def main():
    """
    Drive the program.

    Tests the functions created in this module.
    """

    print('Welcome to the D&D Character Generator!\n')

    name_length = int(input('How many syllables should your character\'s name have?: '))
    character_info = create_character(name_length)
    print_character(character_info)

    shop_items = ['Sword of Sanctimony', 'Potion of Python', 'Daggers of Deception', 'Staff of Serenity',
                  'Juggling Balls of JavaScript', 'Detonator of Divide-by-Zero', 'Gloves of Genius',
                  'Map of Misdirection', 'Crossbow of Courage', 'Charm of Chris\' Approval', 'Cloak of Confusion',
                  'Takashi\'s Donut Box', 'Bottle of Binary', 'Axe of Asking Questions']

    print('\nToday there are', len(shop_items), 'shop items available. They are:')
    for i in shop_items:
        print(i)

    item_number = int(input('\nHow many items would you like to purchase?: '))
    item_selection = choose_inventory(shop_items, item_number)

    print('You received these items:')
    for i in item_selection:
        print(i)

    character_info.append(item_selection)
    print('\n~~~ Your final character! ~~~')
    print_character(character_info)


if __name__ == "__main__":
    main()
