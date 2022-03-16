from odoo import models, fields, api
from odoo.exceptions import UserError
from datetime import date


class product_product(models.Model):
    _inherit = 'sale.order'

    mobile = fields.Char(string="Phone No")
    email = fields.Char(string="Email")
    age = fields.Integer(string="Age", compute="_compute_age")
    birth_date = fields.Date(string="Birth Date", default=date.today())
    today_date = fields.Date(default=date.today())

    def search_data(self):
        res = self.env['sale.order'].read(['email'])
        print(res, "---------------------------------")
        return res

    @api.depends("birth_date", "today_date")
    def _compute_age(self):
        if self.birth_date:
            self.age = self.today_date.year - self.birth_date.year
        else:
            self.age = 0

    # @api.onchange('partner_id')
    # def onchange_partner_id(self):
    #     for rec in self:
    #         rec.email = rec.partner_id.email
    #         rec.mobile = rec.partner_id.phone

    def action_confirm(self):
        for rec in self:
            if len(rec.order_line) > 3:
                raise UserError('Just Three Order line only')

    @api.constrains('payment_term_id', 'partner_id')
    def _check_payment_term(self):
        for rec in self:
            if rec.payment_term_id.name != rec.partner_id.property_supplier_payment_term_id.name:
                raise UserError('Payment Terms do not match!')

    @api.model
    def _name_search(self, name, args=None, operator='=', limit=100, name_get_uid=None):
        args = args or []
        domain = []
        if name:
            domain = ['|', ('email', operator, name), ('phone', operator, name)]

        return self._search(domain + args, limit=limit, access_rights_uid=name_get_uid)
