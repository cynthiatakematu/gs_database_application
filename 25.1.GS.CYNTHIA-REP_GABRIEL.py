#Nome: Cynthia Emiko de Soua Takematu RM: 564100 (REPRESENTANTE)
#Nome: Gabriel Scaraficci de Lima RM: 563739

#1. Entrada de Dados:

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

    total = int(input("Total de pessoas afetadas: "))
    while True:
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

    #2. Armazenamento em Listas:
    tipos_de_desastres.append(tipo)
    paises.append(pais)
    cidades.append(cidade)
    bairros.append(bairro)
    ruas.append(rua)
    total_pessoas_afetadas.append(total)
    criancas.append(c)
    adultos.append(a)
    idosos.append(idoso)
    mobilidade_reduzida.append(mr)
    feridos.append(f)


#3. Análise de dados e 4. Relatório de Resultados:
#a. Exiba o total de desastres registrados.
print(f"\nTotal de desastres registrados: {quantidade}")

#b. Calcule o total geral de pessoas afetadas.
total_geral = sum(total_pessoas_afetadas)
print(f"\nTotal geral de pessoas afetadas: {total_geral}")

#c. Calcule o total de pessoas em cada categoria, somando os dados de todos os desastres.
total_criancas = sum(criancas)
total_adultos = sum(adultos)
total_idosos = sum(idosos)
total_mr = sum(mobilidade_reduzida)
total_feridos = sum(feridos)

print("\nResumo de pessoas afetadas por categoria:")
print(f"Crianças: {total_criancas} | Adultos: {total_adultos} | Idosos: {total_idosos} | Mobilidade reduzida: {total_mr} | Feridos: {total_feridos}")

#d. Identifique qual categoria foi mais afetada no geral.
categorias = ["Crianças", "Adultos", "Idosos", "Mobilidade reduzida", "Feridos"]
valores = [total_criancas, total_adultos, total_idosos, total_mr, total_feridos]
mais_afetada = categorias[valores.index(max(valores))]
print(f"\nCategoria mais afetada: {mais_afetada}")


#e. Descubra qual desastre teve o maior número de afetados e exiba o local completo (rua, bairro, cidade, país).
indice_mais_grave = total_pessoas_afetadas.index(max(total_pessoas_afetadas))
print("\nDesastre com maior número de afetados:")
print(f"Tipo: {tipos_de_desastres[indice_mais_grave]}")
print(f"Local: {ruas[indice_mais_grave]}, {bairros[indice_mais_grave]}, {cidades[indice_mais_grave]}, {paises[indice_mais_grave]}")