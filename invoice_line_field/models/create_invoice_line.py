from odoo import api, fields, models, _
from odoo.exceptions import UserError

class InvoiceLineModel(models.Model):
    _inherit = 'sale.order.line'

    def _prepare_invoice_line(self, **optional_values):

        self.ensure_one()

        res = {
            'display_type': self.display_type,
            'sequence': self.sequence,
            'name': self.name,
            'product_id': self.product_id.id,
            'product_uom_id': self.product_uom.id,
            'quantity': self.qty_to_invoice,
            'discount': self.discount,
            'price_unit': self.price_unit,
            'sqf': self.square_foot,
            'quality_id': self.quality_id.id,
            'tax_ids': [(6, 0, self.tax_id.ids)],
            'analytic_tag_ids': [(6, 0, self.analytic_tag_ids.ids)],
            'sale_line_ids': [(4, self.id)],
        }

        if self.order_id.analytic_account_id:
            res['analytic_account_id'] = self.order_id.analytic_account_id.id
        if optional_values:
            res.update(optional_values)
        if self.display_type:
            res['account_id'] = False
        return res


class InvoiceLineModel(models.Model):
    _inherit = 'account.move'

    def default_get(self, fields_list):
        for line in self.invoice_line_ids:
            line.update({'price_subtotal': line.sqf * line.price_unit})
        res = super(InvoiceLineModel, self).default_get(fields_list)
        return res
