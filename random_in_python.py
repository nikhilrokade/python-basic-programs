import random
import sys

take_lists = random.random()

number_as_string = str(take_lists)
char_count = len(number_as_string)

print(f"The random number is: {take_lists}")
print(f"The character length of this number is : {char_count} \n")

def check(ran_list: int, ran_tuple:int) -> any:
    check_inp = ran_list
    check_inp = (random.randint(5,7))

    print(check_inp)
    check_len_lst = len(str(check_inp)) #length of the string comig from random
    print("checking the list: " , check_len_lst)

    ran_tuple = (random.randint(1,2))
    check_len_tup = len(str(ran_tuple))
    print(check_len_tup)

    print("\n")

check(10,5)

def ran(ran_list, ran_tuple):
    ran_list = (random.random())
    take_ran_list = [ran_list]
    if isinstance(ran_list, list):
        print("It is a list")
    else:
        print("Please enter a list")
    print(take_ran_list)
    check_len_lst = len(str(ran_list)) #length of the string comig from random
    print("checking the list: " , check_len_lst)

    ran_tuple = (random.random())
    check_len_tup = len(str(ran_tuple))
    print(check_len_tup)

    print("\n")

ran([],())

def useRange():
    ''' Sequence Type '''
    furniture_String = 'Tables, Chairs, Cupboards'
    sport_list = ['Table Tennis', 'Snookers', 'Carrom']
    drink_tuple = ('chocolate','dryfruit', 'soups')

    print(furniture_String)
    print(sport_list)
    print(drink_tuple)

    ''' Range '''
    number = 10
    #range(start,stop,step)
    for i in range(1, number):
        print(i, end=" ")

#uses random library
def useRandom():
    '''Random Library'''
    rd_furniture_String = 'Tables, Chairs, Cupboards'
    rd_sport_list = ['Table Tennis', 'Snookers', 'Carrom']
    rd_drink_tuple = ('chocolate','dryfruit', 'soups')

    print(random.choice(rd_furniture_String))
    print(random.choice(rd_sport_list))
    print(random.choice(rd_drink_tuple))

    
#calling function/method
useRange()
print("\n")
print("================================================================")
useRandom()