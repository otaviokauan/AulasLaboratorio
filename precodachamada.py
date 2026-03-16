tempo = float (input("qual o tempo(em minutos) telefonado? "))

conta = 50
if tempo > 100 :
    conta2 = conta + ((tempo - 100) *2)
    print(f"sua conta ficará por {conta2:g}") 
else :
     print(f"sua conta ficará por {conta:g}")