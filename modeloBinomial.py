import graphviz


def modeloBinomial(u, v, timesteps, S0, r): # Definição da função modeloBinomial.
    p = (1 + r - v) / (u - v) # Valor de p*.
    tree = [[S0]] # Inicializa a árvore binomial com o valor inicial do ativo.

    # Gera a árvore binomial
    for i in range(1, timesteps + 1):
        prev_row = tree[-1]
        new_row = [prev_row[0] * u]
        for j in range(1, len(prev_row)):
            new_row.append(prev_row[j] * v)
        new_row.append(prev_row[-1] * v)
        tree.append(new_row)

    return tree

u = float(input("Digite um valor para ser o fator u da ação: "))
v = 1 / u
timesteps = int(input("Digite o número de timesteps: "))
S0 = float(input("Digite o valor inicial do ativo: "))
r = float(input("Digite a taxa de juros: "))

tree = modeloBinomial(u, v, timesteps, S0, r)
for i in range(len(tree)):
    print(f"Período {i}: {tree[i]}")

