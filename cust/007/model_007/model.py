from odoo import models, fields, api


class model_007(models.Model):
    _name="station.info"
    # _inherit = ['station.station']
    # _description = 'model_007'

    age = fields.Integer()
    city = fields.Selection([("a","Ahmedabad"),('b',"Baroda"),('s',"Surat")])

# class added(models.Model):
#     _inherit = "inheritance_trial"
#
#     mobile=fields.Char()
#     email=fields.Char()
