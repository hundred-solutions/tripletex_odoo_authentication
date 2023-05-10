from odoo import fields, models


class TripletexSessionToken(models.Model):
    _name = 'session.token'
    _description = "session token table"

    token = fields.Char()
    expire_date = fields.Date()
