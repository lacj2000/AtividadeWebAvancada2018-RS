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
    return render_template('boletim.html',disciplinas=disciplinas,id=id)

@boletim.route('/formDisciplina/<int:id>')
def formDis(id):
    return render_template('newDisc.html',id=id)

@boletim.route('/cadastrarDisciplina/<int:id>',methods=['GET','POST'])
def cadasDisci(id):
    nome=str(request.form['nome'])
    nota1 = float(request.form['nota1'])
    nota2= float(request.form['nota2'])
    nota3 = float(request.form['nota3'])
    nota4 = float(request.form['nota4'])
    conn=obterConn()
    conn.execute('insert into Disciplinas(Mat,Nota1,Nota2,Nota3,Nota4,Nome)Values(?,?,?,?,?,?)',[id,nota1,nota2,nota3,nota4,nome])
    conn.commit()
    conn.close()
    id1=str(id)
    return redirect('boletim/'+id1+'')

@boletim.route('/alterarDis/<int:ids>')
def alterarDiscip(ids):

    ida=str(id)
    return redirect('boletim/'+ida+'')

@boletim.route('/deleteDis/<int:id>')
def deleteDiscip(id):
    conn=obterConn()
    conn.execute('delete from Disciplinas where id_disciplina=?',[id])
    conn.commit()
    conn.close()
    return redirect('/alunos')


if __name__  == '__main__':
    boletim.run()    