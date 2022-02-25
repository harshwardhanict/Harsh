# -*- coding: utf-8 -*-

from odoo import models, fields, api


class department_wizard(models.Model):
    _name = 'department_wiz'
    _description = 'department_wiz'

    name = fields.Char(string='Name')
    enroll = fields.Integer(string='Enroll')
    user_id = fields.Many2many('res.partner.category', string='Users')

    def Print(self):
        print("Details are ADD")

    # def add_more(self):
    #     print("The More Details are ADD ")