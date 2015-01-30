
# Import Flask class as basis for web application
from flask import Flask, render_template

# Instance of web application
app = Flask(__name__)

@app.route("/") # Decoration that makes function run when URL is visited
def hello_world():
  return render_template('base.html')
  return "Hello World!"

@app.route("/hello/<name>")  # Use <> as placeholder for URL string text to pass to function
def hello_person(name):  # 'name' used as placeholder and function argument
  return render_template('template_hello.html', user_name=name)

@app.route("/jedi/<first_name>/<last_name>")
def jedi_name(first_name, last_name):
  return render_template('template_jedi.html', first_name = first_name, last_name = last_name)
  
  
if __name__ == "__main__":
    # Application to listen on host/port
    app.run(host="0.0.0.0", port=8080)