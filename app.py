from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'oi'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resultados')
def resultados():
    calculos = [
        {
            'distancia': 182,
            'consumo': 12,
            'preco': 5.72,
        },
        {
            'distancia': 43,
            'consumo': 9,
            'preco': 6.02,
        },
         {
            'distancia': 337,
            'consumo': 13,
            'preco': 5.89,
        },
        {
            'distancia': 715,
            'consumo': 10,
            'preco': 5.53,
        }


    ]
    return render_template('resultados.html', calculos=calculos, total=len(calculos))

@app.route('/calcular', methods=['GET', 'POST'])
def calcular():

    if request.method == 'POST':
        distancia = request.form.get('distancia', '0')
        consumo = request.form.get('consumo', '0')
        preco = request.form.get('preco', '0')

        LN = round(float(distancia) / (float(consumo) ), )
        CT = round(float(LN) * (float(preco) ), )
        QR = round(float(CT) / (float(distancia) ), )   

        if QR < 8:
            classificacao = 'Beberrão'
        
        elif QR <= 15:
            classificacao = 'Padrão'
        
        elif QR <= 18:
            classificacao = 'Econômico'

        elif QR > 18.0:
            classificacao = 'Super econômico'

        else:
            classificacao = 'Deu erro na conta!'

        flash(f'IMC: {QR} - Classificação: {classificacao}', 'success')

        return  redirect(url_for('resultados'))


    return render_template('formulario.html')


if __name__ == '__main__':
    app.run(debug=True)