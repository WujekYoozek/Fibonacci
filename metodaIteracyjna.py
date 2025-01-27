import time

def fibonacciSequenceIterative(index):
    if index==1:
        return 0
    elif index==2:
        return 1
    else:
        number1 = 0
        number2 = 1
        number3 = 0
        for i in range(1, index):
		    number3 = number1 + number2
            number1 = number2
            number2 = number3
        return number3

if __name__ == '__main__':
    index=int(input("Choose an element of the sequence: "))
    start_time = time.time()
    print(fibonacciSequenceIterative(index))
    end_time = time.time()
    print(f"Duration: {end_time - start_time}")
