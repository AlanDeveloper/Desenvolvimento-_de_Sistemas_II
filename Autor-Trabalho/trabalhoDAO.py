# -*- encoding: utf-8 -*- 

from serverDAO import serverDao
from trabalho import Trabalho
from autorDAO import autorDAO

class TrabalhoDAO():
    def save(self, trabalho):
        if trabalho.codigo:
            conexao = serverDao().connect()
            cur = conexao.cursor()

            try:

                cur.execute('UPDATE "Trabalho" SET conteudo = %s, nota = %s, "dataEntrega" = %s, titulo = %s, "dataHoraAtualizacao" = NOW() WHERE cod = %s', [trabalho.obterConteudo(), trabalho.obterNota(), trabalho.obterDataEntrega(), trabalho.obterTitulo(), trabalho.obterCodigo()])
                conexao.commit()
            except NameError:
                return None
                
            cur.close()
            conexao.close()

            return 'Trabalho alterado'
        else:
            conexao = serverDao().connect()
            cur = conexao.cursor()

            cur.execute('INSERT INTO "Trabalho" (conteudo, nota, titulo, "dataHoraAtualizacao") VALUES(%s, %s, %s, NOW())', [trabalho.obterConteudo(), trabalho.obterNota(), trabalho.obterTitulo()])
            cur.execute('SELECT max(cod) FROM "Trabalho"')
            
            res = cur.fetchall()
            trabalho.alterarCodigo(res[0][0])
            conexao.commit()
            
            cur.close()
            conexao.close()

            return 'Trabalho salvo'
    def buscar(self, codigo):
        conexao = serverDao().connect()
        cur = conexao.cursor()
        atDAO = autorDAO()
        try:
            cur.execute('SELECT * FROM "Trabalho" WHERE cod = %s', [codigo])
            resposta = cur.fetchall()

            qt = Trabalho(resposta[0][1], resposta[0][2], resposta[0][4])
            qt.alterarDataEntrega(resposta[0][3])
            qt.alterarDataAtt(resposta[0][5])
            qt.alterarCodigo(codigo)
            
            cur.execute('SELECT * FROM "TrabalhoAutor" WHERE "codTrabalho" = %s', [codigo])
            resposta = cur.fetchall()

            for at in resposta:
                autor = atDAO.buscar(at[0])
                qt.adicionarAutor(autor)
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

        trabalhos = []

        try:
            cur.execute('SELECT * FROM "Trabalho"')
            resposta = cur.fetchall()

            for linha in resposta:
                qt = Trabalho(linha[1], linha[2], linha[4])
                qt.alterarCodigo(linha[0])
                qt.alterarDataEntrega(linha[3])
                qt.alterarDataAtt(linha[5])

                trabalhos.append(qt)  

            return trabalhos
        except IndexError: 
            return None

        cur.close()
        conexao.close()
    def deletar(self, trabalho):
        conexao = serverDao().connect()
        cur = conexao.cursor()

        try:
            cur.execute('DELETE FROM "Trabalho" WHERE cod = %s', [trabalho.obterCodigo()])
            conexao.commit()
        except AttributeError:
            return 'Não encontrado'

        cur.close()
        conexao.close()

        return 'Trabalho deletado'

    def adicionar(self, autor, trabalho):
        conexao = serverDao().connect()
        cur = conexao.cursor()

        cur.execute('INSERT INTO "TrabalhoAutor" ("codAutor", "codTrabalho") VALUES(%s, %s)', [autor.obterCodigo(), trabalho.obterCodigo()])
        conexao.commit()

        cur.close()
        conexao.close()

        return 'Autor vinculado'