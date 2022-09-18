
import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='ong'
)


class Animal:
# praetros

    def __init__(self,id_exame, nomeanimal, cor, idade, raca,porte,disponivel, deficiente, adotado,castrado,exames,local_encontro,data_encontro):

        self.ide_exame = id_exame
        self.nome = nomeanimal
        self.idade = idade
        self.raca = raca
        self.porte_animal = porte
        self.deficiente = deficiente
        self.cor=cor
        self.disponivel=disponivel
        self.adotado=adotado
        self.castrado=castrado
        self.exames=exames
        self.local_encontro=local_encontro
        self.data_encontro=data_encontro


    @classmethod
    def cadastrar(self,id_exame, nomeanimal, cor, porte,raca, idade,disponivel, adotado, deficiente,castrado,exames,local_encontro,data_encontro):
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='ong'
        )
        cursor = connection.cursor()
        comando = f'insert into cad_animal(id_exame, nome, cor, porte, raça, idade, disponivel, adotado, deficiente, castrado, quant_exames,local_encontro, data_encontro) values(%s,%s,%s,%s,%s,%s,%s,%s, %s,%s,%s,%s,%s)'
        data=(

            f"{id_exame}",
            f"{nomeanimal}",
            f"{cor}",
            f"{porte}",
            f"{raca}",
            f"{idade}",
            f"{disponivel}",
            f"{adotado}",
            f"{deficiente}",
            f"{castrado}",
            f"{exames}",
            f"{local_encontro}",
            f"{data_encontro}"
        )
        cursor.execute(comando,data)
        connection.commit()
        print("\n===================== Cadastro concluído com sucesso =====================")
        cursor.close()
        connection.close()

    @classmethod
    def atualizardadosanimais(self,id_animal,id_exame, nomeanimal, cor, porte,raca, idade,disponivel, adotado, deficiente,castrado,exames,local_encontro,data_encontro):

        connection=mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='ong'
        )

        cursor=connection.cursor()
        comando=f"UPDATE cad_animal SET id_animal= '{id_animal}', id_exame='{id_exame}', nome='{nomeanimal}', cor='{cor}', porte='{porte}',raça='{raca}', idade='{idade}',disponivel='{disponivel}', adotado='{adotado}', deficiente='{deficiente}',castrado='{castrado}', quant_exames='{exames}',local_encontro='{local_encontro}',data_encontro='{data_encontro}' where id_animal='{id_animal}';"

        cursor.execute(comando)
        connection.commit()
        cursor.close()
        connection.close()

    @classmethod
    def consulta_animal(self,id_animal):

        connection=mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='ong'
        )
        cursor=connection.cursor()

        comando=f'select id_animal, id_exame, nome, cor, porte, raça, idade, disponivel, adotado, deficiente, castrado, quant_exames,local_encontro, data_encontro from cad_animal where  id_animal="{id_animal}" '
        cursor.execute(comando)
        resultado=cursor.fetchall()
        print(resultado)
        cursor.close()
        connection.close()

    @classmethod

    def deletar_aninal(self,id_animal):

        connection=mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='ong'
        )
        cursor=connection.cursor()

        comando=f'delete from cad_animal where id_animal= "{id_animal}"'

        cursor.execute(comando)
        connection.commit()

        cursor.close()
        connection.close()

