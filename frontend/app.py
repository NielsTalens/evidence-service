from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import request
from flask import render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)
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
class EvidenceModel(db.Model):
    __tablename__ = 'evidence'

    id = db.Column(db.Integer, primary_key=True)
    rule_description = db.Column(db.String())
    control_id = db.Column(db.String())
    retrieved_value = db.Column(db.Integer())

    def __init__(self, rule_description, control_id, retrieved_value):
        self.rule_description = rule_description
        self.control_id = control_id
        self.retrieved_value = retrieved_value

    def __repr__(self):
        return f"<Evidence {self.id}>"

@app.route('/')
def hello():
    return {"hello": "world"}

@app.route('/controls', methods=['GET'])
def handle_controls():
    request.method == 'GET'
    controls = ControlsModel.query.all()
    all_controls = [
        {
            "Control Id": control.control_id,
            "Description": control.control_description,
            "Value": control.control_value
        } for control in controls]

    evidences = EvidenceModel.query.all()
    all_evidence = [
      {
          "Control Id": evidence.rule_description,
          "Description": evidence.control_id,
          "Value": evidence.retrieved_value
      } for evidence in evidences]
  # return {"count": len(all_evidence), "evidence": all_evidence, "message": "success"}
    return render_template("index.html", len_e = len(all_evidence), all_evidence = all_evidence, len_c = len(all_controls), all_controls = all_controls)

  # return render_template("index.html", len_c = len(all_controls), all_controls = all_controls)


if __name__ == '__main__':
    app.run(use_reloader = True, debug = True)

#     @app.route('/evidence', methods=['GET'])
# def handle_evidence():
#   request.method == 'GET'
#   evidences = EvidenceModel.query.all()
#   all_evidence = [
#       {
#           "Control Id": evidence.rule_description,
#           "Description": evidence.control_id,
#           "Value": evidence.retrieved_value
#       } for evidence in evidences]
#   # return {"count": len(all_evidence), "evidence": all_evidence, "message": "success"}
#   return render_template("index.html", len = len(all_evidence), all_evidence = all_evidence)