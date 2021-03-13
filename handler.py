import pandas as pd 
from flask import Flask, request, render_template
from werkzeug.security import generate_password_hash, check_password_hash
from flask_basicauth import BasicAuth
import os


df = pd.read_csv('dataset.csv')
df_city = df[['city', 'car_value']].groupby('city', as_index = False).mean()
df_means = df[['car_make', 'car_value']].groupby('car_make', as_index = False).mean()


#instan flask
app = Flask( __name__ )
#app.config['BASIC_AUTH_FORCE'] = True
app.config['BASIC_AUTH_USERNAME'] = 'admin'
app.config['BASIC_AUTH_PASSWORD'] = '123'

basic_auth = BasicAuth(app)


@app.route('/')
def index():
	return render_template('index.html')

#valor médio de todos os carros baseados no fabricante
@app.route('/mediacarrosvalor', methods = ['GET'])
@basic_auth.required
def valor_medio_geral():
	'''
		**Valor médio dos carros**

		Esta função pega o valor médio de todos os carros 
		agrupados por fabricante.

		- Exemplo::
		
			r = requests.get('http://127.0.0.1:5000/mediacarrosvalor', auth=(user, passw))
		
		- Resultado Esperado no sucesso::
		
			HTTP Status Code: 200

			{
				"car_make": {
					"0":"A",
					"1":"B",
					"2":"C",
					"3":"D",
					"4":"E",
					"5":"F",
					"6":"G",
					"7":"H",
					"8":"I",
					"9":"J"
				},
				"car_value":{
					"0":46144.9306930693,
					"1":50383.3846153846,
					"2":48890.2941176471,
					"3":50650.4636363636,
					"4":49621.3936170213,
					"5":46137.6972477064,
					"6":46113.3666666667,
					"7":46126.3269230769,
					"8":45487.5357142857,
					"9":47992.9826086957
				}
			}

	
	'''
	return df_means.to_json()

#valor médio de um fabricante de carro passado como parametro no request
@app.route('/mediafabricante', methods = ['GET'])
@basic_auth.required
def valor_medio_fabricante():
	'''
		**Valor médio do fabricante**

		Esta função retorna o valor médio do carro de um determinado fabricante
		passado como parâmetro no request.
		
		- Exemplo::
		
			r = requests.get('http://127.0.0.1:5000/mediafabricante?fabricante=B', auth=(user, passw))
		
		- Resultado Esperado no sucesso::
		
			HTTP Status Code: 200
		
			{
			"car_make":{
				"1":"B"
			},
			"car_value":{
				"1":50383.3846153846
			}
			}

	'''
	fabricante = request.args.get('fabricante')
	return df_means[df_means['car_make'] == fabricante].to_json()



#valor médio de todos os carros baseados nas cidades correspondentes
@app.route('/mediacidades', methods = ['GET'])
@basic_auth.required
def valor_medio_cidades():


	''' 
		**Valor médio das cidades**

		Essa função Pega o valor médio de todos os carros 
		agrupados por cidade.

		- Exemplo::
		
			r = requests.get('http://127.0.0.1:5000/mediacidades', auth=(user, passw))
		
		- Resultado Esperado no sucesso::
		
			HTTP Status Code: 200
			{
			"city":{
				"0":"C_01",
				"1":"C_02",
				"2":"C_03",
				"3":"C_04",
				"4":"C_05",
				"5":"C_06",
				"6":"C_07"
			},
			"car_value":{
				"0":47869.2534246575,
				"1":46464.6746031746,
				"2":47706.176056338, 
				"3":47865.8732394366,
				"4":48332.3834586466,
				"5":47592.4201183432,
				"6":48582.9366197183}
			}
		''' 
	return df_city.to_json()


#valor médio dos carros de uma cidade passada como parametro no request
@app.route('/mediacarroscidade', methods = ['GET'])
@basic_auth.required
def valor_medio_carro():
	'''
		**Valor médio por cidade**

		Esta função retorna o valor médio do carro em determinada
		cidade passada como parâmetro.
		
		- Exemplo::
		
			r = requests.get('http://127.0.0.1:5000/mediacarroscidade?carro=C_01', auth=(user, passw))
		
		- Resultado Esperado no sucesso::
		
			HTTP Status Code: 200
			{
			"city":{
				"0":"C_01"
			},
			"car_value":{
				"0":47869.2534246575
			}
			}
	'''

	carro = request.args.get('carro')
	return df_city[df_city['city'] == carro].to_json()



if __name__ == '__main__':
	#start flask
	app.run( host = '0.0.0.0', port = '5000')

	