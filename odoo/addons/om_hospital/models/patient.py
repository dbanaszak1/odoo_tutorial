from odoo import api, fields, models
from pkg_resources import require


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = "Odoo practice model"

    name = fields.Char(string='Name', required = True)
    surname = fields.Char(string ='Surname', required = True)
    age = fields.Integer(string = "Age")
    is_child = fields.Boolean(string = "Patient is a child")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string = "Gender")
    