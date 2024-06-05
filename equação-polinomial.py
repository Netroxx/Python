from sympy import symbols, Eq, solve, I

# Define as variáveis simbólicas
x = symbols('x')

# Define a equação polinomial (x + 1)^2 + 9 = 0
equacao = Eq((x + 1)**2 + 9, 0)

# Resolve a equação para encontrar as raízes complexas
raizes = solve(equacao, x)

# Imprime as raízes complexas
print(f"As raízes complexas da equação são: {raizes}")

# Exemplo de operações com números complexos
z1 = 4 + 3*I
z2 = 1 - 2*I

# Soma dos números complexos
soma = z1 + z2

# Produto dos números complexos
produto = z1 * z2

# Imprime os resultados das operações
print(f"A soma dos números complexos é: {soma}")
print(f"O produto dos números complexos é: {produto}")
