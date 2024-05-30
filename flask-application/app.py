# https://medium.com/@bravinwasike18/how-to-build-and-deploy-a-flask-application-to-kubernetes-cluster-e52d460fcb14

from flask import Flask
app = Flask(__name__)
@app.route("/",methods=['GET'])
def hello_world():
 return "<p>This is a Hello World application</p>"
if __name__ == '__main__':
 app.run(debug=True)

