import requests

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
            'price_subtotal': 909909090,
            'sqf': self.square_foot,
            'quality_id': self.quality_id.id,
            'tax_ids': [(6, 0, self.tax_id.ids)],
            'analytic_tag_ids': [(6, 0, self.analytic_tag_ids.ids)],
            'sale_line_ids': [(4, self.id)],
        }
        return res


class InvoiceLineModel(models.Model):
    _inherit = 'account.move'

    def default_get(self, fields_list):
        total = 0
        for line in self.invoice_line_ids:
            line.update({'price_subtotal': line.sqf * line.price_unit})
            total +=line.price_unit * line.sqf
            self.update({
                'amount_untaxed': total,
                'amount_total': total,
            })
        res = super(InvoiceLineModel, self).default_get(fields_list)
        return res


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    price_subtotal = fields.Monetary(string='Subtotal', store=True, readonly=True,
                                     currency_field='currency_id')
    sqf = fields.Float('SQ Feet', compute='_compute_sqf',  store=True)

    @api.depends('quantity')
    def _compute_sqf(self):
        total_feet = 0
        price_sub = 0
        for line in self:
            total_feet += line.quantity * line.product_id.carpet_length * 12 * 3.281
            line.sqf = total_feet
            line.price_subtotal = line.sqf * line.price_unit

    @api.onchange('quantity', 'discount', 'price_unit', 'tax_ids')
    def _onchange_price_subtotal(self):
        res = super(AccountMoveLine, self)._onchange_price_subtotal()
        sub_total = 0
        total_feet = 0
        for line in self:
            total_feet += line.quantity * line.product_id.carpet_length * 12 * 3.281
            line.sqf = total_feet
            line.price_subtotal = line.sqf * line.price_unit
            sub_total += line.sqf * line.price_unit
            line.price_subtotal = sub_total

        return res








