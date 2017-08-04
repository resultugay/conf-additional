from flask.blueprints import Blueprint
from flask.templating import render_template
from flask import  request,flash
from passlib import hash
import random
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from User import User
from datetime import datetime
from sqlalchemy import exc
from forms import LoginForm
from flask import Blueprint,  flash, redirect, render_template, url_for
from Abstract import get_abstract_id
from Decision import Decision

Base = declarative_base()    


engine = create_engine('postgresql://rsltgy:123456@localhost:5432/ubmk')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

''' 
# Insert a Person in the person table
new_person = Users(username='new person',email='ss',name='aa',surname='aa',password='testtt',salt='aa',gender = 'M')
session.add(new_person)
session.commit()
'''

sign_up = Blueprint('sign_up',__name__)
ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


@sign_up.route('/signup', methods=['GET', 'POST'])
def sign_up_page():
    if request.method == 'GET':
        return render_template("sign_up.html")
    else:
        username = request.form['reg_username']
        password = request.form['reg_password']
        #for the salt create 16 character long salt and use it for hash
        user_id = ""
        for i in range(16):
            user_id = user_id + (random.choice(ALPHABET))                
        #hashed_password = hash.sha512_crypt.using(salt=salt).hash(password)   
        hashed_password = hash.sha512_crypt.using(salt_size = 4).hash(password)     
        #k = hash.sha512_crypt.verify(password, hashed_password) for verifying hash        
        email    =  request.form['reg_email']
        name =  request.form['reg_name']
        surname =  request.form['reg_surname']   
        if request.form['reg_gender'] == "male":
            gender = 'M'
        else:
            gender = 'F'
        new_user = User(username=username,email=email,name=name,surname=surname,password=hashed_password,user_id=user_id,gender = gender,reg_date=datetime.now())
        session.add(new_user)
        
        
        '''Abstract decision  '''      
        abstracts = get_abstract_id()
        for abs in abstracts:
            new_decision = Decision(email,abs.abstract_id,None,None,None)
            session.add(new_decision)      
        
        try:
            session.commit()
            form = LoginForm()
            next_page = request.args.get('next', url_for('sign_in.sign_in_page'))
            return redirect(next_page)
        except exc.SQLAlchemyError:
            flash("Problem!!")
            session.rollback()   
            flash('Invalid Credentials')  
            return render_template("home.html")

