from usuario import Usuario
from psycopg2 import connect
from dao import DAO

class UsuarioDao(DAO):
    def __init__(self):
        super().__init__()
    
    def login(self, usuario):
        with connect(self._dados_con) as conn:
            cur = conn.cursor()

            cur.execute('SELECT * FROM usuario WHERE login = %s and senha = md5(%s)', [usuario._login, usuario._senha])
            conn.commit()
            resposta = cur.fetchall()
            cur.close()

        if resposta[0][0] != None:
            return Usuario(cod=resposta[0][0], nome=resposta[0][1], login=resposta[0][2], senha=resposta[0][3])
        else: 
            return False
