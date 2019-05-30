####### Write a program in Python to test whether two strings are anagrams.########


def anagrams(str1,str2):
    string1=list(str1.lower()) #Create a list, each element is the lower case letter of the first string
    string2=list(str2.lower()) #Create a list, each element is the lower case letter of the second string
    if len(string1)!=len(string2): # if the two string do not have the same length print error message
        print(('ERROR! {} and {} are NOT the same length').format(str1,str2))
    elif sorted(string1)==sorted(string2): #sort the elements of the two lists and check if they have the same elements
        print(('{} and {} are anagrams').format(str1,str2))
    else:
        print(('{} and {} are NOT anagrams').format(str1,str2))
    
    return


if __name__ == '__main__':
    
    anagrams('Listen','Silent') #Some examples to check if the code works well in different conditions
    anagrams('Cat','act')
    anagrams('bag','dog')
    anagrams('Good','dog')
    anagrams('thing','Night')
