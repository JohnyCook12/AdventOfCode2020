
"""1. ukol (funkční)
- přečte input (= vzorec lesa)
- zadáš startovní pozici (0,0)  a slidování (slide_right, slide_down)

"""


# read input:

with open("input.txt", "r") as myfile:
    mylist = [line[:-1] for line in myfile.readlines()]
trees = 0
start_line = 0
current_position = 0
line_length = len(mylist[0])

slide_right = 3
slide_down = 1

step = slide_down

for current_line in mylist[::step]:                         # projede celý list, velikost kroku je "step"

    result_line = list(current_line)                        # pro změnu znaku převede nejdřív string na list a pak zpět na string

    if result_line[current_position] == '.':                # v dráze sjezdu nahradí .->O a #->X
        result_line[current_position] = 'O'
    elif result_line[current_position] == '#':
        result_line[current_position] = 'X'
        trees += 1                                          # počítá sražené stromy

    result_line = "".join(result_line)                      #
    print(result_line,'    ',current_line)                  # zobrazí les s dráhou a původní les bez dráhy

    if current_position > (30-slide_right):                 # warpování, když vyjede vpravo z obrazu
        current_position -= (31-slide_right)
    else:
        current_position += slide_right


print("\n",f"Dolů o {slide_down},vpravo o {slide_right}, potkáno stromů: {trees}")

