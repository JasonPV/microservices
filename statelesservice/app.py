from flask import Flask
from flask import Flask, request
from flask_restful import Api, Resource
from generate import generate
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://jason:12345678@db/microservices'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    theme = db.Column(db.String(120), nullable=False)
    genereted = db.Column(db.String(255), nullable=False)

db.create_all()


class GenText(Resource):
    def get(self):
        theme = request.args.get('theme')
        genereted ='hello, nigga'# generate(theme)

        write_to_db = Data(theme=theme, genereted=genereted)
        db.session.add(write_to_db)        
        db.session.commit()     
        return str(genereted)


class GetData(Resource):
    def get(self):
        theme = request.args.get('theme')
        data = Data.query.filter_by(theme=theme).first()
        return data

api.add_resource(GetData, "/getdata/", "/getdata/<string:theme>")
api.add_resource(GenText, "/generate/", "/generate/<string:theme>")


def main():
    app.run()


if __name__ == '__main__':
    main()