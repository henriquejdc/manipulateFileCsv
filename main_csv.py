import csv

# r  → Abrir arquivo para leitura
# w → Abre o arquivo para gravação (irá truncar o arquivo)
# b → binário mais
# r+ → abrir arquivo para leitura e escrita
# a+ → abrir arquivo para leitura e gravação (anexa ao final)
# w+ → abre arquivo para leitura e gravação (trunca arquivos)


with open('file.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["id", "produto", "categoria",
                     "quantidade", "preço", "adicionado_em"])
    writer.writerow([1, "feijão", "comida", 20, 100, "01-01-2020"])
    writer.writerow([2, "arroz", "comida", 20, 150, "01-02-2020"])


with open('file.csv') as file:
    ler_csv = csv.reader(file)
    for row in ler_csv:
        print(row)


# Ler como dicionário
with open('file.csv', 'r') as file:
    ler_csv = csv.DictReader(file)
    for row in ler_csv:
        print(dict(row))
