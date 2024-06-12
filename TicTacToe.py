import random

num = [1,2,3,4,5,6,7,8,9]
user_num = []

def main():
    print("************************\n*** Tic-Tac-Toe Game ***\n************************\n")
    print("[Computer is 'O', You Are 'X']\n")
    grid_print()

    while True:
        try: 
            user = int(input("Enter The Number Of The Square: "))
            if not list_has_integer(num):
                print("!*!*!* It's A Tie !*!*!*")
                break
            elif user in num:
                if user in user_num:
                    raise ValueError
                else:
                    user_num.append(user)
                    index = num.index(user)
                    num[index] = "X"
                    computer_choice()
                grid_print()
            if winner_check():
                break
        except ValueError:
            continue
        except KeyboardInterrupt:
            print("\nThanK You For Playing Tic-Tac-Toe\n")
            break
        

def winner_check():
    winning_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]

    for condition in winning_conditions:
        if all(num[i] == "X" for i in condition):
            print("\n****** Yee! You won ******")
            return True
        elif all(num[i] == "O" for i in condition):
            print("\n!!!!!! Oh No! Computer won !!!!!!")
            return True

    return False

    
      
        

def computer_choice():            
    available_positions = [element for element in num if isinstance(element, int)]
    if available_positions:
        index = num.index(random.choice(available_positions))
        num[index] = "O"



def list_has_integer(list):
    for element in list:
        if isinstance(element, int):
            return True
    return False




def grid_print():
    lines = "|         |         |         |"
    first_line = f"|    {num[0]}    |    {num[1]}    |    {num[2]}    |" 
    second_line = f"|    {num[3]}    |    {num[4]}    |    {num[5]}    |" 
    therd_line = f"|    {num[6]}    |    {num[7]}    |    {num[8]}    |"    
    horizontal = "-------------------------------"

    line_list = [first_line, second_line, therd_line]

    for line in line_list:
        print(horizontal)
        print(lines)          
        print(line)          
        print(lines)  
    print(horizontal)



if __name__ == "__main__":
    main()

