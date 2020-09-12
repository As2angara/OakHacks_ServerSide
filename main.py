from flask import Flask
from flask_restful import Resource, Api, reqparse, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
database = SQLAlchemy(app)


event_put_args = reqparse.RequestParser()
event_put_args.add_argument("name", type=str, help = "help id")
event_put_args.add_argument("description", type=str, help = "help id")
event_put_args.add_argument("meeting_link", type=str, help = "help id")
event_put_args.add_argument("donation_amount", type=float, help = "help id")
event_put_args.add_argument("event_date", type=str, help = "help id")
event_put_args.add_argument("user_id", type=int, help = "help id")


class EventModel(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(255), nullable=False)
    description = database.Column(database.String(255), nullable=False)
    meeting_link = database.Column(database.String(255), nullable=False)
    donation_amount = database.Column(database.Float(255), nullable=False)
    event_date = database.Column(database.String(255), nullable=False)
    user_id = database.Column(database.Integer, primary_key=False)

resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'description': fields.String,
    'meeting_link': fields.String,
    'donation_amount': fields.Float,
    'event_date': fields.String,
    'user_id': fields.Integer
}

database.create_all()

class Event(Resource):
    @marshal_with(resource_fields)
    def get(self, event_id):
        result = EventModel.query.filter_by(id=event_id).first()
        return result

    @marshal_with(resource_fields)
    def put(self, event_id):
        args = event_put_args.parse_args()
        new_event = EventModel(id=event_id, name=args["name"],
                               description=args["description"], meeting_link=args["meeting_link"],
                               donation_amount=args["donation_amount"], event_date=args["event_date"],
                               user_id=args['user_id'])
        database.session.add(new_event)
        database.session.commit()
        return new_event, 201

api.add_resource(Event,"/event/<int:event_id>")
if __name__ == "__main__":
    app.run(debug=True)