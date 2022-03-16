from odoo import models, fields, api


class name_ref(models.Model):
    _inherit = 'res.partner'

    def name_get(self):
        result = []
        for rec in self:
            result.append((rec.id, f"{rec.name} - {rec.ref}"))
        return result




