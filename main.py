def q1():
    '''ano = int(input())
    periodicidade = int(input())

    ano1 = ano + periodicidade
    ano2 = ano1 + periodicidade
    ano3 = ano2 + periodicidade
    ano4 = ano3 + periodicidade

    print(ano1, ano2, ano3, ano4, end=".")'''

    ano = int(input(" "))
    periodicidade = int(input(" "))

    inicio = ano + periodicidade
    fim = ano + (periodicidade * 4)

    for a in range(inicio, fim +1, periodicidade):
        print(a, end=" ")

def q2():
    ler = True
    while ler:
        numero = int(input(""))
        if numero <=0:
            break
        inicio = 2
        fim = numero// 2
        primo = False
        for n in range(inicio, fim +1):
            if numero % n == 0:
                print("Não")
                primo = False
                break
        else: 
            primo = True
            print("Primo")
   
def q3():
    ler = True
    dinheiro_doado = 0
    quantidade = 0
    while ler:
        valor = float(input(""))
        if valor < 0:
            break
        dinheiro_doado += valor
        quantidade += 1
    if quantidade == 0:
        print("0.00")
        print("0.00")
    else:
        media = dinheiro_doado/quantidade
        print(f"{dinheiro_doado:.2f}")
        print(f"{media:.2f}")

def q4():

    dias = int(input(""))
    km = int(input(""))
    if dias <= 0:
        print("Valor inválido")
    else:
        base = dias * 90
        quota = 100
        taxa = 0
        if km > quota:
            taxa = 12 * (km - quota)
        total = base + taxa

        print(F"{total:.2f}")
def q5():
    escala = int(input(""))
    temp = float(input(""))

    if escala == "C":
        K= temp +273
        F = temp * 1.8+32
        print(f"{K:.2f} K")
        print(f"{F:.2f} F")
    elif escala == "F":
        C = temp - 273
        K = ((temp-32) * 5/9) + 273
        print(f"{C:.2f} C")
        print(f"{K:.2f} K")
    else:
        if temp < 0:
            print("Valor de temperatura abaixo do minimo")
        else:

            C = temp -273
            F = (temp-273)*1.8+32
            print(f"{C:.2f} C")
            print(f"{F:.2f} F")


if __name__=="__main__":
    # teste sua questão manualmente aqui
    pass

