from datetime import date
ano_nasc=int(input("Estamos em 2025, diz-me em que ano nascestes para verificar se vais ou não para o recensamento"))
idade = date.today().year - ano_nasc
if idade < 18:
    print("Ainda não tens idade para o recensamento")
elif idade == 18:
    print("Estás na idade para o recenseamento")
elif idade == 19:
    print("Estás na idade para o recenseamento")
elif idade > 19:
    print("Já passou o prazo para o recensamento")
