from odoo import models, fields, api


class rental_type(models.Model):
    _name = 'rental_type'
    _description = 'rental_type'

    name = fields.Char(string="Name")
    code = fields.Char(string="Code")
    description = fields.Char(string="Description")