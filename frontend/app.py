from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import request
from flask import render_template

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/ca_db"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class ControlsModel(db.Model):
    __tablename__ = 'controls'

    id = db.Column(db.Integer, primary_key=True)
    control_id = db.Column(db.String())
    control_description = db.Column(db.String())
    control_value = db.Column(db.Integer())

    def __init__(self, control_id, control_description, control_value):
        self.control_id = control_id
        self.control_description = control_description
        self.control_value = control_value

    def __repr__(self):
        return f"<Control {self.control_id}>"

@app.route('/')
def hello():
    return {"hello": "world"}

@app.route('/controls', methods=['POST', 'GET'])
def handle_controls():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            new_control = ControlsModel(control_id=data['control_id'], control_description=data['control_description'], control_value=data['control_value'])

            db.session.add(new_control)
            db.session.commit()

            return {"message": f"control {new_control.description} has been created successfully."}
        else:
            return {"error": "The request payload is not in JSON format"}

    elif request.method == 'GET':
        controls = ControlsModel.query.all()
        results = [
            {
                "Control Id": control.control_id,
                "Description": control.control_description,
                "Value": control.control_value
            } for control in controls]

        # for x in range(len(results)):
        #   print(results[x])
        # return {"count": len(results), "controls": results, "message": "success"}
        return render_template("index.html", len = len(results), results = results)

if __name__ == '__main__':
    app.run(use_reloader = True, debug = True)