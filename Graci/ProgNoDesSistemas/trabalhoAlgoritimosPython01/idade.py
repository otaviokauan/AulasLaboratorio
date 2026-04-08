idade = float (input("Em que ano você nasceu? "))
data = float (input ("Em que ano estamos? "))

idadeA = data - idade
idadeM = idadeA * 30
idadeD = idadeA * 365


print(f"Sua idade em anos é {idadeA}")
print(f"Sua idade em meses é {idadeM}")
print(f"Sua idade em dias é {idadeD}")

