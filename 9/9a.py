
"""
1. ukol ()
"""


with open("input.txt", "r") as myfile:
    mylist = [line[:-1] for line in myfile.readlines()]


def two_numbers(input_list: list, wanted_sum: str):
    """ Rerurn if list contains 2 numbers giving wanted_sum and what are those numbers(if true) or what was wanted_sum (if false)"""

    for a in input_list:
        b = int(wanted_sum)-int(a)
        if str(b) in input_list:
            return(True,int(a),b)
    return (False, int(wanted_sum))

def which_numbers_are_correct(input_list: list, preamble_length: int) -> bool:
    """ For each number in list (except preamble at the begining) returns tuple: (valid?, number).
        Number is valid when it is sum of some 2 numbers in preamble (25chars before number)"""


    result_list = []
    i = preamble_length+1
    for i in range(i,len(input_list)+1):
        preamble_list = input_list[slice(i-preamble_length-1,i-1)]
        result_list.append(((two_numbers(preamble_list, input_list[i-1]))[0], input_list[i-1]))
    return result_list

print(list(c[1] for c in which_numbers_are_correct(mylist,25) if c[0]==False))      # print just the not valid (false) numbers