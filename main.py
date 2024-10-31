from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug = True

# Configure SQLite Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contact_messages.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Message model
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)

# Create the database and tables
with app.app_context():
    db.create_all()

menu = ["Service 0", "Service 1", "Service 2"]

@app.route("/index")
@app.route("/")
def index():
    return render_template('index_pro.html', title="TenshI")

@app.route("/about")
def about():
    return render_template('about_pro.html', title="TenshI", menu=menu)

@app.route("/contacts")
def contacts():
    return render_template('contacts_pro.html', title="TenshI")

@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        message = request.form.get("message")

        # Create a new message instance
        new_message = Message(username=username, email=email, message=message)

        # Add to the database
        db.session.add(new_message)
        db.session.commit()

        return redirect(url_for('contact'))  # Redirect to the contact page after submission

    return render_template('contact_pro.html', title="TenshI")

if __name__ == '__main__':
    app.run(host='0.0.0.0')
