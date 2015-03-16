from flask import Flask, render_template

app = Flask(__name__)
@app.route("/jedi/<firstname>/<lastname>")
def jedi(firstname,lastname):
  jedi_name = lastname[0:3]+firstname[0:2]
  return render_template("template.html",jedi_=jedi_name)

if __name__ == "__main__":  
  app.run(host="0.0.0.0", port=8080)  
  
  
  