preco = float(input("qual o valor de fabrica do carro? "))

precofabrica = preco * 0.28
imposto = preco * 0.45
resultado = precofabrica + imposto + preco

print(f"o carro sera ser vendido por {resultado}")