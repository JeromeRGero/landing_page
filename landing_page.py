from flask import Flask, render_template, redirect, request, url_for
import os
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/ninjas")
def ninjas():
    return render_template('ninjas.html')

@app.route("/dojos/new")
def dojos():
    return render_template('dojos.html')

@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)

@app.route('/process', methods=["POST"])
def process():
    print "Got Post Info!"
    name = request.form['name']
    # email = request.form['email']
    print(name)
    name = 'Hello ' + name + '!'
    return render_template('dojos.html', name=name)



app.run(debug=True)