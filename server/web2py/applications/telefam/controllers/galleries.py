# coding: utf8

@auth.requires_login()
def index():
    """
    Index of galleries
    List of galleries and button to create a new one
    """
    items = db(db.galleries.telefam_id==session.telefam_id).select()
    return dict(items=items)


def edit():    
#    form = SQLFORM(db.galleries, request.args[0], submit_button='Send')
    crud.messages.submit_button = 'Change'
    crud.settings.update_next = URL('index')
    form = crud.update(db.galleries, request.args[0],deletable=True)
    return dict(form=form)


def new():
#    form = SQLFORM(db.galleries, submit_button='Send')
    crud.messages.submit_button = 'Send'
    form = crud.create(db.galleries)
    if form.process().accepted:
        response.flash = 'form accepted'
        redirect(URL('index'))
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill out the form'
    return dict(form=form)


def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request,db)



