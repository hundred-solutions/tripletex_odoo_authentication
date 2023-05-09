from odoo import models, fields


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    consumer_token = fields.Char(string='Consumer Token',
                                 config_parameter='tripletex_authentication.consumer_token',
                                 help='Enter your Consumer Token here.')
    employee_token = fields.Char(string='Employee Token',
                                 config_parameter='tripletex_authentication.employee_token',
                                 help='Enter your Employee Token here.')
