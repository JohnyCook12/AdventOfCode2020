
"""
2. ukol (funkcni)
"""

# read input:

with open("input.txt", "r") as myfile:
    mylist = [line[:-1] for line in myfile.readlines()]
    accumulator = 0

    mylist2 = []
    for i in mylist:
        mylist2.append(i.split(" "))


    ### ENUMERATE SE NEHODÍ, JDEME NA TO WHILE LOOPEM ###

    def change_command(input_list: list, position: int) -> list:
        """ změní na dané pozici nop na jmp a jmp na nop """

        input_list_tup = [tuple(i) for i in input_list]
        output_list = [list(i) for i in input_list_tup]

        if output_list[position][0] == 'jmp':
            output_list[position][0] = 'nop'
            #print(position + 1, input_list[position], 'jmp -> nop')
        elif output_list[position][0] == 'nop':
            output_list[position][0] = 'jmp'
            #print(position + 1, input_list[position], 'upraveno:  nop -> jmp')

        return output_list
    def start_device(input_list) -> int:
        """
        Projede program a vrátí jak skončil a kolik byl zrovna accumulator
        :return:
        ==1: INFINITE LOOP
        ==2: FINISHED CORRECTLY BY LAST COMMAND (675)
        ==3: FINISHED CORRECTLY BY JUMPING OUT
        """
        # limit_counter = 0       #smazat
        accumulator = 0
        finish_code = 0
        viewed_commands = []
        x = 0

        while x < len(input_list):         ### WORKING LOOP ###
            if x == 675:
                finish_code = 2
                break
            else:
                if x in viewed_commands:
                    finish_code = 1
                    break
                else:
                    if input_list[x][0] == 'acc':
                        accumulator += int(input_list[x][1])
                        # print(x + 1, input_list[x])
                        viewed_commands.append(x)
                        x += 1
                        #limit_counter += 1              # smazat
                    elif input_list[x][0] == 'jmp':
                        finish_code = 3                  # defaultně je 3, tj. jumping out.
                        # print(x + 1, input_list[x])
                        viewed_commands.append(x)
                        x += int(input_list[x][1])
                        #limit_counter += 1              # smazat
                    elif input_list[x][0] == 'nop':
                        # print(x + 1, input_list[x])
                        viewed_commands.append(x)
                        x += 1
                        #limit_counter += 1              # smazat


        return (finish_code, accumulator)


    # projedeme celý "program" a když vidí NOP / JMP zkusí ho změnit na ten druhej a zapíše si jak program skončil (+akumulátor) pro ACC zapíše jen 'A'.
    # Je-li výsledek 2 nebo 3 (tj. skončil správně), zapíše si index změněného příkazu do extra listu
    run_result_list = []
    index_of_correct_finish = []
    result = 0
    a = 0

    while a < len(mylist2):
        if mylist2[a][0]=='acc':
            run_result_list.append('A')
            a += 1
        elif mylist2[a][0]=='jmp' or mylist2[a][0]=='nop':
            current_list = change_command(mylist2,a)
            result = start_device(current_list)
            run_result_list.append(result[0])
            if result[0] == 2 or result[0] == 3:
                index_of_correct_finish.append(a)
                index_of_correct_finish.append(result)



            a += 1

    print(run_result_list)
    print(index_of_correct_finish)


    # if result == 1: print('INFINITE LOOP')
    # if result == 2: print('LAST COMMAND')
    # if result == 3: print('JUMP OUT')
