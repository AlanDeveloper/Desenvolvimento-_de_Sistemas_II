# -*- encoding: utf-8 -*- 

from datetime import datetime
from autor import Autor
from autorDAO import autorDAO
from trabalho import Trabalho
from trabalhoDAO import TrabalhoDAO

class Maneger():
    def stage(self, num):

        if num == '1':
            opcAt = input('\n1 - Registrar | 2 - Alterar | 3 - Listar | 4 - Deletar | 5 - Voltar: ')
            if opcAt == '1':
                self.registroAutor()
            if opcAt == '2': 
                self.alterarAutor()
            if opcAt == '3':
                self.listarAutor()
            if opcAt == '4':
                self.deletarAutor()

        if num == '2':
            opcAt = input('\n1 - Registrar | 2 - Alterar | 3 - Listar | 4 - Deletar | 5 - Vincular autor | 6 - Voltar: ')
            if opcAt == '1':
                self.registroTrabalho()
            if opcAt == '2': 
                self.alterarTrabalho()
            if opcAt == '3':
                self.listarTrabalho()
            if opcAt == '4':
                self.deletarTrabalho()
            if opcAt == '5':
                self.vincularAutor()

        return num

    def registroAutor(self): 
        atDAO = autorDAO()

        nome = input('Digite o nome: ')
        email = input('Digite o e-mail: ')

        print(atDAO.save(Autor(nome, email)))
    def alterarAutor(self):
        atDAO = autorDAO()

        at = atDAO.buscar(input('Digite o código: '))
        if at != None: 
            opcoes = input('1 - Todos | 2 - Nome | 3 - Email: ')
            if opcoes == '1': 
                at.alterarNome(input('Digite o nome: '))
                at.alterarEmail(input('Digite o  email: '))
            if opcoes == '2': 
                at.alterarNome(input('Digite o nome: '))
            if opcoes == '3': 
                at.alterarEmail(input('Digite o  email: '))
            
            print(atDAO.save(at))
        else: 
            print('Não encontrado')
    def listarAutor(self):
        atDAO = autorDAO()

        lista = atDAO.listar()
        for lt in lista:
            print(lt.obterAutor())
        if len(lista) == 0:
            print('Nenhum registrado')
    def deletarAutor(self):
        atDAO = autorDAO()

        at = atDAO.buscar(input('Digite o código: '))
        print(atDAO.deletar(at))

    def registroTrabalho(self): 
        tbDAO = TrabalhoDAO()

        conteudo = input('Digite o conteudo: ')
        nota = input('Digite a nota: ')
        titulo = input('Digite o titulo: ')

        print(tbDAO.save(Trabalho(conteudo, nota, titulo)))
    def alterarTrabalho(self):
        tbDAO = TrabalhoDAO()

        tb = tbDAO.buscar(input('Digite o código: '))

        if tb != None: 
            opcoes = input('1 - Todos | 2 - Conteudo | 3 - Nota | 4 - Título: ')
            if opcoes == '1': 
                tb.alterarConteudo(input('Digite o conteudo: '))
                tb.alterarNota(input('Digite a  nota: '))
                tb.alterarTitulo(input('Digite o  titulo: '))
            if opcoes == '2': 
                tb.alterarConteudo(input('Digite o conteudo: '))
            if opcoes == '3': 
                tb.alterarNota(input('Digite a  nota: '))
            if opcoes == '4':
                tb.alterarTitulo(input('Digite o  titulo: '))
            
            print(tbDAO.save(tb))
        else: 
            print('Não encontrado')
    def listarTrabalho(self):
        tbDAO = TrabalhoDAO()

        lista = tbDAO.listar()
        for lt in lista:
            print(lt.obterTrabalho())
        if len(lista) == 0:
            print('Nenhum registrado')

    def deletarTrabalho(self):
        tbDAO = TrabalhoDAO()

        tb = tbDAO.buscar(input('Digite o código: '))
        print(tbDAO.deletar(tb))

    def vincularAutor(self):
        tbDAO = TrabalhoDAO()
        atDAO = autorDAO()

        trabalho = tbDAO.buscar(input('Digite o código do trabalho: '))
        autor = atDAO.buscar(int(input('Digite o código do autor: ')))
        print(tbDAO.adicionar( autor, trabalho))