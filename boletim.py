from flask import Flask, render_template, request, redirect
import sqlite3

boletim = Flask(__name__)
def obterConn():
    conn= sqlite3.connect('boletim.bd')
    return conn
@boletim.route('/formAlunos')
def formAluno():
    return render_template('newAluno.html')

@boletim.route('/cadastrarAluno', methods=['POST'])
def cadasAluno():
        nome=request.form['nome']
        conn=obterConn()
        conn.execute('INSERT INTO Aluno(nome) values(?)',[nome])
        conn.commit()
        conn.close()
        return redirect('/alunos')
    

@boletim.route('/alunos')
def Alunos():
    conn=obterConn()
    search=conn.execute('select * from Aluno;')
    alunos=search.fetchall()
    return render_template('alunos.html',alunos=alunos)

@boletim.route('/boletim/<int:id>')
def boleti(id):
    conn=obterConn()
    search=conn.execute('select * from Disciplinas where Mat=?;',[id])
    disciplinas=search.fetchall()
   
    return render_template('boletim.html',disciplinas=disciplinas)



if __name__  == '__main__':
    boletim.run()    