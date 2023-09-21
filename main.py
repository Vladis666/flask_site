app = Flask(__name__)

@app.route("/index")
@app.route("/about")
def about():

if __name__ == '__main__':
    app.run(debug=True)

