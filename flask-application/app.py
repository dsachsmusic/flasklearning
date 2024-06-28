from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
#from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_folder="./react-frontend", static_url_path="/")

cors = CORS(app)#, resources={r"/submit-form": {"origins": "http://localhost:5000"}},
            #methods=["POST"])

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
#db = SQLAlchemy(app)


#class ContactForm(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    name = db.Column(db.String(80), nullable=False)
#    email = db.Column(db.String(120), nullable=False)
#    message = db.Column(db.Text, nullable=False)

@app.route("/")
def index():
    return app.send_static_file("index.html")

# Add more routes for your Flask backend APIs here...
@app.route('/submit-form', methods=['POST'])
def submit_form():
    data = request.get_json()
    if data:
        return jsonify({'message': 'We got your info'}), 201
    #new_entry = ContactForm(
    #    name=data['name'],
    #    email=data['email'],
    #    message=data['message']
    #)
    #db.session.add(new_entry)
    #db.session.commit()

if __name__ == "__main__":
    #db.create_all()
    app.run(debug=True)