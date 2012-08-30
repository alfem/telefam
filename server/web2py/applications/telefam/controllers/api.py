# coding: utf8

import datetime

def call():
    """
    Returns status of changes to a Telefam device
    """
    session.forget()
    return service()

def get_telefam_by_key(key):
    telefams=db(db.telefams.key==key).select()
    if len(telefams) != 1:
      return False
    else:
      return telefams[0]

@service.json
def update_last_connection(key):
    now=datetime.datetime.now()
    db(db.telefams.key==key).update(last_connection=now)
    return now

@service.json
def get_status(key):
# if provided key is invalid then return nothing (note: choose a long key to avoid brute force attacks)
    telefam=get_telefam_by_key(key)
    if not telefam:
        return 

    status={}

    status['messages']=db((db.messages.telefam_id==telefam.id) & (db.messages.updated_on > telefam.last_connection)).count()

    status['galleries']=db((db.galleries.telefam_id==telefam.id) & (db.galleries.updated_on > telefam.last_connection)).count()

    return status

# Returns a list of available messages since last conection
@service.json
def get_message_list(key):
    telefam=get_telefam_by_key(key)
    if not telefam:
        return 

    messages_since_last_connection=db((db.messages.telefam_id==telefam.id) & (db.messages.updated_on >= telefam.last_connection)).select(db.messages.id, orderby=db.messages.updated_on)

    return messages_since_last_connection

# Returns a message (avoiding strange fields)
@service.json
def get_message(key, id):
    telefam=get_telefam_by_key(key)
    if not telefam:
        return 

    record=db.messages(id)

    record_dict={}
    for key,value in record.iteritems():
        if key not in ("update_record", "delete_record"):
            record_dict[key]=value

    return record_dict

