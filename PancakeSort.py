from stapel_class import Stapel
from itertools import permutations
from typing import Iterator
from time import time
from math import inf

def get_position_to_switch(stack: list[int], current_size: int) -> list[int]:
    positions = set()
    ############################################################
    ## Bewegt vorderstes Element der Liste zu seinem Partener ##
    ##                  (also 2 zu 1 oder 3)                  ##    
    if stack[0] + 1 in stack:
        index = stack.index(stack[0] + 1) - 1
        positions.add(index)
    if stack[0] -1 in stack:
        index = stack.index(stack[0] - 1) - 1
        positions.add(index)
    ##############################################################################
    ## wenn das vorderste Element das größte ist, wird es nach hinten getauscht ##
    if stack[0] == current_size:
        positions.add(current_size - 1)
    ################################
    ## entfernt größtest Element ##
    index_highest = stack.index(current_size)
    positions.add(index_highest)
    ########################################
    ## tauscht größtes Element nach vorne ##
    positions.add(index_highest + 1)
    ################################################
    ## macht das selbe für das 2. höchste Element ##
    index_second_highest = current_size - 1
    if current_size > 1:
        index_second_highest = stack.index(current_size - 1)
        go_on = True
        index_to_change = current_size - 1
        if index_second_highest == current_size - 1:
            go_on = False
            if current_size > 2:
                index_to_change -= 1
                for i in range(current_size - 2, 1, -1):
                    index_next_highest = stack.index(i)
                    if index_next_highest != index_second_highest - 1:
                        go_on = True
                        index_second_highest = index_next_highest
                        break
                    index_to_change -= 1
        if go_on:
            positions.add(index_second_highest + 1)
            if index_second_highest == 0:
                positions.add(index_to_change)
            positions.add(index_second_highest)
    ##############################################
    ## entfernt vorderstes oder zweitvorderstes ##
    positions.add(0)
    positions.add(1)
    return positions

#################################################################
## gibt die Länge der Liste zurück, welche noch unsortiert ist ##
##              (also [1, 3, 2, 4, 5] -> 3)                    ##
def shorten_list(stack: list[int], current_size: int) -> int:
    new_size = current_size
    for i in range(current_size - 1, -1, -1):
        if stack[i] == i + 1:
            new_size -= 1
        else:
            break
    return new_size

######################################################################
## berechnet die Liste neu, wenn ein Element entfernt wurde, sodass ##
##   die Liste immer aus den Zahlen 1 bis Länge der Liste besteht   ##
##              (also [5, 4, 2, 1] -> [4, 3, 2, 1])                 ##
def recalculate_list(stack: list[int], current_size: int, number_removed: int):
    for i in range(number_removed + 1, current_size + 2):
        if i in stack:
            stack[stack.index(i)] -= 1

#########################################################################
## wendet den Stapel an gegebener Stelle, gibt den neuen Stapel zurück ##
def turn(stack: list[int], position: int) -> list[int]:
    if position == 0:
        return stack[1:]
    return stack[position - 1::-1] + stack[position + 1:]

######################################################################
## kreiert einen Generator, der beim x-ten Aufruf von next(), wobei ##
## x für die kürzeste Anzahl an Wendeoperationen für die gegebene   ##
##      Liste steht, eine Liste mit Wendeoperationen zurückgibt     ##
def find_least_turns(stack: list[int], current_size: int, my_switch: list[int]) -> Iterator[list[int]]:
    current_size = shorten_list(stack, current_size)
    if current_size == 0:
        yield my_switch
    else:
        yield [-1]
    my_next = []
    for position in get_position_to_switch(stack, current_size):
        new_stack = turn(stack, position)
        recalculate_list(new_stack, current_size, stack[position])
        my_next += [find_least_turns(new_stack, current_size - 1, [position])]
    next_return = []
    while next_return == []:
        for nexts in my_next:
            res = next(nexts)
            if res != [-1]:
                next_return = res + my_switch
                break
        else:
            yield [-1]
    yield next_return

######################################################
## erschafft einen Generator, der nach und nach die ##
##    eingelesenen gegebenen Textfiles ausspuckt    ##
def read_text_files(max: int) -> Iterator[tuple[list[int], int]]:
    for i in range(max + 1):
        with open("pancake" + str(i) + ".txt") as file:
            stapel = []
            size = int(next(file).replace("\n", ""))
            for elm in file:
                stapel += [int(elm.replace("\n", ""))]
            yield stapel, size

############################################################
## wendet next() x-mal auf den find_least_turns Generator ##
##        an und gibt das richtige Ergebnis zurück        ##
def get_least_turns(stack: list[int], current_size: int) -> list[int]:
    gen = find_least_turns(stack, current_size, [])
    res = [-1]
    while res == [-1]:
        res = next(gen)
    return list(reversed(res))

###################################################
## errechnet die PWUE-Zahl der Liste der Länge n ##
def find_PWUE_zahl(n: int) -> int:
    if n == 0:
        return 0
    elif n == 3:
        return [2, 3, 1], len(get_least_turns([2, 3, 1], 3))
    my_list = [0 for i in range(n)]
    my_list[-1] = 1
    current_number = n
    for i in range(n - 3, -1, -2):
        my_list[i] = current_number
        current_number -= 1
    while 0 in my_list:
        my_list[n - list(reversed(my_list)).index(0) - 1] = current_number
        current_number -= 1
        if 0 in my_list:
            my_list[my_list.index(0)] = current_number
            current_number -= 1
    return my_list, len(get_least_turns(my_list, n))

###########################################################################################
## testet den Sortieralgorithmus, also vergleicht ihn mit dem, der auf jeden Fall stimmt ##
def test_algorithm(min: int, max: int):
    for i in range(min, max):
        n = i
        s = Stapel(n, n // 2 + 1)
        stapel = [i for i in range(1, n + 1)]
        counter = 0
        not_correct = 0
        for elm in permutations(stapel):
            try:
                counter += 1
                assert s.try_out(list(elm)) == len(get_least_turns(list(elm), n))
            except AssertionError:
                not_correct += 1
        print(n, ":", (not_correct / counter) * 100, "%")

    
if __name__ == "__main__":
    ###################################
    ## Löst alle gegebenen Beispiele ##
    print("______________________________________________________")
    print("a)")
    files = read_text_files(7)
    for file in files:
        print(file)
        res = get_least_turns(file[0], file[1])
        print(res, len(res))
        print("______________")

    #######################################
    ## Berechnet PWUE Zahlen von 0 bis n ##
    print("______________________________________________________")
    print("b)")
    a = input("How many PWUE Numbers do you want to calculate [recommended 13]: ")
    n = 13
    if a != "":
        n = int(a)
    for i in range(0, n + 1):
        print(i, ":", find_PWUE_zahl(i))

    ############################
    ## testet den algorithmus ##
    print("______________________________________________________")
    print("c) (own)")
    a = input("Do you want to test the algoritm? [y/n]: ")
    if a == "y":
        test_algorithm(1, 8)
        a = input("Do you want to continue testing? [y/n]: ")
        if a == "y":
            print("This process runs pretty much infinite. To stop press: [Ctrl-C]")
            test_algorithm(8, 100)