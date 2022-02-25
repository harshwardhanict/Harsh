from odoo import models, fields,api


class harshwardhan_wizard(models.TransientModel):
     _name = 'harshwardhan.wizard'

     name = fields.Char()
     PhoneNo=fields.Integer()
     Price = fields.Integer()
     Email=fields.Char()

     def Print(self):
         print("hax")
