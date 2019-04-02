import datetime
class Game:
    def __init__(self, name, launch, value):
        self._name = name
        self._launch = launch
        self._value = value
        self._code = 'Nenhum'

        self._setLaunch(launch)
    def __str__(self):
        return "Nome: {}, Código: {}, Lançamento: {}, Valor: R$ {}".format(self._name, self._code, self._launch, str(self._value).replace('.', ',').replace(',0', ',00'))

    def _getName(self): return self._name
    def _getLaunch(self): return self._launch
    def _getValue(self): return self._value
    def _getCode(self): return self._code

    def _setName(self, name): self._name = name
    def _setLaunch(self, launch):
        launch = launch.split('-')
        if len(launch[2]) == 4 and len(launch[1]) == 2 and len(launch[0]) == 2:
            self._launch = datetime.date(int(launch[2]), int(launch[1]), int(launch[0]))
    def _setValue(self, value): 
        try:
            int(value)
            self._value = value
        except ValueError:
            print('Valor inválido')
        self._value = value
    def _setCode(self, code): self._code = code

    name = property(_getName, _setName)
    launch = property(_getLaunch, _setLaunch)
    value = property(_getValue, _setValue)
    code = property(_getCode, _setCode)