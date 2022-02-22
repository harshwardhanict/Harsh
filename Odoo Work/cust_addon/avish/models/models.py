# -*- coding: utf-8 -*-

from odoo import models, fields, api


class avish(models.Model):
     _name = 'avish.avish'
     _description = 'avish.avish'

     name = fields.Char()
     PhoneNo=fields.Integer()
     Price = fields.Integer()
     Email=fields.Char()
     Gender=fields.Selection([("girl","Female"),("boy","Male")])
     value = fields.Float(compute="_value_pc", store=True)
     Profile=fields.Binary()
     description = fields.Text()
     partner_id=fields.Many2one()

     @api.depends('Price')
     def _value_pc(self):
         for record in self:
             record.value = float(record.Price) / 10
