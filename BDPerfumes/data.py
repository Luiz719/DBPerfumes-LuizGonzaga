import sqlite3


def titulo(n, s, p, tabela):
    print('=' * n)
    print(f'{s}'.center(n))
    print('=' * n)
    e = ''
    while e not in ("S", "N"):
        e = input(f"Cadastrar nova(o) {p}? [S/N]").upper().strip()
    if e == "S":
        i = 1
        while True:
            nome = input(f"Digite o nome da(o) {p}: ")
            if p == 'Perfume':
                quant = int(input("Digite a quantidade do perfume: "))
                im = int(input("Digite o id da Marca desejada: "))
                ifi = int(input("Digite o id da Fixação desejada: "))
                iv = int(input("Digite o id do Volume desejado: "))
                cursor.execute(f"INSERT INTO {tabela} VALUES ({i}, '{nome}', {quant}, {iv}, {im}, {ifi})")
            else:
                cursor.execute(f"INSERT INTO {tabela} VALUES ({i}, '{nome}')")
            e = ''
            while e not in ("S", "N"):
                e = input(f"Cadastrar nova(o) {p}? [S/N]").strip().upper()
            if e == "N":
                break
            else:
                i += 1


path = r"C:\SqLite\aulas"
banco = sqlite3.connect(path + r'\exercicio_auto.db')
cursor = banco.cursor()

titulo(40, "CADASTRO - MARCAS", "Marca", "Marcas")
titulo(40, "CADASTRO - FIXAÇÕES", "Fixação", "Fixacoes")
titulo(40, "CADASTRO - ESSÊNCIAS", "Essência", "Essencias")
titulo(40, "CADASTRO - VOLUMES", "Volume", "Volumes")
titulo(40, "CADASTRO - PERFUMES", "Perfume", "Perfumes")

banco.commit()
