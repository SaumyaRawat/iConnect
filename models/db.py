# -*- coding: utf-8 -*-

#########################################################################
## This scaffolding model makes your app work on Google App Engine too
## File is released under public domain and you can use without limitations
#########################################################################

## if SSL/HTTPS is properly configured and you want all HTTP requests to
## be redirected to HTTPS, uncomment the line below:
# request.requires_https()

## app configuration made easy. Look inside private/appconfig.ini
from gluon.contrib.appconfig import AppConfig
## once in production, remove reload=True to gain full speed
myconf = AppConfig(reload=True)


if not request.env.web2py_runtime_gae:
    ## if NOT running on Google App Engine use SQLite or other DB
    db = DAL(myconf.take('db.uri'), pool_size=myconf.take('db.pool_size', cast=int), check_reserved=['all'])
else:
    ## connect to Google BigTable (optional 'google:datastore://namespace')
    db = DAL('google:datastore+ndb')
    ## store sessions and tickets there
    session.connect(request, response, db=db)
    ## or store session in Memcache, Redis, etc.
    ## from gluon.contrib.memdb import MEMDB
    ## from google.appengine.api.memcache import Client
    ## session.connect(request, response, db = MEMDB(Client()))

## by default give a view/generic.extension to all actions from localhost
## none otherwise. a pattern can be 'controller/function.extension'
response.generic_patterns = ['*'] if request.is_local else []
## choose a style for forms
response.formstyle = myconf.take('forms.formstyle')  # or 'bootstrap3_stacked' or 'bootstrap2' or other
response.form_label_separator = myconf.take('forms.separator')


## (optional) optimize handling of static files
# response.optimize_css = 'concat,minify,inline'
# response.optimize_js = 'concat,minify,inline'
## (optional) static assets folder versioning
# response.static_version = '0.0.0'
#########################################################################
## Here is sample code if you need for
## - email capabilities
## - authentication (registration, login, logout, ... )
## - authorization (role based authorization)
## - services (xml, csv, json, xmlrpc, jsonrpc, amf, rss)
## - old style crud actions
## (more options discussed in gluon/tools.py)
#########################################################################

from gluon.tools import Auth, Service, PluginManager

auth = Auth(db)
service = Service()
plugins = PluginManager()

## create all tables needed by auth if not custom tables
auth.define_tables(username=False, signature=False)

## configure email
mail = auth.settings.mailer
mail.settings.server = 'logging' if request.is_local else myconf.take('smtp.sender')
mail.settings.sender = myconf.take('smtp.sender')
mail.settings.login = myconf.take('smtp.login')

## configure auth policy
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True

#########################################################################
## Define your tables below (or better in another model file) for example
##
## >>> db.define_table('mytable',Field('myfield','string'))
##
## Fields can be 'string','text','password','integer','double','boolean'
##       'date','time','datetime','blob','upload', 'reference TABLENAME'
## There is an implicit 'id integer autoincrement' field
## Consult manual for more options, validators, etc.
##
## More API examples for controllers:
##
## >>> db.mytable.insert(myfield='value')
## >>> rows=db(db.mytable.myfield=='value').select(db.mytable.ALL)
## >>> for row in rows: print row.id, row.myfield
db.define_table('person',
                Field('name', 'string', length=255, required=True),
                Field('dob', 'date', required=True),
                Field('gender', 'string', required=True),
                Field('maritialstatus', 'string', length=255, required=False, default=True),
                Field('country', 'string', length=255, required=True),
                Field('state', 'string', length=255, required=True),
                Field('city', 'string', length=255, required=True),
                Field('pincode', 'string', length=255, required=False),
                Field('aboutme', 'string', length=300, required=True),
                )
##db.define_table('females',
##                db.Field('name', 'string', length=255, required=True),
##               db.Field('dob', 'date', required=True),
##                db.Field('gender', 'string', required=True),
##                db.Field('maritialstatus', 'string', length=255, required=False, default=True),
##                db.Field('country', 'string', length=255, required=True),
##                db.Field('state', 'string', length=255, required=True),
##               db.Field('city', 'string', length=255, required=True),
##              db.Field('pincode', 'string', length=255, required=False),
##                db.Field('aboutme', 'text', required=True),
##                migrate='females.table')
######################################################################################################

db.define_table('appearance',
                Field('weight', 'string', length=255, required=True),
                Field('complexion', 'string', length=255, required=True),
                Field('bodytype', 'string', length=255, required=True),
                Field('height', 'string', length=255, required=True),
                Field('specialcase','string', required=True),
                )
db.define_table('edu',
                Field('highestqual', 'string', length=255, required=True),
                Field('college', 'string', required=False),
                Field('employed', 'string', required=True),
                Field('occupation', 'string', length=255, required=False),
                Field('company', 'string', length=255, required=False),
                Field('income', 'string', length=255, required=True),
                Field('income', 'string', length=255, required=True),
                Field('income', 'string', length=255, required=True),
                )
db.define_table('interest',
                Field('smoking', 'string', length=255, required=True),
                Field('drinking', 'string', required=True),
                Field('genre', 'string', required=False),
                Field('artists', 'string', length=255, required=False),
                Field('artists', 'string', length=255, required=False),
                Field('album', 'string', length=255, required=False),
                Field('song', 'string', length=255, required=False),
                Field('movie', 'string', length=255, required=False),
                Field('books', 'string', length=255, required=False),
                Field('dest', 'string', length=255, required=False),
                Field('dest', 'string', length=255, required=False),
                Field('dest', 'string', length=255, required=False),
                )
#ANJALI
#########################################################################

## after defining tables, uncomment below to enable auditing
# auth.enable_record_versioning(db)
