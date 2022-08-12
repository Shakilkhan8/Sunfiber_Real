from odoo import api, fields, models

class AccountMoveModelInherit(models.Model):
    _inherit = 'account.move'


class InvoiceInheritModel(models.Model):
    _inherit = 'account.move.line'

    quality_id = fields.Many2one("carpet.product.quality")
    discount = fields.Float('Discount')
    sqf = fields.Float('Sqf')


