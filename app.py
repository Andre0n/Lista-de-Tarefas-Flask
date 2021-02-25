#coding:utf8

# Importando o Flask.
from flask import Flask, render_template, request, redirect

# Importando a Classe Tarefa.
from Tarefa import Tarefa

# Iniciando Objeto app do tipo Flask.
app = Flask(__name__)

# Lista de objetos do tipo Tarefa.
tarefas = []


# Define a rota Inicial.
@app.route('/')
def mostra_home():
	# Renderiza a página Inicial.
	return render_template("index.html", tarefas=tarefas)# -> Passando a Lista como parâmetro


@app.route('/cadastro')
def mostra_cadastro():
	# Renderiza a página de Cadastro.
	return render_template("cadastro.html")


@app.route('/editar/<int:id>')
def mostra_editar(id):
	# Renderiza a página de Cadastro.
	return render_template("editar.html", tarefas = tarefas,  id = id)


@app.route('/cadastrar', methods=('GET', 'POST'))
def cadastrar_tarefa():
    if request.method == 'POST':
        # Recupera os dados via HTTP.
        titulo = request.form['titulo']
        descricao = request.form['descricao']
        # Instacia nova Tarefa.
        nova_tarefa = Tarefa(titulo, descricao)
        # Adiciona a tarefa ao final da Lista.
        tarefas.append(nova_tarefa)
    # Redireciona para Home
    return redirect('/')


@app.route('/apagar/<id>')
def apagar_tarefa(id):
	# Recebe o identificador e remove da lista.
	tarefas.remove(tarefas[int(id)])

	# Redireciona para Home
	return redirect('/')


@app.route('/edit/<id>', methods=['POST', ])
def edit(id):
    id = int(id)
    if request.method == 'POST':
        if (id < len(tarefas)):
            novo_titulo = request.form['titulo']
            nova_descricao = request.form['descricao']
            tarefas[id].set_titulo(novo_titulo)
            tarefas[id].set_descricao(nova_descricao)
    return redirect('/')


if __name__ == "__main__":
	# Iniciando a aplicação.
    app.run( )
