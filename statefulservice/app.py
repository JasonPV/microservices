from flask import Flask
from flask import Flask, request
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
import pickle


app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://jason:12345678@db/microservices'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

try:
    with open('data.pickle', 'rb') as f:
        data = pickle.load(f)
except:
    data = {}

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    theme = db.Column(db.String(120), nullable=False)
    genereted = db.Column(db.String(255), nullable=False)


class GetTexts(Resource):
    def get(self):
        theme = request.args.get('theme')
        text = Data.query.filter_by(theme=theme).first()
        if text:
            text = text.genereted
            if theme in data.keys():
                data[theme] += 1
            else:
                data[theme] = 1
            with open('data.pickle', 'wb') as f:
                pickle.dump(data, f)
            return text
            
        else:
            if theme in data.keys():
                data[theme] += 1
            else:
                data[theme] = 1
            with open('data.pickle', 'wb') as f:
                pickle.dump(data, f)
            return "this theme not used"


class GetStats(Resource):
    def get(self):
        return data


api.add_resource(GetTexts, "/gettexts/", "/gettexts/<string:theme>/")
api.add_resource(GetStats, "/getstats/", "/getstats/")


if __name__ == '__main__':
    app.run()
