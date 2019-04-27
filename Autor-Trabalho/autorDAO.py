# -*- encoding: utf-8 -*- 

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

                return 'Autor alterado'
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

                return 'Autor salvo'
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
        except BaseException:
            return None

        cur.close()
        conexao.close()
    def listar(self):
        conexao = serverDao().connect()
        cur = conexao.cursor()

        autores = []

        try:
            cur.execute('SELECT * FROM "Autor"')
            resposta = cur.fetchall()

            for linha in resposta:
                qt = Autor(linha[1], linha[2])
                qt.alterarCodigo(linha[0])

                autores.append(qt)  

            return autores
        except IndexError: 
            return None

        cur.close()
        conexao.close()
    def deletar(self, autor):
        conexao = serverDao().connect()
        cur = conexao.cursor()

        try:
            cur.execute('DELETE FROM "Autor" WHERE cod = %s', [autor.obterCodigo()])
            conexao.commit()
        except AttributeError:
            return 'Não encontrado'

        cur.close()
        conexao.close()

        return 'Autor deletado'
