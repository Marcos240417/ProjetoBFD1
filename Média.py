name = input("Digite seu nome: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

print(f"{name}, sua média é: {media:.2f}")

if media >= 7:
    print(f"{name} está aprovado(a)")
elif media >= 6 and media >=5:
    print(f"{name} está em recuperação")
else:
    print(f"{name} está reprovado(a)")