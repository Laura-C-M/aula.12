from datetime import date
ano=int(input("Vamos ver a que categoria pertences num desporto, para descobrires tens de inserir o teu ano de nascimento"))
idade = date.today().year - ano
if idade <= 9:
    print("Estás na classe Benjamim")
elif idade <=14 and idade > 9 :
    print("Estás na classe Infantil")
elif idade <= 19 and idade > 14:
    print("Estás na classe Júnior")
elif idade <= 25 and idade > 19:
    print("Estás na classe Sénior")
elif idade > 25:
    print("Estás na classe Master")