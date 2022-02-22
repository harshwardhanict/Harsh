from odoo import models, fields,api


class avish_wizard(models.TransientModel):
     _name = 'avish.wizard'

     name = fields.Char()
     PhoneNo=fields.Integer()
     Price = fields.Integer()
     Email=fields.Char()

     def Print(self):
         print("hax")