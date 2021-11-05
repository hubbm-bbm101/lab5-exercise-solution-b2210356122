def avg_number(N):
    avg = N/2 + 1
    return avg


def sum_number(N):
    sum = ((N+1)/2) ** 2
    return sum


number = int(input("enter number (>0): "))
if number % 2 == 0:
    result = avg_number(number)
    print("the average of even numbers 1 to " + "N is: " + str(result))
elif number % 2 == 1:
    result = sum_number(number)
    print("the sum of odd numbers 1 to " + "N is: " + str(result))