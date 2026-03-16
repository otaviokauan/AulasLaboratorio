
qalcatra = float(input("quantos quilos de alcatra foi comprado? "))
qfile = float(input("quantos quilos de file duplo foi comprado? "))
qpicanha = float(input("quantos quilos de picanha foi comprado? "))
tipo = float (input("para comprar com cartão tabaja digite 1, para outros metodos digite 2 "))

if qfile >= 5:
    vfile = 5.80
else:
    vfile = 4.90

if qalcatra >= 5:
    valcatra =6.80
else:
    valcatra =  5.90

if qpicanha >= 5:
    vpicanha = 7.80
else:
    vpicanha = 6.90

valor = (qpicanha * vpicanha) + (qfile * vfile) + (qalcatra * valcatra)

if tipo == 1:
    valor = valor * 0.95

print(f"o valor total de sua compra deu {valor:g}")

#OTAVIO
