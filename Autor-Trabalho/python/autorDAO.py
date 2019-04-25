from serverDAO import serverDao
from autor import Autor

class autorDAO():
    def save(self, autor):
        try:
            if autor.codigo:
                conexao = serverDao().connect()
                cur = conexao.cursor()

                cur.execute('UPDATE "Autor" SET nome = %s, email = %s WHERE cod = %s', [autor.obterNome(), autor.obterEmail(), autor.obterCodigo()])
                conexao.commit()
                
                cur.close()
                conexao.close()
            else:
                conexao = serverDao().connect()
                cur = conexao.cursor()

                cur.execute('INSERT INTO "Autor"(nome, email) VALUES(%s, %s)', [autor.obterNome(), autor.obterEmail()])
                cur.execute('SELECT max(cod) FROM "Autor"')
                
                res = cur.fetchall()
                autor.alterarCodigo(res[0][0])
                conexao.commit()
                
                cur.close()
                conexao.close()
        except AttributeError:
            return None
    def buscar(self, codigo):
        conexao = serverDao().connect()
        cur = conexao.cursor()

        try:
            cur.execute('SELECT * FROM "Autor" WHERE cod = %s', [codigo])
            resposta = cur.fetchall()
   
            qt = Autor(resposta[0][1], resposta[0][2])
            qt.alterarCodigo(codigo)

            return qt
        except IndexError: 
            return None

        cur.close()
        conexao.close()