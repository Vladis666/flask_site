from flask import Flask, render_template

app = Flask(__name__)
app.debug = True
menu = ["Service 0", "Service 1", "Service 2"]

@app.route("/index")
@app.route("/")
def index():
    return render_template('index01.html', title="TenshI")
@app.route("/about")
def about():
    return render_template('about01.html', title="TenshI",menu=menu)

@app.route("/contacts")
def contacts():
    return render_template('contacts001.html', title="TenshI")

if __name__ == '__main__':
   # app.run(debug=True)
    app.run(host='0.0.0.0')

