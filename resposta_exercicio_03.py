import random

#Questão 3

from bisect import insort, bisect_left

def activityNotifications(expenditure, d):
    window = sorted(expenditure[:d])
    count = 0

    for i in range(d, len(expenditure)):
        if d % 2 == 1:
            mediana = window[d // 2]
        else:
            mediana = (window[d // 2] + window[d // 2 - 1]) / 2

        if expenditure[i] >= 2 * mediana:
            count += 1

        antigo = expenditure[i - d]
        window.pop(bisect_left(window, antigo))
        insort(window, expenditure[i])

    return count

def gerar_dados(n, max_val=200):
    return [random.randint(0, max_val) for _ in range(n)]

def main():
    n, d = 10, 5
    gastos = gerar_dados(n)

    print(f"n = {n}, d = {d}")
    print("Gastos:", gastos)

    resultado = activityNotifications(gastos, d)
    print("Notificações:", resultado)

if __name__ == '__main__':
    main()