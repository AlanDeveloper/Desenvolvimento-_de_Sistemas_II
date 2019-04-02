from gameDAO import GameDAO
from game import Game
import os

class Maneger:

    def __init__(self): 
        self._control = None
        self._game = None
    def _stage(self, num):
        if num == '1': self._controlFile()
        if num == '2': self._controlGame()
        if num == '3': 
            cond = input('Deseja excluir os arquivos?(S/N): ').upper()
            if cond == 'S':
                dirs = os.listdir('./database/')
                for file in dirs: os.remove('./database/' + file)
            print('Encerrando sistema...')
        return num

    def _controlFile(self):
        while True:
            print('\nArquivo atual: {}'.format(self._control._getFile() if self._control != None else 'Nenhum'))
            num = input('1 - Criar arquivo | 2 - Listar arquivos | 3 - Selecionar arquivo | 4 - Alterar nome do arquivo | 5 - Excluir arquivo | 6 - Voltar: ')
            if num == '1': 
                nameFl = input('Selecione um nome para o arquivo: ') + '.txt'
                if os.path.exists('./database/' + nameFl): 
                    print('Arquivo já existe')
                else: 
                    self._control = GameDAO(nameFl)
            if num == '2':
                dirs = os.listdir('./database/')
                if len(dirs) > 0: 
                    for file in dirs: print(file) 
                else: 
                    print('Pasta vazia')
            if num == '3':
                nameFl = input('Digite o nome do arquivo: ') + '.txt'
                if os.path.exists('./database/' + nameFl):
                    self._control = GameDAO(nameFl)
                else: 
                    print('Arquivo não existe')
            if num == '4': 
                if self._control != None: 
                    try :
                        nameFl = input('Digite o novo nome: ') + '.txt'
                        print(self._control._setFile(nameFl))
                    except FileExistsError:
                        print('O nome {} já está sendo utilizado'.format(nameFl))
                else:
                    print('Selecione algum arquivo antes')
            if num == '5':
                try:
                    print(self._control._delFile())
                    self._control = None
                except AttributeError:
                    print('Favor criar um arquivo ou selecionar algum')
            if num == '6': break
    
    def _controlGame(self):
        while True:
            num = input('\n1 - Criar jogo | 2 - Salvar jogo | 3 - Alterar jogo | 4 - Listar jogos | 5 - Excluir jogo | 6 - Voltar: ')

            if num == '1':
                name = input('Digite um nome: ')
                launch = input('Digite a data de lançamento(DD-MM-YYYY): ')
                value = input('Digite o valor: ')

                if name != '' and launch != '' and value != '':
                    try:
                        int(value)
                        dt = launch.split('-')
                        if len(dt) == 3: 
                            self._game = Game(name, launch, value)
                            print('Jogo {} criado'.format(self._game._getName()))
                        else:
                            print('Data inválida')
                    except ValueError: 
                        print('Verifique se digitou data/valor válidos')
                else: 
                    print('Um dos campos está vazio')
            if num == '2': 
                try:
                    print(self._control._persistence(self._game))
                except AttributeError:
                    print('Crie um jogo válido antes')
            if num == '3':
                qt = 'S'
                if self._game != None:
                    if self._game._getCode() == 'Nenhum':
                        qt = input('Você possui um jogo não salvo, caso prossiga irá perde-lo\nDeseja prosseguir?(S/N): ').upper()
                if qt == 'S':
                    try:
                        newgame = self._control._getGame(input('Digite o código: '))
                        self._game = Game(newgame[0], newgame[2], newgame[3])
                        self._game._setCode(newgame[1])

                        qt = input('1 - Nome | 2 - Lançamento | 3 - Valor: ')
                        if qt == '1': self._game._setName(input('Selecione o novo nome: '))
                        if qt == '2': self._game._setLaunch(input('Selecione o novo lançamento(DD-MM-YYYY): '))
                        if qt == '3': self._game._setValue(input('Selecione o novo valor: '))
                        
                        self._control._changeGame(self._game)
                        print('Jogo {} alterado'.format(self._game._getName()))
                    except AttributeError:
                        print('Selecione o arquivo atual')
                    except IndexError:
                        print('Arquivo vazio')
            if num == '4': 
                try:
                    print(self._control._getGames())
                except AttributeError:
                    print('Selecione o arquivo antes')
            if num == '5':
                qt = 'S'
                if self._game != None:
                    if self._game._getCode() == 'Nenhum':
                        qt = input('Você possui um jogo não salvo, caso prossiga irá perde-lo\nDeseja prosseguir?(S/N): ').upper()
                if qt == 'S':
                    try:
                        code = input('Digite o código: ')
                        int(code)
                        if self._control._getNGames() != 0:
                            print(self._control._delGame(code))
                        else: 
                            print('Arquivo vazio')
                
                    except ValueError:
                        print('Código inválido')
                    except AttributeError:
                        print('Selecione o arquivo atual')
            if num == '6': break