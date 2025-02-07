def check_base_list(highest_base, binary_looking_num):

    for base in range(highest_base, 1, -1):
        if is_prime(convert_to_base_ten(base, binary_looking_num)):
            continue
        else:
            return False

    return True



def convert_to_base_ten(orig_base, num):

    num_str = str(num)
    i = int(len(num_str) - 1)
    count = 0

    for char in num_str:

        count += int(char) * (int(orig_base)**i)
        i -= 1

    return count


def is_prime(num):

    if num in [0,1]:
        return False

    if num in [2,3]:
        return True

    for check in range(2, int(num ** 0.5) + 1):

        if int(num) % check == 0:
            return False

    return True


def find_highest_base(bin_num):

    check = 3

    while True:
        if check_base_list(check, bin_num):
            check += 1

        else:
            return check - 1


def show_only_first_instance(max_num):

    int_list = [0,1,2,3,4,5,6,7,8,9,10]

    for num in range(int(max_num) + 1):

        if is_prime(num) and find_highest_base(bin(num)[2:]) in int_list:

            print(f"{num} | {bin(num)[2:]} | {find_highest_base(bin(num)[2:])}")
            int_list.remove(find_highest_base(bin(num)[2:]))


def show_everything(max_num):

    numlist = [0,0,0,0,0,0,0,0,0,0,0]

    numDict = {}

    for val in range(2,11):
        numDict[val] = []

    for num in range(int(max_num) + 1):

        if is_prime(num):

            print(f"{num} | {bin(num)[2:]} | {find_highest_base(bin(num)[2:])}")
            numlist[find_highest_base(bin(num)[2:])] += 1
            numDict[find_highest_base(bin(num)[2:])] += [num]

    for x in range(2,len(numlist)):
        print(f"\nCount of primes with max base = {x}: {numlist[x]}")

    while True:

        user_input = input("Would you like to see information about a base or a prime number? (Enter 'base' or 'prime', or enter 'q' to quit).\n> ")

        if user_input.lower() == "q":
            break
                
        if user_input.lower() == "base":

            while True:
                val = input("\nPlease enter the base you would like to observe, and I will print all corresponding primes.\nYou may also enter 'q' to quit\n> ")

                if val == "q":
                    break

                try: base = int(val)
                except:
                    print("Try again.")
                    continue

                for prime in numDict[base]:
                    print(prime)

        if user_input.lower() == "prime":

            while True:

                string = input("Please enter a prime number to see which was its maximum base.\nYou may also enter 'q' to quit.\n> ")

                if string == "q":
                    break

                try: prime = int(string)
                except:
                    print("Try again. This is not an integer.")
                    continue

                if is_prime(prime):

                    print(f"{prime} converted to binary is: {bin(prime)[2:]}")

                    print(f"The highest base for which {bin(prime)[2:]} is prime is: {find_highest_base(bin(prime)[2:])}")

                    for i in range(2, find_highest_base(bin(prime)[2:])+1):

                        print(f"{bin(prime)[2:]} in base {i} = {convert_to_base_ten(i, bin(prime)[2:])} in base 10")

                else:

                    print(f"{prime} is not a prime number. Try again.")

        else:
            print("Try again.")

assert convert_to_base_ten(2, 10) == 2
assert convert_to_base_ten(2, 101011) == 43
assert convert_to_base_ten(4, 1001) == 65
assert convert_to_base_ten(10, 546) == 546

assert is_prime(2) == True
assert is_prime(1) == False
assert is_prime(23) == True
assert is_prime(91) == False
assert is_prime(25252525) == False

assert check_base_list(3, 10) == True
assert check_base_list(4, 10) == False

while True:
    
    maximum = input("Please enter a max nummber:\n> ")

    show_everything(maximum)

    

    
