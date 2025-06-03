#Nome: Cynthia Emiko de Soua Takematu RM: 564100 (REPRESENTANTE)
#Nome: Gabriel Scaraficci de Lima RM: 563739

# b. Para cada desastre, colete e armazene em listas as informações.
tipos_de_desastres = []
paises = []
cidades = []
bairros = []
ruas = []
total_pessoas_afetadas = []
#categorias
criancas = []
adultos = []
idosos = []
mobilidade_reduzida = []
feridos = []

# a. Solicite ao usuário a quantidade de desastres registrados.
quantidade = int(input("Insira a quantidade de desastres registrados: "))

for i in range(quantidade):
    print(f"\n--- Desastre {i+1} ---")

    tipo = input("Tipo de desastre: ")
    pais = input("País: ")
    cidade = input("Cidade: ")
    bairro = input("Bairro: ")
    rua = input("Rua: ")

    while True:
        total = int(input("Total de pessoas afetadas: "))
        print("Informe quantas pessoas pertencem a CADA uma das categorias:")

        c = int(input("Número de crianças: "))
        a = int(input("Número de adultos: "))
        idoso = int(input("Número de idosos: "))
        mr = int(input("Número de pessoas com mobilidade reduzida: "))
        f = int(input("Número de feridos: "))

        soma = c + a + idoso + mr + f

        if soma > total:
            print(f"A soma das categorias ({soma}) excede o total de afetados ({total}). Confira as informações.")
        elif soma < total:
            print(f"A soma das categorias ({soma}) é menor que o total de afetados ({total}). Confira as informações.")
        else:
            break

    # Armazenar os dados nas listas
    tipos_de_desastres.append(tipo)
    paises.append(pais)
    cidades.append(cidade)
    bairros.append(bairro)
    ruas.append(rua)
    total_pessoas_afetadas.append(total)
    #Armazenar nas categorias
    criancas.append(c)
    adultos.append(a)
    idosos.append(idoso)
    mobilidade_reduzida.append(mr)
    feridos.append(f)
