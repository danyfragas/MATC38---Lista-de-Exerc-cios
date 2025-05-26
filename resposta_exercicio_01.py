import random

#Questão 1

def resolver_labirinto(n, m, k, maze, tunnels):
    from collections import defaultdict

    tunnel_map = {}
    for i1, j1, i2, j2 in tunnels:
        tunnel_map[(i1, j1)] = (i2, j2)
        tunnel_map[(i2, j2)] = (i1, j1)

    memo = {}

    def dfs(i, j): #função que calc a probabilidade de escapar a partide de i, j
        if (i, j) in memo:
            return memo[(i, j)]
        if maze[i][j] == '%': #célula = saída
            return 1.0
        if maze[i][j] == '*': #célula = mina
            return 0.0

        maze[i] = maze[i][:j] + '#' + maze[i][j+1:] 
        total = 0
        soma = 0.0

        for di, dj in [(-1,0),(1,0),(0,-1),(0,1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m and maze[ni][nj] != '#':
                if (ni, nj) in tunnel_map:
                    ni, nj = tunnel_map[(ni, nj)]
                soma += dfs(ni, nj)
                total += 1

        maze[i] = maze[i][:j] + 'O' + maze[i][j+1:] 
        memo[(i, j)] = soma / total if total else 0.0
        return memo[(i, j)]

    for i in range(n):
        for j in range(m):
            if maze[i][j] == 'A':
                return dfs(i, j)

    return 0.0

def gerar_labirinto(n, m):
    elementos = ['O'] * 5 + ['#', '*', '%']
    labirinto = [''.join(random.choice(elementos) for _ in range(m)) for _ in range(n)]
    i, j = random.randint(0, n - 1), random.randint(0, m - 1)
    linha = list(labirinto[i])
    linha[j] = 'A'
    labirinto[i] = ''.join(linha)
    return labirinto

def gerar_tuneis(k, n, m):
    tuneis = set()
    while len(tuneis) < k:
        i1, j1 = random.randint(0, n - 1), random.randint(0, m - 1)
        i2, j2 = random.randint(0, n - 1), random.randint(0, m - 1)
        if (i1 != i2 or j1 != j2) and abs(i1 - i2) + abs(j1 - j2) > 1:
            tuneis.add((i1, j1, i2, j2))
    return list(tuneis)

def main():
    n, m, k = 5, 6, 2
    maze = gerar_labirinto(n, m)
    tunnels = gerar_tuneis(k, n, m)

    print("Maze:")
    for linha in maze:
        print(linha)
    print("Tunnels:", tunnels)

    resultado = resolver_labirinto(n, m, k, maze, tunnels)
    print("Probabilidade de fuga:", resultado)

if __name__ == '__main__':
    main()
