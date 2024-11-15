from odoo import api, fields, models
from pkg_resources import require


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = 'mail.thread'
    _description = "Odoo practice model"

    name = fields.Char(string='Name', required = True, tracking = True)
    surname = fields.Char(string ='Surname', required = True, tracking = True)
    age = fields.Integer(string = "Age", tracking = True)
    is_child = fields.Boolean(string = "Patient is a child")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string = "Gender")

    @api.onchange('age')
    def  onchange_age(self):
        if self.age < 18:
            self.is_child = True
        else:
            self.is_child = False