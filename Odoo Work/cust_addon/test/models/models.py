# -*- coding: utf-8 -*-

from odoo import models, fields, api


class test(models.Model):
    _name = 'test.test'
    _description = 'test.test'

    name = fields.Char()
    Email = fields.Char()
    Price =fields.Integer()
    Gts=fields.Float(compute="_value_pc", store=True)
    PhoneNo=fields.Integer()
    description = fields.Text()

    @api.depends('Price')
    def _value_pc(self):
        for record in self:
            record.Gts = float(record.Price) / 100
