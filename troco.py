precouni = float (input("qual o valor do produto? "))
quant = float (input("quantos produtos foram comprados? "))
pagamento = float (input("quanto dinheiro foi dado pelo cliente? "))

total = precouni * quant

if pagamento > total:
  troco =  pagamento - total
  print(f"seu troco é de {troco:g} reais")
else:
  if total > pagamento:
    devendo = total - pagamento
    print(f"faltam {devendo:g} reais")
  else:
    print(f" obrigado pela compra :) ")