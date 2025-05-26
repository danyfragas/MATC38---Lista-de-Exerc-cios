import random

#Questão 2

def insertionSort(arr):
    gcbrDeslocamentos = 0

    for gcbrI in range(1, len(arr)):
        gcbrAtual = arr[gcbrI]
        gcbrJ = gcbrI - 1

        while gcbrJ >= 0 and arr[gcbrJ] > gcbrAtual:
            arr[gcbrJ + 1] = arr[gcbrJ]
            gcbrDeslocamentos += 1
            gcbrJ -= 1

        arr[gcbrJ + 1] = gcbrAtual
        
    return gcbrDeslocamentos

def generate_random_array(size, min_val=1, max_val=100):
    return [random.randint(min_val, max_val) for _ in range(size)]

def main():
    arr = generate_random_array(10)
    print("Array de entrada:", arr)
    result = insertionSort(arr)
    print("Deslocamentos realizados:", result)

if __name__ == '__main__':
    main()