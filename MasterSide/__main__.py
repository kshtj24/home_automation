from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homePage():
    return render_template('home.html')

@app.route('/bedroom')
def bedroomControlPage():
    return render_template('bedroom.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
