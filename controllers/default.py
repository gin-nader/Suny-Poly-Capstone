# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
#########################################################################


@auth.requires_login()
def index():


    return locals()

@auth.requires_login()
def survey():
    form = SQLFORM(db.phishing_survey).process()
    if form.accepted:
        session.flash = "Success!"
        redirect(URL('survey_result'))
    return locals()

@auth.requires_login()
def survey_result():
    for row in db().select(
        db.phishing_survey.ALL, db.auth_user.ALL):
        print row
    return locals()

@auth.requires_login()
def hashing():
    return locals()

@auth.requires_login()
def phishing():
    return dict()

@auth.requires_login()
def keylogger():
    return locals()

def register():
    return dict(form=auth.register())

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()
