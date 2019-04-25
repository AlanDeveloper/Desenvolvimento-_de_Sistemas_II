# -*- encoding: utf-8 -*- 
# Caso não por está linha de cima a palavra "João" é reconhecida como Non-ASCII = Erro de sintaxe

from autor import Autor
from autorDAO import autorDAO
from trabalho import Trabalho

autorDAO = autorDAO()

autor = Autor('Alan', 'alansantos32@gmail.com')
autorDAO.save(autor)
autor2 = Autor('Junior', 'jr@gmail.com')
autorDAO.save(autor2)

autor.alterarEmail('alanssantos32@gmail.com')
autorDAO.save(autor)

autor3 = autorDAO.buscar(3)
if autor3 == None: print('Não encontrado')

autor3 = autorDAO.buscar(4)
try:
    autor3.alterarEmail('jr2@gmail.com')
except AttributeError:
    print('Não encontrado')
autorDAO.save(autor3)
print('Salvo' if autor3 != None else 'Não salvo')