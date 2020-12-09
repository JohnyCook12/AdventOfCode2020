
"""
1. ukol (funkcni)

"""

# read input:

with open("input.txt", "r") as myfile:

    mylist = [line[:-1] for line in myfile.readlines()]


    # roztřídit do listu listů (listu skupin) podle řádků a mezer mezi řádky

    mylist2 = []
    temp_list = []
    for line in mylist:
        if line == "":
            mylist2.append(temp_list)
            temp_list = []
        else:
            temp_list.append(line)


    # zjistit v rámci skupiny, jaká obsahuje písmenka (bez duplicit)

    all_unique_answers = []
    group_yes_numbers = []

    for skupina in mylist2:
        unique_answers_in_group = []
        for one_man_answer in skupina:
            unique_answers_in_group.extend(one_man_answer)
        unique_answers_in_group = list(set(unique_answers_in_group))
        all_unique_answers.append(unique_answers_in_group)
        group_yes_numbers.append(len(unique_answers_in_group))

    # print(mylist2)
    # print(all_unique_answers)
    # print(group_yes_numbers)
    print('Soucet poctu otazek na ktere nekdo ve skupine odpovedel ano: ',sum(group_yes_numbers))

    """2"""

    all_yes_total = []
    all_yes_total_number = []

    for skupina in mylist2:
        all_yes_in_group = []
        all_yes_answers = []
        all_yes_no_duplicities = []

        for one_man_answer in skupina:
            all_yes_in_group.extend(one_man_answer)
        for i in all_yes_in_group:
            if all_yes_in_group.count(i) >= len(skupina):
                all_yes_answers.append(i)
        all_yes_no_duplicities = list(set(all_yes_answers))
        all_yes_total.append(all_yes_no_duplicities)
        all_yes_total_number.append((len(all_yes_no_duplicities)))

    # print(all_yes_total)
    # print(all_yes_total_number)
    print('Součet otázek na které odpověděli ano všichni v dané skupině: ',sum(all_yes_total_number))

