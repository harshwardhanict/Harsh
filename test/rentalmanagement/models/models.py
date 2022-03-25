# -*- coding: utf-8 -*-

from odoo import models, fields, api


class RentalManagement(models.Model):
    _name = 'rental_management'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'rental_management'
    _rec_name = 'name'

    name = fields.Char(string="Name", tracking=True, required=True)
    l_name = fields.Char(string="Surname", tracking=True)
    cust = fields.Many2one('res.partner', string="Customer", tracking=True)
    rental_type = fields.Many2one('rentaltype.rentaltype', string="Rental Type")
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")
    rental_product = fields.Many2one('product.product', string="Rental Product")
    price = fields.Float(string="Price")
    state = fields.Selection([("draft", "Draft"), ("waiting", "Waiting"), ("approve", "Approve"), ("cancle", "Cancle")])
    rental_info = fields.One2many('rental_person','person',string="Info")
    note = fields.Html()

    def name_get(self):
        result = []
        for rec in self:
            if not rec.l_name:
                result.append((rec.id, f"{rec.name}"))
            else:
                result.append((rec.id, f"{rec.name} - {rec.l_name}"))
        return result

    @api.depends('name')
    def click_by_name(self):
        display_msg = str(self.name)
        return self.message_post(body=display_msg)

    # @api.model
    # def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None):
    #     """
    #     this is method is for
    #     search with customer email,name and phone number
    #     """
    #     args = args or []
    #     domain = []
    #     print("insideeeeeeeeeeeeeeeeeeeeeeeeeee", self._context)
    #     if self._context.get('harsh'):
    #         cl = self.env['rental_management'].browse(self._context.get('harsh'))
    #         domain += [('id', 'in', cl.rental_management.ids)]
    #     return self._search(domain + args, limit=limit, access_rights_uid=name_get_uid)



class rental_person(models.Model):
    _name = 'rental_person'
    _description = 'rental_person'

    person = fields.Many2one('rental_management')
    p_name = fields.Char(string="Name")
    job = fields.Char(string="JOB")

