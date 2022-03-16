# -*- coding: utf-8 -*-

from odoo import models, fields, api


class RentalManagement(models.Model):
    _name = 'rental_management'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'rental_management'

    name = fields.Char(string="Name", tracking=True)
    cust = fields.Many2one('res.partner', string="Customer", tracking=True)
    rental_type = fields.Many2one('rentaltype.rentaltype', string="Rental Type")
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")
    rental_product = fields.Many2one('product.product', string="Rental Product")
    price = fields.Float(string="Price")
    state = fields.Selection([("draft", "Draft"), ("waiting", "Waiting"), ("approve", "Approve"), ("cancle", "Cancle")])



    @api.depends('name')
    def click_by_name(self):
        display_msg = str(self.name)
        return self.message_post(body=display_msg)
