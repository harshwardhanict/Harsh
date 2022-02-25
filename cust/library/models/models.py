# -*- coding: utf-8 -*-

from odoo import models, fields, api


class library(models.Model):
     _name = 'library.library'
     _description = 'library.library'

     name = fields.Char()
     value = fields.Integer()
     image=fields.Binary(string='Image')
     stat = fields.Selection([('application','Application'),('confirm','Confirm')],string='Status',index=True,readonly=True)


