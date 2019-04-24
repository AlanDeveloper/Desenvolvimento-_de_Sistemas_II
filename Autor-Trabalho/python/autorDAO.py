from serverDAO import serverDao

class autorDAO():
    def save(self, autor):
        if autor.codigo:
            print('ola')
        else:
            conexao = serverDao().connect()
            cur = conexao.cursor()

            cod = cur.execute('INSERT INTO "Autor"(nome, email) VALUES(%s, %s);SELECT (cod) FROM "Autor" WHERE nome = %s', [autor.obterNome(), autor.obterEmail(), autor.obterNome()])
            print(cur.fecthall())
            conexao.commit()
            
            cur.close()
            conexao.close()
            autor.alterarCodigo(cod)

