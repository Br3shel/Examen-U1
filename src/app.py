from flask import Flask, render_template,request

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/habilidades')
def habilidades():
    return render_template('habilidades.html')

@app.route('/datos')
def datos():
    return render_template('datos.html')

@app.route('/mensaje', methods=['GET','POST'])
def mensaje():
    if request.method=='POST':
        info=(request.form['mensaje'])
        return render_template('enviado.html',info=info)
    else:    
        return render_template('mensaje.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)