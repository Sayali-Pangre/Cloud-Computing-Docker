from flask import Flask
from flask_restful import Resource, Api



app = Flask(__name__)
api = Api(app)


class Book(Resource):
    def get(self):
        return {
                'books':['python for Beginners' , 'IOT for architects','HPC application','cloud computing','machine learning','Artificial Intelligence']   
                }


#Create routes
api.add_resource(Book,'/')


#Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80,debug=True)
