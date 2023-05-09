# -*- coding: utf-8 -*-
#############################################################################
#
#    Hundred Solutions
#
#    Copyright (C) 2023-TODAY Hundred Solutions(<https://www.hundredsolutions.com/>)
#    Author: www.hundredsolutions.com
#
#    You can modify it under the terms of the GNU AFFERO
#    GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#
#    You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
#    (AGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################

{
    'name': 'Tripletex Odoo Integration',
    'version': '16.0.1.0.0',
    'summary': """Odoo and Tripletex integration""",
    'author': "Hundred Solutions",
    'maintainer': 'Hundred Solutions',
    'company': "Hundred Solutions",
    'website': 'https://www.hundredsolutions.com/',
    'category': 'Customs',
    'description': """
    Helps You To work odoo and tripletex.
    """,
    'depends': [
        'base',
        'mail',
    ],
    'data': [
        'security/ir.model.access.csv',
        'wizard/session_token_create.xml',
        'views/credential.xml',
        'views/token.xml',
    ],
    'images': ['static/description/banner.png'],
    'license': 'AGPL-3',
    'installable': True,
    'application': True,
}
