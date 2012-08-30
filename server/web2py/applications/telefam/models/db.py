# -*- coding: utf-8 -*-

#########################################################################
## This scaffolding model makes your app work on Google App Engine too
## File is released under public domain and you can use without limitations
#########################################################################

## if SSL/HTTPS is properly configured and you want all HTTP requests to
## be redirected to HTTPS, uncomment the line below:
# request.requires_https()

if not request.env.web2py_runtime_gae:
    ## if NOT running on Google App Engine use SQLite or other DB
    db = DAL('sqlite:///home/alfem/alfem/prog/telefam/server/telefam.db')
else:
    ## connect to Google BigTable (optional 'google:datastore://namespace')
    db = DAL('google:datastore')
    ## store sessions and tickets there
    session.connect(request, response, db = db)
    ## or store session in Memcache, Redis, etc.
    ## from gluon.contrib.memdb import MEMDB
    ## from google.appengine.api.memcache import Client
    ## session.connect(request, response, db = MEMDB(Client()))

## by default give a view/generic.extension to all actions from localhost
## none otherwise. a pattern can be 'controller/function.extension'

#response.generic_patterns = ['*'] if request.is_local else []

response.generic_patterns = ['*.json'] 


## (optional) optimize handling of static files
# response.optimize_css = 'concat,minify,inline'
# response.optimize_js = 'concat,minify,inline'

#########################################################################
## Here is sample code if you need for
## - email capabilities
## - authentication (registration, login, logout, ... )
## - authorization (role based authorization)
## - services (xml, csv, json, xmlrpc, jsonrpc, amf, rss)
## - old style crud actions
## (more options discussed in gluon/tools.py)
#########################################################################

from gluon.tools import Auth, Crud, Service, PluginManager, prettydate
auth = Auth(db, hmac_key=Auth.get_or_create_key())
auth.settings.extra_fields['auth_user']= [
    Field('photo','upload',autodelete=True),
    Field('updated_on','datetime', default=request.now, update=request.now, readable=False, writable=False)]

crud, service, plugins = Crud(db), Service(), PluginManager()

## create all tables needed by auth if not custom tables
auth.define_tables()

## configure email
mail=auth.settings.mailer
mail.settings.server = 'smtp.el-magnifico.org'
mail.settings.sender = 'alfonso@el-magnifico.org'
mail.settings.login = 'alfonso:alfemi'

## configure auth policy
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True

## if you need to use OpenID, Facebook, MySpace, Twitter, Linkedin, etc.
## register with janrain.com, write your domain:api_key in private/janrain.key
#from gluon.contrib.login_methods.rpx_account import use_janrain
#use_janrain(auth,filename='private/janrain.key')

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
#########################################################################

db.define_table('telefams',
   Field('description',length=80),
   Field('user_id', db.auth_user, default=auth.user_id),
   Field('key', length=32),
   Field('last_connection', 'datetime'))
   
db.telefams.description.requires = IS_NOT_EMPTY()
db.telefams.user_id.requires = IS_IN_DB(db, db.auth_user.id)
db.telefams.user_id.readable = db.telefams.user_id.writable = False
db.telefams.last_connection.writable = False

db.define_table('messages',
   Field('user_id', db.auth_user, default=auth.user_id),
   Field('telefam_id', db.telefams, default=session.telefam_id),
   Field('text','text',length=512),
   Field('photo','upload',autodelete=True),
   Field('sound','upload'),
   Field('status', default="New"),
   Field('created_on', 'datetime', default=request.now),
   Field('read_on', 'datetime'),
   Field('updated_on', 'datetime', default=request.now)
   )

db.messages.user_id.requires = IS_IN_DB(db, db.auth_user.id)
db.messages.user_id.readable = db.messages.user_id.writable = False
db.messages.telefam_id.requires = IS_IN_DB(db, db.telefams.id)
db.messages.telefam_id.readable = db.messages.telefam_id.writable = False
db.messages.text.requires = IS_NOT_EMPTY()
db.messages.status.readable = db.messages.status.writable = False
db.messages.status.requires= IS_IN_SET(['New', 'Sent', 'Read'])
db.messages.user_id.readable = False
db.messages.telefam_id.readable = False
db.messages.created_on.writable = False
db.messages.read_on.writable = False
db.messages.updated_on.readable = db.messages.updated_on.writable = False
db.messages.updated_on.update=request.now

db.define_table('galleries',
   Field('user_id', db.auth_user, default=auth.user_id),
   Field('telefam_id', db.telefams, default=session.telefam_id),
   Field('description',length=80),
   Field('service', default="flickr"),
   Field('url',default="http://www.flickr.com/photos/..."),
   Field('status', default="New"),
   Field('created_on', 'datetime', default=request.now),
   Field('read_on', 'datetime'),
   Field('updated_on', 'datetime', default=request.now)
   )

db.galleries.user_id.requires = IS_IN_DB(db, db.auth_user.id)
db.galleries.user_id.readable = db.galleries.user_id.writable = False
db.galleries.telefam_id.requires = IS_IN_DB(db, db.telefams.id)
db.galleries.telefam_id.readable = db.galleries.telefam_id.writable = False
db.galleries.description.requires = IS_NOT_EMPTY()
db.galleries.service.requires= IS_IN_SET(['Flickr'])
db.galleries.status.readable = db.galleries.status.writable = False
db.galleries.status.requires= IS_IN_SET(['New', 'Sent', 'Read'])
db.galleries.user_id.readable = False
db.galleries.telefam_id.readable = False
db.galleries.created_on.writable = False
db.galleries.read_on.writable = False
db.galleries.updated_on.readable = db.galleries.updated_on.writable = False
db.galleries.updated_on.update=request.now

