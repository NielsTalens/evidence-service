import json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import request, Response
from flask import render_template
from flask_bootstrap import Bootstrap
from sqlalchemy import text
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

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

    #evidences = relationship("EvidenceModel",backref="control")

    def __init__(self, control_id, control_description, control_value):
        self.control_id          = control_id
        self.control_description = control_description
        self.control_value       = control_value

    def __repr__(self):
        return f"<Control {self.control_id}>"

class EvidenceModel(db.Model):
    __tablename__ = 'evidence'

    evidence_id         = db.Column(db.Integer, primary_key=True)
    control_id          = db.Column(db.Integer(),ForeignKey('control.control_id'))
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
    # print(get_fails())
    control_list = ControlModel.query.all()
    all_controls = [
        {
             "Control Id"           : control.control_id
            ,"Control Description"  : control.control_description
            ,"Control Value"        : control.control_value
        } for control in control_list]

    evidence_list = EvidenceModel.query.all()

    all_evidence = [
        {
             "Evidence Id"           : evidence.evidence_id
            ,"Control Id"            : evidence.control_id
            ,"Evidence Value"        : evidence.evidence_value
        } for evidence in evidence_list]

    all_fails = get_fails()
    all_success = get_success()

    # print(all_fails)
    return render_template("index.html", len_e          = len(all_evidence)
                                       , all_evidence   = all_evidence
                                       , len_c          = len(all_controls)
                                       , all_controls   = all_controls
                                       , len_fail       = len(all_fails)
                                       , all_fails      = all_fails
                                       , len_suc        = len(all_success)
                                       , all_success    = all_success)

def get_fails(): 
    failed_controls = db.session.query(  EvidenceModel.control_id            \
                                        ,EvidenceModel.evidence_value        \
                                        ,ControlModel.control_description)   \
                                        .join(EvidenceModel, EvidenceModel.control_id == ControlModel.control_id)                                          \
                                        .filter(EvidenceModel.control_id     == ControlModel.control_id)            \
                                        .filter(EvidenceModel.evidence_value >  ControlModel.control_value).all()

    all_fails = [
        {
            "Description"     : fails.control_description,
            "Control id"      : fails.control_id,
            "Evidence value"  : fails.evidence_value
        } for fails in failed_controls]
    return(all_fails)

def get_success():
   # succeeded_controls = db.session.query(EvidenceModel)      
   #                                            \
   #                                     .filter(EvidenceModel.control_id     == ControlModel.control_id) \
   #                                     .filter(EvidenceModel.evidence_value <= ControlModel.control_value).all()

    succeeded_controls = db.session.query(  EvidenceModel.control_id                                                \
                                        ,EvidenceModel.evidence_value                                               \
                                        ,ControlModel.control_description)                                          \
                                        .join(EvidenceModel, EvidenceModel.control_id == ControlModel.control_id)   \
                                        .filter(EvidenceModel.control_id     == ControlModel.control_id)            \
                                        .filter(EvidenceModel.evidence_value <=  ControlModel.control_value).all()
    
    all_success = [
        {
            "Description"      : success.control_description,
            "Control id"       : success.control_id,
            "Evidence value"   : success.evidence_value
        } for success in succeeded_controls]
    return(all_success)


if __name__ == '__main__':
    app.run(use_reloader = True, debug = True)
