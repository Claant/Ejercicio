from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1/<float:peso>/<float:altura>')
def calcularIMC(peso, altura):
    calculo= peso/ (altura ** 2)
    if calculo < 18.5:
        categoria = 'Bajo peso'
    elif calculo < 25:
        categoria = 'Peso normal'
    elif calculo < 30:
        categoria = 'Sobrepeso'
    else:
        categoria = 'Obesidad'
    return render_template('ejercicio1.html', resultado=calculo, cat=categoria)


@app.route('/ejercicio2/<int:n1>/<int:n2>/<int:n3>')
def calcularMayor(n1,n2,n3):
    lista=[n1,n2,n3]
    resultado = max(lista)
    return render_template('ejercicio2.html', resultado=resultado)

@app.route('/ejercicio3/<int:num>')
def tablaDeMultiplicar(num):
    tabla =[]
    for i in range(1, 13):
        resultado = i * num
        tabla.append((i, resultado))
    return render_template('ejercicio3.html', num=num, tabla=tabla)

@app.route('/ejercicio4/<int:nota1>/<int:nota2>/<int:asistencia>')
def ejercicio4(nota1,nota2,asistencia):
    promedio = (nota1+nota2)/2
    if asistencia >=80 and promedio>=40:
        estado = "APROBADO"
    else:
        estado="REPROBADO"
    return render_template('ejercicio4.html',promedio=promedio,estado=estado)

if __name__ == '__main__':
    app.run()