def checkio(str_number, radix):

    import string

    #creating a dictionary with letters as keys mapping to value from 10 onward

    letter_dic = {c : i for i, c in enumerate(string.ascii_uppercase, 10)}

    #adding the numerals to this dictionary for digits from 0 to 9

    numerals = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9}
    letter_dic.update(numerals)

    #initializing my decimal variable
    decimal = 0


    for i in range(len(str_number)):

        #Using working number variable to reverse order of digits to operate on

        workingnumber = str_number[abs(i - (len(str_number))) - 1]

        #Condition to make sure we don't run operation if number is outside scope of radix

        if letter_dic[workingnumber] >= radix:
            return -1

        else:

            decimal = decimal + (letter_dic[workingnumber] * (radix ** i))


    return decimal


print(checkio("AF", 16))
print(checkio("101", 2))
print(checkio("Z", 36)
)
