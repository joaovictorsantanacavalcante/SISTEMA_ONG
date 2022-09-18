import mysql.connector
import Adotante

class endereco(Adotante.adotante):
    def __init__(self, id_endereco, logradouro, numero, bairro, cidade, uf, cep, id_adotante, nome, nascimento, telefone1, telefone2, email, usuario, senha):
        super().__init__(id_adotante, nome, nascimento, telefone1, telefone2, email, usuario, senha)
        self.__id_endereco = id_endereco
        self.__id_adotante = id_adotante
        self.__logradouro = logradouro
        self.__numero = numero
        self.__bairro = bairro
        self.__cidade = cidade
        self.__uf = uf
        self.__cep = cep

    @classmethod
    def cadastro_endereco(self, id_endereco, id_adotante, logradouro, numero, bairro, cidade, uf, cep):
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="ong"
        )
        cursor = connection.cursor()
        comando_insert = "INSERT INTO endereço (id_endereço, id_adotante, logradouro, numero, bairro, cidade, uf, cep) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        data = (
            f'{id_endereco}',
            f'{id_adotante}',
            f'{logradouro}',
            f'{numero}',
            f'{bairro}',
            f'{cidade}',
            f'{uf}',
            f'{cep}'
        )
        cursor.execute(comando_insert, data)
        connection.commit()
        cursor.close()
        connection.close()

    def consultar_enderecos():
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="ong"
        )
        cursor = connection.cursor()

        comando_select = f"SELECT * FROM endereço"

        cursor.execute(comando_select)
        results = cursor.fetchall()

        cursor.close()
        connection.close()

        for result in results:
            print(result)

    @classmethod
    def atualizar_enderecos(self, id_endereco, id_adotante, logradouro, numero, bairro, cidade, uf, cep):
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="ong"
        )
        cursor = connection.cursor()

        comando_update = f"UPDATE endereço SET id_endereço = %s, id_adotante = %s, logradouro = %s, numero = %s, bairro = %s, cidade = %s, uf = %s, cep = %s WHERE id_endereço = '{id_endereco}'"
        data = (
            f'{id_endereco}',
            f'{id_adotante}',
            f'{logradouro}',
            f'{numero}',
            f'{bairro}',
            f'{cidade}',
            f'{uf}',
            f'{cep}'
        )
        cursor.execute(comando_update, data)
        connection.commit()

        recordsaffected = cursor.rowcount

        cursor.close()
        connection.close()

        print("\n=====================", recordsaffected, "Registro alterado com sucesso =====================")

    @classmethod
    def deletar_enderecos(self, id_endereco):
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="ong"
        )
        cursor = connection.cursor()

        comando_delete = "DELETE FROM endereço WHERE id_endereço = %s"
        data = (id_endereco,)

        cursor.execute(comando_delete, data)
        connection.commit()


        cursor.close()
        connection.close()

