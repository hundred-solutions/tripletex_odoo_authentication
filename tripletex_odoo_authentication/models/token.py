from odoo import fields, models


class TripletexSessionToken(models.Model):
    _name = 'session.token'

    token = fields.Char()
    expire_date = fields.Date()
