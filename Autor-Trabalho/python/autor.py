class Autor():
    def __init__(self, nome, email):
        self._nome = nome
        self._email = email
        self._codigo = None
    
    def obterNome(self): 
        return self._nome
    def obterEmail(self): 
        return self._email 
    def obterCodigo(self): 
        return self._codigo

    def alterarNome(self, nome):
        self._nome = nome
    def alterarEmail(self, email): 
        self._email = email
    def alterarCodigo(self, codigo): 
        self._codigo = codigo

    nome = property(obterNome, alterarNome)
    email = property(obterEmail, alterarEmail)
    codigo = property(obterCodigo, alterarCodigo)
