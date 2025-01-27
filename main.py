import time

def fibonacciSequenceRecursion(element):
    if element==0:
        return 0
    elif element==1:
        return 1
    else:
        outcome=fibonacciSequenceRecursion(element-1)+fibonacciSequenceRecursion(element-2)
        return outcome
if __name__ == '__main__':
    index=int(input("Choose an element of the sequence: "))
    start_time = time.time()
    print(fibonacciSequenceRecursion(index))
    end_time = time.time()
    print(f"Duration: {end_time - start_time}")
