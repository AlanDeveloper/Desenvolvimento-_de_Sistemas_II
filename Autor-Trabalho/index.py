# -*- encoding: utf-8 -*- 
from mng import Maneger

if __name__ == "__main__":
    print('Bem Vindo!')
    print('Utilize as teclas numéricas para nos dizer sua ação no sistema\n')
    print('Crie autores, trabalhos e vincule-os sendo eles salvados no banco de dados')

    # # # # # # # # # # # # 

    mng = Maneger()
    while True:
        num = mng.stage(input('\n1 - Autores | 2 - Trabalhos | 3 - Encerrar sistema: '))
        if num == '3': break