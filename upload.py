from werkzeug.utils import secure_filename
from flask import Blueprint, flash, redirect, render_template, url_for
from flask import send_from_directory
from sqlalchemy.ext.declarative.api import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_login.utils import current_user
from datetime import datetime
from sign_up import ALPHABET
from flask import request
import random
from sqlalchemy import exc
from Attachment import Attachment, get_attachment


Base = declarative_base()    


engine = create_engine('postgresql://rsltgy:123456@localhost:5432/ubmk')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

upload = Blueprint('upload',__name__)

@upload.route('/upload',  methods=['GET', 'POST'])
def upload_page():
    if request.method == 'POST':
        data = request.files['file'].read()
        abs_id = request.form['absid']
        session.query(Attachment).filter_by(abstracts_id = abs_id).update({"filecontent": data})
        session.commit()
        return redirect(url_for('home.home_page'))
        #attc = Attachment(attachment_id=412,abstracts_id=1558,filecontent=data,filename='ada.pdf',filetype='application/pdf',filesize='2141')
        try:
            session.commit()
            print("done")
            return redirect(url_for('home.home_page'))
        except exc.SQLAlchemyError:
            print("problem")
            session.rollback()
    return render_template("file_upload.html")


