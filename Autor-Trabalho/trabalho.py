# -*- encoding: utf-8 -*- 

from datetime import datetime

class Trabalho():
    def __init__(self, conteudo, nota, titulo):
        self._conteudo = conteudo
        self._nota = nota
        self._titulo = titulo
        self._dataAtt = datetime.now()
        self._codigo = None
        self._autores = []
    
    def adicionarAutor(self, autor):
            self._autores.append(autor)

    def obterTrabalho(self):
        return 'Conteúdo: {}, Nota: {}, Título: {}, Código: {}, Data da Entrega: {}, Data da última atualização: {}'.format(self._conteudo, self._nota, self._titulo, self.obterCodigo(), self.obterDataEntrega(), self._dataAtt)

    def obterConteudo(self): 
        return self._conteudo
    def obterNota(self): 
        return self._nota
    def obterDataEntrega(self): 
        return self._dataEntrega
    def obterDataAtt(self): 
        return self._dataAtt
    def obterTitulo(self): 
        return self._titulo
    def obterCodigo(self): 
        return self._codigo

    def alterarConteudo(self, conteudo): 
        self._conteudo = conteudo
    def alterarNota(self, nota): 
        self._nota = nota
    def alterarDataEntrega(self, dataEntrega): 
        self._dataEntrega = dataEntrega
    def alterarDataAtt(self, data): 
        self._dataAtt = data
    def alterarTitulo(self, titulo): 
        self._titulo = titulo
    def alterarCodigo(self, codigo): 
        self._codigo = codigo

    conteudo = property(obterConteudo, alterarConteudo)
    nota = property(obterNota, alterarNota)
    titulo = property(obterTitulo, alterarTitulo)
    dataAtt = property(obterDataAtt, alterarDataAtt)
    codigo = property(obterCodigo, alterarCodigo)
    dataEntrega = property(obterDataEntrega, alterarDataEntrega)