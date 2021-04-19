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

@app.route('/', methods=['GET'])
def handle_controls():
    request.method == 'GET'
    controls = ControlsModel.query.all()
    all_controls = [
        {
            "Control Id": control.control_id,
            "Description": control.control_description,
            "Control value": control.control_value
        } for control in controls]

    evidences = EvidenceModel.query.all()
    all_evidence = [
      {
          "Description": evidence.rule_description,
          "Control id": evidence.control_id,
          "Retrieved value": evidence.retrieved_value
      } for evidence in evidences]

    # I think that it would be nicer to have this as a sql procedure
    checks_fail = []
    checks_succeed = []
    for evidence in all_evidence:
      for control in all_controls:
        if evidence['Control id'] == control['Control Id']:
          if evidence['Retrieved value'] != control['Control value']:
            checks_fail.append(evidence)
          else:
            checks_succeed.append(evidence)

    return render_template("index.html", len_e = len(all_evidence), all_evidence = all_evidence, len_c = len(all_controls), all_controls = all_controls, evidences=evidences, len_chf = len(checks_fail), checks_fail=checks_fail,len_chs = len(checks_succeed), checks_succeed=checks_succeed)

if __name__ == '__main__':
    app.run(use_reloader = True, debug = True)
