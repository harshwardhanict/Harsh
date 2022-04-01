# -*- coding: utf-8 -*-

from odoo import models, fields, api


class rental(models.Model):
    _name = 'rental.rental'
    _description = 'rental.rental'

    name = fields.Char(string="Name")
    customer = fields.Many2one('res.partner', string="Customer")
    rental_type = fields.Many2one('res.partner', string="Rental Type")
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")
    rental_product = fields.Many2one('res.partner', string="Rental Product")
    price = fields.Float(string="Price")
    state = fields.Selection([("draft", "Draft"), ("waiting", "Waiting"), ("approve", "Approve"), ("cancle", "Cancle")])
