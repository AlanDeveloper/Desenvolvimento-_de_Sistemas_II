from mng import Maneger


if __name__ == "__main__":
    print('Bem Vindo!')
    print('Use esse sistema como uma biblioteca de jogos')
    print('Utilize as teclas numéricas para nos dizer sua ação no sistema\n')
    print('Dicas de uso: \n - Aqui você pode criar múltiplos arquivos e cada arquivo pode conter seu(s) jogo(s)\n - Antes de criar ou salvar um jogo entre na seção "Arquivo de controle" e selecione um arquivo para nos dizer onde salvar seu jogo')

    # # # # # # # # # # # # 

    mng = Maneger()
    while True:
        num = mng._stage(input('\n1 - Arquivo de controle | 2 - Jogos | 3 - Encerrar sistema: '))
        if num == '3': break