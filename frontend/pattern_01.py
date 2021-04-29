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

class ControlModel(db.Model):
    __tablename__ = 'control'

    control_id          = db.Column(db.Integer, primary_key=True)
    control_description = db.Column(db.String())
    control_value       = db.Column(db.Integer())

    def __init__(self, control_id, control_description, control_value):
        self.control_id          = control_id
        self.control_description = control_description
        self.control_value       = control_value

    def __repr__(self):
        return f"<Control {self.control_id}>"

class EvidenceModel(db.Model):
    __tablename__ = 'evidence'

    evidence_id         = db.Column(db.Integer, primary_key=True)
    control_id          = db.Column(db.Integer())
    evidence_value      = db.Column(db.Integer())

    def __init__(self, evidence_id, control_id, evidence_value):
        self.evidence_id          = evidence_id
        self.control_id           = control_id
        self.evidence_value       = evidence_value

    def __repr__(self):
        return f"<Evidence {self.id}>"

@app.route('/', methods=['GET'])
def handle_controls():
    request.method == 'GET'
    control_table = ControlModel.query.all()
    all_control = [
        {
            "Control Id"           : control.control_id,
            "Control Description"  : control.control_description,
            "Control Value"        : control.control_value
        } for control in control_table]

    evidence_table = EvidenceModel.query.all()
    all_evidence = [
      {
          "Evidence Id"       : evidence.rule_description,
          "Control Id"        : evidence.control_id,
          "Evidence Value"    : evidence.evidence_value
      } for evidence in evidence_table]

    controls_fail = []
    controls_succeed = []
    for evidence in all_evidence:
      for control in all_control:
        if evidence['Control Id'] == control['Control Id']:
          if evidence['Evidence value'] > control['Control value']:
            controls_fail.append(evidence)
          else:
            controls_succeed.append(evidence)

    return render_template("index.html", len_e = len(all_evidence), all_evidence = all_evidence, len_c = len(all_control), all_control = all_control, evidence=evidence, len_chf = len(controls_fail), controls_fail=controls_fail,len_chs = len(controls_succeed), controls_succeed=controls_succeed)

  # return render_template("index.html", len_c = len(all_control), all_controls = all_control)


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