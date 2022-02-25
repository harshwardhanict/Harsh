# -*- coding: utf-8 -*-

from odoo import models, fields, api


class department(models.Model):
    _name = 'department.department'
    _description = 'department.department'

    name = fields.Char()
    marks = fields.Integer()
    fee = fields.Float()
    description = fields.Text()

    def website(self):
        # print("button is click")
        return {
            'name': 'smart button',
            'domain': [],
            'view_type': 'form',
            'res_model': 'station.station',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window'
        }
