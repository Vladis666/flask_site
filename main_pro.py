from flask import Flask, render_template, request

app = Flask(__name__)
app.debug = True
menu = ["Service 0", "Service 1", "Service 2"]

@app.route("/index")
@app.route("/")
def index():
    return render_template('index_pro.html', title="TenshI")
@app.route("/about")
def about():
    return render_template('about_pro.html', title="TenshI",menu=menu)

@app.route("/contacts")
def contacts():
    return render_template('contacts_pro.html', title="TenshI")
@app.route("/contact", methods=["POST", "GET"])
def contact():
    print(request.form)
    return render_template('contact_pro.html', title="TenshI")

if __name__ == '__main__':
   # app.run(debug=True)
    app.run(host='0.0.0.0')
