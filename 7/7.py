
"""
1. ukol (funkcni)
"""

import re

# read input:

with open("input.txt", "r") as myfile:
    mylist = [line[:-1] for line in myfile.readlines()]


    def extract_info(vstup: str) -> list:
        """
        Odstraní zbytečná slova - ' contain bags ', ' bag, ', ' bags, ', ' bag.', ' bags.' a sloučí info o každé tašce.
        RESULT: list, kde první člen je typ tašky a zbytek její obsah.
        """

        final_list = []
        numbers = '0123456789'

        final_list.append(vstup[:vstup.find(' bags contain ')])
        rest = (vstup[(vstup.find(' bags contain ') + len(' bags contain ')):])
        rest2 = rest.split(' ')
        rest3 = []
        index = 1
        for i in rest2:
            if (index % 4 != 0):
                rest3.append(i)
                index += 1
            else:
                index = 1
        # rest 3 je list obsahu bez všech bagů

        final_content = []
        temp_content = []
        content_index = 1
        for x in rest3:
            if content_index % 3 == 0:
                temp_content.append(x)
                final_content.append((' ').join(temp_content))
                temp_content = []
                content_index = 1
            else:
                temp_content.append(x)
                content_index += 1

        return (final_list + final_content)


    ### TADY ZAČÍNÁ KÓD ###


    bag_list = []               # první člen každého listu je obsahující taška, ostatní jsou obsah
    for bag_line in mylist:
        # bag_list.append(bag_line.split(' '))
        bag_list.append(extract_info(bag_line))


    def obsah_tasky(taska: str) -> list:        # ze jména tašky vypíše její obsah
        obsah = []
        for bag in bag_list:
            if bag[0] == taska:
                for i in range(len(bag)-1):
                    obsah.append(bag[i+1])
        return obsah
    print('')


    ### ŘEŠENÍ ###


    def find_bags_including_bag(vstup: str) -> list:
        """ vrátí list tašek co přímo obsahují vstupní tašku"""

        including_bags = []
        for bag in bag_list:
            for i in obsah_tasky(bag[0]):
                if i[2:] == vstup:
                    including_bags.append(bag[0])
        return including_bags


    level_1 = find_bags_including_bag('shiny gold')                         # 1. LEVEL - obsahuje přímo shiny_gold bag
    print(level_1)
    print('Level_1 - počet: ',len(level_1))
    

    # Následující kód je nahrazen (a zopakován) FOR cyklem níže.
    # 2 - 11 level (v dalších už nejsou tašky).
    # pomocí EXEC příkazu se mění čísla levelů.
    """
    level_2 = []                                                            # obsahuje NEpřímo shiny_gold bag (obsahuje tašky z předchozích levelů)
    for bag in level_1:
        for i in find_bags_including_bag(bag):
            level_2.append(i)
    
    print(level_2)
    print('Level_2 - počet: ',len(level_2))
    """

    for x in range(2, 11):
        exec(f'level_{x} = []\nfor bag in level_{x - 1}:\n    for i in find_bags_including_bag(bag):\n        level_{x}.append(i)')
        exec(f"print(level_{x})\nprint('Level_{x} - počet: ',len(level_{x}))")


    # finální sloučení listů ze všech levelů dohromady, odstranění duplicit a určení počtu položek.

    final_bags_list = ['dotted lavender', 'vibrant red', 'posh tan', 'vibrant white', 'wavy maroon']    # LEVEL1
    for x in range(2,11):
        exec(f'final_bags_list += level_{x}')                       # sloučíme do final_bags_list

    print('')
    print(final_bags_list)
    print('Počet tašek ve výsledném listu: ', len(list(set(final_bags_list))))





    """ ######## 2 úkol ######## """

    print("heyc")
