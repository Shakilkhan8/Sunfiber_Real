from odoo import api, fields, models

class AccountMoveModelInherit(models.Model):
    _inherit = 'account.move'


    @api.model
    def create(self, vals_list):
        res = super(AccountMoveModelInherit, self).create(vals_list)
        order = self.env['sale.order'].search([('name', '=', res['invoice_origin'])])
        order.invoice_status = 'invoiced'
        return  res


class InvoiceInheritModel(models.Model):
    _inherit = 'account.move.line'

    quality_id = fields.Many2one("carpet.product.quality")
    discount = fields.Float('Discount')
    sqf = fields.Float('Sqf')


