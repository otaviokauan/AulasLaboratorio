nota = int(input("qual sua nota? "))
faltas = int(input("quantas faltas você tem? "))

if faltas < 20:
    if nota >= 9:
        print("aluno de prestigio A !")
    elif nota >= 7.5 and nota < 8.9:
        print("aluno de prestigio B !")
    elif nota > 5 and nota < 7.4:
        print("aluno de prestigio C !")
    elif nota > 4 and nota < 4.9:
        print("aluno de prestigio D !")
    else:
        print("aluno de prestigio E !")

if faltas > 20:
    if nota >= 9 and nota < 10:
        print("aluno de prestigio B !")
    elif nota >= 7.5 and nota < 8.9:
        print("aluno de prestigio C !")
    elif nota > 5 and nota < 7.4:
        print("aluno de prestigio D !")
    elif nota > 4 and nota < 4.9:
        print("aluno de prestigio E !")
    else:
        print("aluno de prestigio E !")

#Otavio