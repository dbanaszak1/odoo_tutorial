# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Hospital',
    'author': 'dbanaszak',
    'website': 'www.test.test',
    'summary': "Odoo 16",
    'installable': True,
    'application': True,
    'auto_install': False,
    'depends': ['mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/patient.xml',
    ]
}