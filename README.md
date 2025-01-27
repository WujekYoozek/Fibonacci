# Ciąg Fibonacciego
## Co to jest ciąg Fibonacciego?
### Definicja
Ciąg Fibonacciego to ciąg liczb naturalnych, który zaczyna się od 0 i 1, a każda kolejna liczba jest sumą dwóch poprzednich. Ciąg ten został opisany przez włoskiego matematyka Leonardo Fibonacciego w XII wieku.
# Obliczanie danego elementu ciągu Fibonacciego metodą rekurencyjną i iteracyjną
## Metoda Rekurencyjna
### Definicja
Rekurencja (łac. recurrere – przybiec z powrotem) – technika, w której funkcja lub metoda wywołuje samą siebie w celu rozwiązania problemu.
### Kod
```python
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
```
### Pomiary wydajności
![pomiar wydajności](https://cdn.discordapp.com/attachments/1015567218899161139/1333515354315558923/image.png?ex=67992c73&is=6797daf3&hm=82dd18c490e438de6a55a64dd8643568b96e980db55b6214334a6011da9e94a0&)

## Metoda Iteracyjna
### Definicja
Iteracja (łac. iteratio – powtarzanie) – czynność powtarzania tej samej operacji w pętli z góry określoną liczbę razy lub aż do spełnienia określonego warunku.
### Kod
```python
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
```
### Pomiary wydajności
![pomiar wydajności](https://cdn.discordapp.com/attachments/1015567218899161139/1333530247727022212/image.png?ex=67993a52&is=6797e8d2&hm=42df122cdad88b93c5d53e047ecb520718ca2c55d5f1e2eb76d70c82363a4698&)

__Pozycja 20577 (Iteracja) - 0.005s__  
__Pozycja 22 (Rekurencja) - 0.005s__
