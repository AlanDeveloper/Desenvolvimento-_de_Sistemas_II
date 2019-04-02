import os

class GameDAO:
    def __init__(self, fl):
        self._file = fl
        self._path = './database/'
        if os.path.exists(self._path + self._file):
            fl = open(self._path + self._file, 'r')
        else: 
            fl = open(self._path + self._file, 'w')
        fl.close()

    def _getFile(self): return self._file
    def _setFile(self, namefl):
        os.rename(self._path + self._file, self._path + namefl)
        rt = 'Arquivo {} renomeado para {}'.format(self._file, namefl)
        self._file = namefl
        return rt
    
    file = property(_getFile, _setFile)

    def _persistence(self, game):
        fl = open(self._path + self._file, 'a+')
        game._setCode(self._getNGames() + 1)
        fl.write('{};{};{};{};\n'.format(game._getName(), game._getCode(), game._getLaunch(), game._getValue()))
        
        fl.close()
        return 'Jogo {} salvo!'.format(game._getName())
    def _changeGame(self, game):
        self._delGame(game._getCode())
        self._persistence(game)

    def _codeOrder(self):
        fl = open(self._path + self._file, 'r')

        lines = list()
        ct = 1
        for line in fl:
            line = line.split(';')
            line[1] = ct
            ct += 1
            lines += '{};{};{};{};\n'.format(line[0], line[1], line[2], line[3])
        fl.close()

        fl = open(self._path + self._file, 'w')
        fl.write(''.join(lines))

    def _delFile(self):
        os.remove(self._path + self._file)
        return 'Arquivo excluído'
    def _delGame(self, code):
        fl = open(self._path + self._file, 'r')

        lines = list()
        lines += [line for line in fl if line.find(';{};'.format(code)) == -1]
        fl.close()
        
        fl = open(self._path + self._file, 'w')
        fl.write(''.join(lines))
        fl.close()
        self._codeOrder()
        
        return 'Jogo excluído!'

    def _getFile(self): return self._file
    def _getGame(self, code):
        fl = open(self._path + self._file, 'r')

        game = [line for line in fl if line.find(';{};'.format(code)) != -1]
        fl.close()
        return (''.join(game)).split(';')
    def _getGames(self):
        fl = open(self._path + self._file, 'r')

        lines = list()
        for line in fl:
            line = (''.join(line)).split(';')
            line = "Nome: {}, Código: {}, Lançamento: {}, Valor: R$ {}".format(line[0], line[1], line[2], str(line[3]).replace('.', ',').replace(',0', ',00'))
            lines += line

        return ''.join(lines) if self._getNGames() > 0 else 'Nenhum jogo no arquivo'

    def _getNGames(self):
        fl = open(self._path + self._file, 'r')
        
        lines = list()
        lines += [line for line in fl]

        fl.close()
        return len(lines)