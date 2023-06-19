n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))
r1 = n1 + n2
r2 = n1 * n2
r3 = n1 - n2
if n2 != 0:
    r4 = n1 / n2
    print("A divisão de", n1, "por", n2, "é:", r4)
else:
    print("Não é possível dividir por zero.")
r5 = n1 % n2
print("O resto da divisão de", n1, "por", n2, "é:", r5)
print("A soma de", n1, "e", n2, "é:", r1)
print("A multiplicação de", n1, "e", n2, "é:", r2)
print("A subtração de", n1, "e", n2, "é:", r3)