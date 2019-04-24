from autor import Autor
from trabalho import Trabalho
from autorDAO import autorDAO

autorDAO = autorDAO()

autor = Autor('Alan', 'alaantos32@gmail.com')
trabalho = Trabalho('lero', 7, 'liro')


autorDAO.save(autor)
print(autor.obterCodigo())