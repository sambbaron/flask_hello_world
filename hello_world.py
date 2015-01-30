
# Import Flask class as basis for web application
from flask import Flask

# Instance of web application
app = Flask(__name__)

@app.route("/hello") # Decoration that makes function run when URL is visited
def hello_world():
  return "Hello World!"

@app.route("/hello/<name>")  # Use <> as placeholder for URL string text to pass to function
def hello_person(name):  # 'name' used as placeholder and function argument
  html = """
        <h1>
            Hello {}!
        </h1>
        <p>
            Here's a picture of a kitten.  Awww...
        </p>
        <img src="http://placekitten.com/g/200/300">
  """
  return html.format(name.title())

@app.route("/jedi/<first_name>/<last_name>")
def jedi_name(first_name, last_name):
  return "Your jedi name is {}{}".format(last_name[:3], first_name[:2])
  
  
if __name__ == "__main__":
    # Application to listen on host/port
    app.run(host="0.0.0.0", port=8080)