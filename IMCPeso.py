peso = float(input("Digite o seu peso (em kg, ex: 70.5): "))
altura = float(input("Digite a sua altura (em metros, ex: 1.75): "))

imc = peso / (altura ** 2)

print(f"\nSeu IMC é: {imc:.2f}")

if imc < 18.5:
    print("Condição: Abaixo do peso")

elif imc >= 18.5 and imc < 25:
    print("Condição: Peso normal")

elif imc >= 25 and imc <= 30:
    print("Condição: Acima do peso")

else: 
    print("Condição: Obeso")