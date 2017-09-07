from flask.blueprints import Blueprint
from flask.templating import render_template
from flask_login import current_user, login_required, login_user, logout_user
from Abstract import get_abstracts
from Abstract import get_abstracts2
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
from Session import get_sessions
from Abstract import Abstract
from Abstract import birinci_gun_13_1
from Abstract import birinci_gun_13_2
from Abstract import birinci_gun_13_3
from Abstract import birinci_gun_13_4
from Abstract import birinci_gun_13_5
from Abstract import birinci_gun_13_6
from Abstract import birinci_gun_13_7
from Abstract import birinci_gun_13_8
from Abstract import ikinci_gun_9_1
from Abstract import ikinci_gun_9_2
from Abstract import ikinci_gun_9_3
from Abstract import ikinci_gun_9_4
from Abstract import ikinci_gun_9_5
from Abstract import ikinci_gun_9_6
from Abstract import ikinci_gun_9_7
from Abstract import ikinci_gun_9_8
from Abstract import ikinci_gun_11_1
from Abstract import ikinci_gun_11_2
from Abstract import ikinci_gun_11_3
from Abstract import ikinci_gun_11_4
from Abstract import ikinci_gun_11_5
from Abstract import ikinci_gun_11_6
from Abstract import ikinci_gun_11_7
from Abstract import ikinci_gun_11_8
from Abstract import ikinci_gun_14_1
from Abstract import ikinci_gun_14_2
from Abstract import ikinci_gun_14_3
from Abstract import ikinci_gun_14_4
from Abstract import ikinci_gun_14_5
from Abstract import ikinci_gun_14_6
from Abstract import ikinci_gun_14_7
from Abstract import ikinci_gun_14_8



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
 
@home.route('/sessions',methods=['GET', 'POST'])
def session_page():
    if request.method == 'GET':
        abstracts = get_abstracts2() 
        sessions = get_sessions()        
        totalnumber = 0;
        for a in abstracts:
           totalnumber+=1
        return render_template("sessions.html",abstracts=abstracts,total_number_of_papers=totalnumber,sessions=sessions)
    else:
        
        
        
        session_list = request.form.getlist("sessions")

        
        for a in session_list:
            session.query(Abstract).filter_by(abstract_id = a.split(',')[0]).update({"session": a.split(',')[1]})

        session.commit()  
        
        
        abstracts = get_abstracts2() 
        totalnumber = 0;
        for a in abstracts:
           totalnumber+=1
        
         

        sessions = get_sessions()        

           
        return render_template("sessions.html",abstracts=abstracts,total_number_of_papers=totalnumber,sessions=sessions)      
      
      
@home.route('/program',methods=['GET', 'POST'])
def program_page():
    
        bir = birinci_gun_13_1()     
        iki = birinci_gun_13_2() 
        uc = birinci_gun_13_3() 
        dort = birinci_gun_13_4() 
        bes = birinci_gun_13_5() 
        alti = birinci_gun_13_6() 
        yedi = birinci_gun_13_7() 
        sekiz = birinci_gun_13_8() 
        
        iki_bir_bir = ikinci_gun_9_1()     
        iki_bir_iki = ikinci_gun_9_2() 
        iki_bir_uc = ikinci_gun_9_3() 
        iki_bir_dort = ikinci_gun_9_4() 
        iki_bir_bes = ikinci_gun_9_5() 
        iki_bir_alti = ikinci_gun_9_6() 
        iki_bir_yedi = ikinci_gun_9_7() 
        iki_bir_sekiz = ikinci_gun_9_8() 
        
        iki_iki_bir = ikinci_gun_11_1()     
        iki_iki_iki = ikinci_gun_11_2() 
        iki_iki_uc = ikinci_gun_11_3() 
        iki_iki_dort = ikinci_gun_11_4() 
        iki_iki_bes = ikinci_gun_11_5() 
        iki_iki_alti = ikinci_gun_11_6() 
        iki_iki_yedi = ikinci_gun_11_7() 
        iki_iki_sekiz = ikinci_gun_11_8() 
        
        iki_uc_bir = ikinci_gun_14_1()     
        iki_uc_iki = ikinci_gun_14_2() 
        iki_uc_uc = ikinci_gun_14_3() 
        iki_uc_dort = ikinci_gun_14_4() 
        iki_uc_bes = ikinci_gun_14_5() 
        iki_uc_alti = ikinci_gun_14_6() 
        iki_uc_yedi = ikinci_gun_14_7() 
        iki_uc_sekiz = ikinci_gun_14_8() 
        
           
        return render_template("program.html",bir=bir,iki=iki,uc=uc,dort=dort,bes=bes,alti=alti,yedi=yedi,sekiz=sekiz,
 
            iki_bir_bir          =      iki_bir_bir   , 
            iki_bir_iki          =      iki_bir_iki   ,
            iki_bir_uc          =       iki_bir_uc    ,
            iki_bir_dort          =     iki_bir_dort  ,
            iki_bir_bes          =      iki_bir_bes   ,
            iki_bir_alti          =     iki_bir_alti  ,
            iki_bir_yedi          =     iki_bir_yedi  ,
            iki_bir_sekiz          =    iki_bir_sekiz ,
            iki_iki_bir          =      iki_iki_bir   , 
            iki_iki_iki          =      iki_iki_iki   ,
            iki_iki_uc          =       iki_iki_uc    ,
            iki_iki_dort          =     iki_iki_dort  ,
            iki_iki_bes          =      iki_iki_bes   ,
            iki_iki_alti          =     iki_iki_alti  ,
            iki_iki_yedi          =     iki_iki_yedi  ,
            iki_iki_sekiz          =    iki_iki_sekiz , 
            iki_uc_bir          =       iki_uc_bir    , 
            iki_uc_iki          =       iki_uc_iki    ,
            iki_uc_uc          =        iki_uc_uc     ,
            iki_uc_dort          =      iki_uc_dort   ,
            iki_uc_bes          =       iki_uc_bes    ,
            iki_uc_alti          =      iki_uc_alti   ,
            iki_uc_yedi          =      iki_uc_yedi   ,
            iki_uc_sekiz          =     iki_uc_sekiz  ,)       