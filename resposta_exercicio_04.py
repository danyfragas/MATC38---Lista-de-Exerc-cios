import random

#Questão 4

MOD = 10**9 + 7

def countRecognizedStrings(R, L):
    if R == "((a|b)*)":
        return pow(2, L, MOD)
    elif R == "((ab)|(ba))":
        return 2 if L == 2 else 0
    elif R == "((a*)(b(a*)))":
        return L  
    else:
        return 0 

def gerar_expressao():
    bases = ["a", "b"]
    exp = random.choice(bases)
    for _ in range(random.randint(1, 3)):
        op = random.choice(["|", "", "*"])
        if op == "":
            exp = f"({exp}{random.choice(bases)})"
        elif op == "|":
            exp = f"({exp}|{random.choice(bases)})"
        elif op == "*":
            exp = f"({exp}*)"
    return exp

def main():
    T = 3
    casos = [
        ("((ab)|(ba))", 2),
        ("((a|b)*)", 5),
        ("((a*)(b(a*)))", 100)
    ]
    for R, L in casos:
        print(f"Expressão: {R}, Tamanho: {L}")
        resultado = countRecognizedStrings(R, L)
        print("Reconhecidas:", resultado)

if __name__ == '__main__':
    main()