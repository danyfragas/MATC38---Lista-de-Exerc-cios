import random

#Questão 5

from collections import defaultdict

def similar_pair(n, k, edges):
    tree = defaultdict(list)
    for pai, filho in edges:
        tree[pai].append(filho)

    resultado = 0

    def dfs(no, ancestrais):
        nonlocal resultado
        for anc in ancestrais:
            if abs(anc - no) <= k:
                resultado += 1
        for filho in tree[no]:
            dfs(filho, ancestrais + [no])

    raiz = set(range(1, n + 1)) - {filho for _, filho in edges}
    dfs(raiz.pop(), [])

    return resultado

def generateTestCases():
    return [
        (5, 2, [(3, 2), (3, 1), (1, 4), (1, 5)]),
        (6, 3, [(1, 2), (1, 3), (2, 4), (3, 5), (3, 6)]),
        (4, 1, [(1, 2), (2, 3), (3, 4)]),
        (7, 4, [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (6, 7)]),
        (3, 0, [(1, 2), (2, 3)])
    ]

def main():
    testCases = generateTestCases()
    for idx, (n, k, edges) in enumerate(testCases, 1):
        print(f"🧪 Teste {idx}")
        print(f"n = {n}, k = {k}, edges = {edges}")
        result = similar_pair(n, k, edges)
        print(f"➡ Resultado: {result}\n")

if __name__ == "__main__":
    main()