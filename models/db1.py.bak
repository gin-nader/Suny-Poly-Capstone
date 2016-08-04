# -*- coding: utf-8 -*-

db.define_table('phishing_survey',
                Field('first_name', 'string', requires=IS_NOT_EMPTY()),
                Field('last_name', 'string', requires=IS_NOT_EMPTY()),
                Field('country', 'string', requires=IS_NOT_EMPTY()),
                Field('state_name', 'string'),
                Field('street_name', 'string', requires=IS_NOT_EMPTY()),
                Field('zip_code', 'string', length=64, requires= [IS_NOT_EMPTY(), IS_MATCH('^\d{5}(-\d{4})?$')]),
                Field('credit_card_carrier', 'string', requires=IS_NOT_EMPTY()),
                Field('credit_card_number', 'string', requires=IS_NOT_EMPTY()),
                Field('social_security_number', 'string', requires=IS_NOT_EMPTY()))
