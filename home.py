from flask.blueprints import Blueprint
from flask.templating import render_template
from flask_login import current_user, login_required, login_user, logout_user
from Abstract import get_abstracts
from Attachment import get_attachment
from flask import make_response
from flask import request
from flask import request

from sqlalchemy.ext.declarative.api import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_login.utils import current_user
from Decision import Decision,get_accept_decisions,get_poster_decisions,get_reject_decisions
from Decision import get_all_accept_decisions
from Decision import get_all_poster_decisions
from Decision import get_all_reject_decisions
from sqlalchemy.sql import func

Base = declarative_base()    


engine = create_engine('postgresql://rsltgy:123456@localhost:5432/ubmk')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

home = Blueprint('home',__name__)

@home.route('/',  methods=['GET', 'POST'])
def home_page():
    if request.method == 'GET':
      if current_user.is_authenticated:
        abstracts = get_abstracts() 
        totalnumber = 0;
        for a in abstracts:
           totalnumber+=1
          
           
        accept_decisions = get_accept_decisions(current_user.get_email())
        accept_decisions = [r[0] for r in accept_decisions] 
        
        poster_decisions = get_poster_decisions(current_user.get_email())
        poster_decisions = [r[0] for r in poster_decisions] 
        
        reject_decisions = get_reject_decisions(current_user.get_email())
        reject_decisions = [r[0] for r in reject_decisions] 
        return render_template("home.html",abstracts=abstracts,total_number_of_papers=totalnumber,accept_decisions=accept_decisions,poster_decisions=poster_decisions,reject_decisions=reject_decisions)
      else:
        return render_template("home.html")
    else:
        if current_user.is_authenticated:
          abstracts = get_abstracts() 
          totalnumber = 0;
          abs = []
          for a in abstracts:
            totalnumber+=1
            abs.append(int(a.abstract_id))
          
          all_accepts = request.form.getlist("accept")
          all_posters = request.form.getlist("poster")
          all_rejects = request.form.getlist("reject")
          
          
          for accept in abs:
              session.query(Decision).filter_by(user_email = current_user.get_email()).\
                                      filter_by(abstract_id = accept).update({"accept": 0})
              session.query(Decision).filter_by(user_email = current_user.get_email()).\
                                      filter_by(abstract_id = accept).update({"poster": 0})
              session.query(Decision).filter_by(user_email = current_user.get_email()).\
                                      filter_by(abstract_id = accept).update({"reject": 0})                                                                           
              
          for accept in all_accepts:
              session.query(Decision).filter_by(user_email = current_user.get_email()).\
                                      filter_by(abstract_id = accept).update({"accept": 1})

          for poster in all_posters:
              session.query(Decision).filter_by(user_email = current_user.get_email()).\
                                      filter_by(abstract_id = poster).update({"poster": 1})
              
          for reject in all_rejects:
              session.query(Decision).filter_by(user_email = current_user.get_email()).\
                                      filter_by(abstract_id = reject).update({"reject": 1})          
          session.commit()         
          
          accept_decisions = get_accept_decisions(current_user.get_email())
          accept_decisions = [r[0] for r in accept_decisions] 
        
          poster_decisions = get_poster_decisions(current_user.get_email())
          poster_decisions = [r[0] for r in poster_decisions] 
         
          reject_decisions = get_reject_decisions(current_user.get_email())
          reject_decisions = [r[0] for r in reject_decisions] 
          
          
          
          return render_template("home.html",abstracts=abstracts,total_number_of_papers=totalnumber,accept_decisions=accept_decisions,poster_decisions=poster_decisions,reject_decisions=reject_decisions)
        else:
          return render_template("home.html")


@home.route('/papers/<int:abs>')
@login_required
def paper_page(abs):
    attachment = get_attachment(abs)
    if attachment.filecontent is None:
        attachment = get_attachment(1500)
    response = make_response(attachment.filecontent)
    response.headers['Content-Type'] = 'application/pdf'
    return response




@home.route('/admin')
def admin_page():
      if current_user.is_authenticated:
        abstracts = get_abstracts() 
        totalnumber = 0;
        for a in abstracts:
           totalnumber+=1
         
           
        accept_decisions = get_accept_decisions(current_user.get_email())
        accept_decisions = [r[0] for r in accept_decisions] 
        
        poster_decisions = get_poster_decisions(current_user.get_email())
        poster_decisions = [r[0] for r in poster_decisions] 
        
        reject_decisions = get_reject_decisions(current_user.get_email())
        reject_decisions = [r[0] for r in reject_decisions] 

        all_accept = get_all_accept_decisions()
        all_poster = get_all_poster_decisions()
        all_reject = get_all_reject_decisions()        


        return render_template("admin.html",abstracts=abstracts,total_number_of_papers=totalnumber,accept_decisions=accept_decisions,poster_decisions=poster_decisions,reject_decisions=reject_decisions,all_accept=all_accept,all_poster=all_poster,all_reject=all_reject)
      else:
        return render_template("home.html")
    