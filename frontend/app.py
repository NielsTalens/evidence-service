import json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import request, Response
from flask import render_template
from flask_bootstrap import Bootstrap
from sqlalchemy import text


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
    # print(get_fails())
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

    all_fails = get_fails()
    all_success = get_success()

    # print(all_fails)
    return render_template("index.html", len_e = len(all_evidence), all_evidence = all_evidence, len_c = len(all_controls), all_controls = all_controls, len_fail = len(all_fails), all_fails=all_fails, len_suc = len(all_success), all_success=all_success)

def get_fails():
    failed_controls = db.session.query(EvidenceModel).filter(EvidenceModel.control_id==ControlsModel.control_id).filter(EvidenceModel.retrieved_value!=ControlsModel.control_value).all()

    all_fails = [
        {
            "Description": fails.rule_description,
            "Control id": fails.control_id,
            "Retrieved value": fails.retrieved_value
        } for fails in failed_controls]
    return(all_fails)

def get_success():
    succeeded_controls = db.session.query(EvidenceModel).filter(EvidenceModel.control_id==ControlsModel.control_id).filter(EvidenceModel.retrieved_value==ControlsModel.control_value).all()
    all_success = [
        {
            "Description": success.rule_description,
            "Control id": success.control_id,
            "Retrieved value": success.retrieved_value
        } for success in succeeded_controls]
    return(all_success)


if __name__ == '__main__':
    app.run(use_reloader = True, debug = True)
