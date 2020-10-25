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
def mostraIndex():
	# Renderiza a página Inicial.
	return render_template("index.html", tarefas=tarefas)# -> Passando a Lista como parâmetro

@app.route('/cadastro')
def mostraCadastro():
	# Renderiza a página de Cadastro.
	return render_template("cadastro.html")

@app.route('/cadastrar', methods=['POST',])
def cadastraTarefa():
	#Recupera os dados via HTTP.
	titulo = request.form['titulo']
	descricao = request.form['descricao']

	#Instacia nova Tarefa.
	nova_tarefa = Tarefa(titulo, descricao)

	#Adiciona a tarefa ao final da Lista.
	tarefas.append(nova_tarefa)

	#Redireciona para Home
	return redirect('/')

@app.route('/apagar/<id>')
def apagarTarefa(id):
	tarefas.remove(tarefas[int(id)])
	return redirect('/')

if __name__ == "__main__":
	# Iniciando a aplicação.
    app.run(host= '192.168.0.2')