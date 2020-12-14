import sqlite3


def titulo(n, s):
    print('=' * n)
    print(f'{s}'.center(n))
    print('=' * n)
    cursor.execute(f"SELECT * FROM {s.title()}")
    tabela = cursor.fetchall()
    print("ID".ljust(21), "NOME".ljust(50))
    for i in tabela:
        print(str(i[0]).ljust(22), end="")
        print(i[1].ljust(50))


path = r"C:\SqLite\aulas"
banco = sqlite3.connect(path + r'\exercicio_auto.db')
cursor = banco.cursor()

titulo(40, "MARCAS")
titulo(40, "FIXACOES")
titulo(40, "VOLUMES")
titulo(40, "ESSENCIAS")
titulo(40, "ESSENCIA_PERFUME")

cursor.execute("SELECT * FROM Perfumes")
t2 = cursor.fetchall()
print('=' * 60)
print('PERFUMES'.center(60))
print('=' * 60)
print("ID".ljust(5), "Nome".ljust(10), "QNT.".ljust(10), "Volume".ljust(10), "Marca".ljust(10), "Fixação")
for m in t2:
    print(str(m[0]).ljust(5), end="")
    print(m[1].ljust(12), end="")
    print(str(m[2]).ljust(12), end="")
    print(str(m[3]).ljust(12), end="")
    print(str(m[4]).ljust(12), end="")
    print(str(m[5]))
