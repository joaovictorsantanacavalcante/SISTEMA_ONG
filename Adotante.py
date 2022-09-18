
import mysql.connector

class adotante:
    def __init__(self, id_adotante, nome, nascimento, telefone1, telefone2, email, usuario, senha):
        self.__id_adotante = id_adotante
        self.__nome = nome
        self.__data_nasc = nascimento
        self.__telefone1 = telefone1
        self.__telefone2 = telefone2
        self.__email = email
        self.__usuario = usuario
        self.__senha = senha

    @classmethod
    def cadastro_adotante(self, id_adotante, nome, nascimento, telefone1, telefone2, email, usuario, senha):
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="ong"
        )
        cursor = connection.cursor()
        comando_insert = "INSERT INTO adotante (id_adotante, nome, data_nasc, telefone1, telefone2, email, usuario, senha) VALUES (%s, %s, %s, %s, %s, %s, %s, aes_encrypt(%s, 'ad'))"
        data = (
            f'{id_adotante}',
            f'{nome}',
            f'{nascimento}',
            f'{telefone1}',
            f'{telefone2}',
            f'{email}',
            f'{usuario}',
            f'{senha}'
        )
        cursor.execute(comando_insert, data)
        connection.commit()
        print("\n===================== Cadastro concluído com sucesso =====================")
        cursor.close()
        connection.close()

    def consultar_adotantes():
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="ong"
        )
        cursor = connection.cursor()

        comando_select = f"SELECT * FROM adotante"

        cursor.execute(comando_select)
        results = cursor.fetchall()

        cursor.close()
        connection.close()

        for result in results:
            print(result)

    @classmethod
    def selecionar_adotantes(cls, id_adotante):
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="ong"
        )
        select = f"SELECT id_adotante, nome, data_nasc, telefone1, telefone2, email, usuario, senha FROM ong.adotante WHERE id_adotante = '{id_adotante}';"
        cursor = connection.cursor()
        cursor.execute(select)
        row = cursor.fetchone()
        cursor.close()
        connection.close()
        lista = []
        for r in row:
            lista.append(r)
        return adotante(lista[0], lista[1], lista[2], lista[3], lista[4], lista[5], lista[6], lista[7])

    def atualizar_adotantes(self, id_adotante, nome, nascimento, telefone1, telefone2, email, usuario, senha):
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="ong"
        )
        cursor = connection.cursor()

        comando_update = f"UPDATE adotante SET id_adotante = %s, nome = %s, data_nasc = %s, telefone1 = %s, telefone2 = %s, email = %s, usuario = %s, senha = %s WHERE id_adotante = '{id_adotante}'"
        data = (
            f'{id_adotante}',
            f'{nome}',
            f'{nascimento}',
            f'{telefone1}',
            f'{telefone2}',
            f'{email}',
            f'{usuario}',
            f'{senha}'
        )
        cursor.execute(comando_update, data)
        connection.commit()

        recordsaffected = cursor.rowcount

        cursor.close()
        connection.close()

        print("\n=====================", recordsaffected, "Registro alterado com sucesso =====================\n")

    def deletar_adotantes(self, id_adotante):
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="ong"
        )
        cursor = connection.cursor()

        comando_delete = "DELETE FROM adotante WHERE id_adotante = %s"
        data = (id_adotante,)

        cursor.execute(comando_delete, data)
        connection.commit()

        recordsaffected = cursor.rowcount

        cursor.close()
        connection.close()

        print("\n=====================", recordsaffected, "Registro excluído com sucesso =====================")

    @classmethod
    def login(self, usuario, senha):
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="ong"
        )
        lista = []
        while len(lista) == 0:
            cursor = connection.cursor()
            comando = f"SELECT usuario, senha FROM adotante WHERE usuario = '{usuario}' AND senha = aes_encrypt('{senha}', 'ad')"
            cursor.execute(comando)
            results = cursor.fetchall()
            for r in results:
                lista.append(r)
            if len(lista) == 0:
                print("\n===================== [ERRO] Nome de usuário ou senha inválido, tente novamente! =====================")
                usuario = input("\nUsuário: ")
                senha = input("\nSenha: ")
        cursor.close()
        connection.close()
        print("\n===================== Login realizado com sucesso! =====================")

