from flask import Flask, render_template, request, redirect

app = Flask(__name__)
filmes = []

@app.route('/')
def index():
    return render_template('lista_filmes.html', filmes=filmes)


@app.route('/adicionar_filme', methods=['GET', 'POST'])
def adicionar_filme():
    if request.method == 'POST':
        nome = request.form['nome']
        data = request.form['data']
        genero = request.form['genero']
        codigo = len(filmes)
        filmes.append([codigo, nome, data, genero])
        return render_template('lista_filmes.html', filmes=filmes)
    else:
        return render_template('adicionar_filme.html')

@app.route('/editar_filme/<int:codigo>', methods=['GET', 'POST'])
def editar_filme(codigo):
    if request.method == 'POST':
        nome = request.form['nome']
        data = request.form['data']
        genero = request.form['genero']
        filmes[codigo] = [codigo, nome, data, genero]
        return redirect('/lista_filmes')
    else:
        filme = filmes[codigo]
        return render_template('editar_filme.html', filme=filme)

@app.route('/apagar_filme/<int:codigo>')
def apagar_filme(codigo):
    filmes.pop(codigo)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)