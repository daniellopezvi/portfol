from flask import Flask, render_template, send_from_directory, url_for, request, redirect
import os, csv 

app = Flask(__name__) #esto hace que el nombre de este fichero sea reconocido como __main__, y será el nombre de la app
print(__name__)

@app.route('/')
def my_home():
	return render_template('index.html')

# @app.route('/index.html')
# def my_home2():
# 	return render_template('index.html')

@app.route('/<string:page_name>') #coge la dirección que se da en el URL y la busca en templates
def html_page(page_name):
	return render_template(page_name)


# @app.route('/<username>/<int:post_id>')
# def hello_world(username=None, post_id=None):
# 	# print(url_for('static', filename='favicon.ico'))
# 	return render_template('./index.html', name=username, post_id=post_id)



# @app.route('/about')
# def about():
# 	# print(url_for('static', filename='favicon.ico'))
# 	return "This blog is about me"



#      método para poner el favicon, pero no usado, ya que es mejor ponerlo en el html
# @app.route('/favicon.ico')
# def favicon():
#     return send_from_directory(os.path.join(app.root_path, 'static'),'favicon.ico', mimetype='image/vnd.microsoft.icon')




# De la documentación de Flask
# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     error = None
#     if request.method == 'POST':
#         if valid_login(request.form['username'],
#                        request.form['password']):
#             return log_the_user_in(request.form['username'])
#         else:
#             error = 'Invalid username/password'
#     # the code below is executed if the request method
#     # was GET or the credentials were invalid
#     return render_template('login.html', error=error)

#esto para que nos devuelva una respuesta básica al rellenar el formulario
# @app.route('/submit_form', methods=['POST', 'GET'])
# def submit_form():
#        return "form submitted hoooorayyy!!"

#y para que capture lo que introduzcamos en el formulario y lo exporte al txt
# def export_data(data):
# 	with open("database.txt", mode="a") as database:
# 			email = data["email"]
# 			subject = data["subject"]
# 			message = data["message"]
# 			file = database.write(f"\n{email}, {subject}, {message}")

def export_to_csv(data):
	with open("database.csv", mode="a") as database2:
			email = data["email"]
			subject = data["subject"]
			message = data["message"]
			csv_writer = csv.writer(database2, delimiter=",", lineterminator='\n', quotechar='"', quoting=csv.QUOTE_MINIMAL)
			csv_writer.writerow([email,subject,message])

#consejo de modificar linea 70:
#with open("database.csv", newline='', mode="a") as database2:



@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == "POST":
		data = request.form.to_dict()
#vuelve lo que entremos en un diccionario
		export_to_csv(data)
		return redirect('/thankyou.html')
	else:
		return "something went wrong, try again"




