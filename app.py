from flask import Flask, render_template, url_for

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
     return 'welcome to the home page'

if __name__ == "__main__":
     app.run(debug=True)
