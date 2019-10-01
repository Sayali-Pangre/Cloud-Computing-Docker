#import framework
#product service
from flask import Flask
from flask_restful import Resource, Api
#instatiate the app
app = Flask(__name__)
api = Api(app)
class Book(Resource):
  def get(self):
    return {
       'books': ['python for beginner','IoT fro architects','HPC applications', 'cloud computing', 'wireless sensor network']
           }
#create routes
api.add_resource(Book,'/')
#run the application
if __name__=='__main__':
  app.run(host='0.0.0.0',port=80,debug=True)
