import sqlite3

path = r"C:\SqLite\aulas"
banco = sqlite3.connect(path + r'\exercicio_auto.db')
cursor = banco.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS Marcas (id integer_PK, nome varchar)')
cursor.execute('CREATE TABLE IF NOT EXISTS Fixacoes (id integer_PK, nome varchar)')
cursor.execute('CREATE TABLE IF NOT EXISTS Volumes (id integer_PK, nome varchar)')
cursor.execute('CREATE TABLE IF NOT EXISTS Essencias (id integer_PK, nome varchar)')
cursor.execute('CREATE TABLE IF NOT EXISTS Perfumes (id integer_PK, nome varchar, quantidade integer, '
               'id_Volumes_FK integer, id_Marca_FK integer, id_Fixacoes_FK integer)')
cursor.execute('CREATE TABLE IF NOT EXISTS Essencia_Perfume (id_Essencias_FK integer, id_Perfumes_FK integer)')
