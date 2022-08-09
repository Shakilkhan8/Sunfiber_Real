from odoo import api, fields, models

class AccountMoveModelInherit(models.Model):
    _inherit = 'account.move'


class InvoiceInheritModel(models.Model):
    _inherit = 'account.move.line'

    quality_id = fields.Many2one("carpet.product.quality")
    discount = fields.Float('Discount')



class SaleAdvancePayment(models.TransientModel):
    _inherit = 'sale.advance.payment.inv'

    def _prepare_invoice_values(self, order, name, amount, so_line):
        res = super()._prepare_invoice_values(order, name, amount, so_line)
        for rec in res['invoice_line_ids']:
            rec_list = list(rec)
            rec_list[2]['quality_id'] = 1
        hh = 6
        return res

