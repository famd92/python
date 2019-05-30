###Write a program that prints the numbers from 1 to 100. But for multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz" ####


def fizzbuzz(number):
    if (number%3 ==0 and number%5 ==0):
        output = 'Fizz Buzz'
    elif (number%3 ==0):
        output = 'Fizz'
    elif (number%5 ==0):
        output ='Buzz'
    else:
        output = number
    return output

if __name__ == '__main__':
    for i in range(1,101):
        print(fizzbuzz(i))
