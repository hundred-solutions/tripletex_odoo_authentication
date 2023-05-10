
from odoo import fields, models,_
import requests
from odoo.exceptions import UserError


class SessionTokenWizard(models.TransientModel):
    _name = 'token.wizard'
    _description = "token.wizard here is a wizard"

    expire_date = fields.Date()

    def session_token_generate(self):
        base_url = 'http://api.tripletex.io/v2'
        consumer_token = self.env['ir.config_parameter'].sudo().get_param('tripletex_authentication.consumer_token')
        employee_token = self.env['ir.config_parameter'].sudo().get_param('tripletex_authentication.employee_token')
        expiration_date = self.expire_date
        date = expiration_date.strftime('%Y-%m-%d')
        params = {'consumerToken': consumer_token, 'employeeToken': employee_token, 'expirationDate': date}
        r = requests.put(f'{base_url}/token/session/:create', params=params)
        token_data = self.env['session.token'].search([])
        if r.status_code == 200:
            response_data = r.json()
            if token_data:
                token_data.write({
                        'expire_date': response_data['value']['expirationDate'],
                        'token': response_data['value']['token']
                    })
            else:
                self.env['tripletex.token'].create({
                    'expire_date': response_data['value']['expirationDate'],
                    'token': response_data['value']['token']
                })
        else:
            raise UserError(_("Not Valid"))

