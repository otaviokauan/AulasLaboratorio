nota1 = float (input("digite sua primeira nota"))
nota2 = float (input("digite sua segunda nota"))
nota3 = float (input("digite sua terceira nota"))

n1 = nota1 * 4
n2 = nota2 * 3
n3 = nota3 * 3
resultado = (n1 + n2 + n3) / 10

if resultado >= 5:
    print(f"você foi aprovado")
else:
    print(f"você foi reprovado")