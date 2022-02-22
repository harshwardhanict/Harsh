# -*- coding: utf-8 -*-

from odoo import models, fields, api


class harshwardhan(models.Model):
    _name = 'harshwardhan.harshwardhan'
    _description = 'harshwardhan.harshwardhan'

    name = fields.Char()
    Email = fields.Char()
    Price = fields.Float(compute="_value_pc", store=True)
    PhoneNo=fields.integer()
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
