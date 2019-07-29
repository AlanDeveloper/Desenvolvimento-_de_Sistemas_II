# Não consegui inserir na url os cod, por isso não é possível entrar nelas, apenas se fizer manualmente os comandos funcionam


#!-*- conding: utf8 -*-

from flask import Flask, render_template, request, session, redirect
from usuariodao import UsuarioDao
from ideiadao import IdeiaDao
from usuario import Usuario
from ideia import Ideia

app = Flask(__name__, template_folder='template')

@app.before_first_request
def before():
    session['logged_in'] = False

@app.route('/')
def index():
    if session['logged_in'] == False:
        return render_template('form.html')
    else: 
        return ideia()

@app.route('/user', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if session['logged_in'] == False:
            user = Usuario(login=request.form['username'], senha=request.form['password'])
            res = UsuarioDao().login(user)
            if res != False:
                user = res
                session['logged_in'] = True
                session['username'] = request.form['username']
                session['password'] = request.form['password']
            else:
                return 'Dados incorretos'
    return redirect('/')    

@app.route('/exit')
def logout():
    session['logged_in'] = False
    return redirect('/')

@app.route('/ideia', methods=['GET', 'POST'])
def ideia():
    if request.method == 'POST':
        user = Usuario(login=session['username'], senha=session['password'])
        user = UsuarioDao().login(user)
        i = Ideia(titulo=request.form['title'], descricao=request.form['desc'], usuario=user)
        IdeiaDao().inserir(i)
    return redirect('/list')

@app.route('/<page>')
def view(page):
    if session['logged_in'] == False:
        return redirect('/')
    if page == 'list':
        dados = IdeiaDao().listar(10, 0)
        return render_template(page + '.html', dados=dados)
    return render_template(page + '.html')

@app.route('/about/<cod>')
def about(cod):
    if session['logged_in']:
        i = IdeiaDao().buscar(cod)
        user = Usuario(login=session['username'], senha=session['password'])
        user = UsuarioDao().login(user)
        return render_template('about.html', ideia=i, user=user)
    return redirect('/')

@app.route('/del/<cod>')
def delete(cod):
    if session['logged_in']:
        i = IdeiaDao().buscar(cod)
        IdeiaDao().excluir(i)
    return redirect('/')

@app.route('/alter/<cod>')
def alterar(cod):
    if session['logged_in']:
        user = Usuario(login=session['username'], senha=session['password'])
        user = UsuarioDao().login(user)
        i = Ideia(titulo=request.form['title'], descricao=request.form['desc'], usuario=user, cod=cod)
        IdeiaDao().salvar(i)
    return redirect('/')

def main():
    app.secret_key = 'minha chave'
    app.env = 'development'
    app.run(debug=True, port=2000)

if __name__ == "__main__":
    main()
