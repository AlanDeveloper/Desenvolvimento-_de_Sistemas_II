from datetime import datetime
class Trabalho():
    def __init__(self, conteudo, nota, titulo):
        self._conteudo = conteudo
        self._nota = nota
        self._titulo = titulo
        self._dataAtt = datetime.now()

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
    def alterarDataAtt(self): 
        self._dataAtt = datetime.now()
    def alterarTitulo(self, titulo): 
        self._titulo = titulo
    def alterarCodigo(self, codigo): 
        self._codigo = codigo

    conteudo = property(obterConteudo, alterarConteudo)
    nota = property(obterNota, alterarNota)
    titulo = property(obterTitulo, alterarTitulo)

    # where dataatualizacao = datapega
