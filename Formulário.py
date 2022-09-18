def __init__(self, moradores, motivo, possui_animais, animais, profissao, moradia, favor_adocao, despesas, rotina,
             tempo_fora):
    self.moradores = moradores
    self.motivo_adocao = motivo
    self.possui_animais = possui_animais
    self.quais_animais = animais
    self.profissao = profissao
    self.tipo_moradia = moradia
    self.favor_adocao = favor_adocao
    self.condicao_despesas = despesas
    self.rotina = rotina
    self.tempo_fora = tempo_fora


@classmethod
def formulario_perguntas(self, moradores, motivo, possui_animais, animais, profissao, moradia, favor_adocao, despesas,
                         rotina, tempo_fora):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="ong"
    )
    cursor = connection.cursor()
    comando_insert = "INSERT INTO formulario (moradores, motivo_adocao, possui_animais, quais_animais, profissao, tipo_moradia, favor_adocao, condicao_despesas, rotina, tempo_fora) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    data = (
        f'{moradores}',
        f'{motivo}',
        f'{possui_animais}',
        f'{animais}',
        f'{profissao}',
        f'{moradia}',
        f'{favor_adocao}',
        f'{despesas}',
        f'{rotina}',
        f'{tempo_fora}'
    )
    cursor.execute(comando_insert, data)
    connection.commit()
    print("\n===================== Formulário enviado com sucesso! =====================")
    cursor.close()
    connection.close()


