from odoo import api, fields, models
from odoo.exceptions import UserError
from odoo.exceptions import UserError

class CarpetColorModel(models.Model):
    _inherit = 'sale.order'

    color_line_id = fields.One2many('carpet.color.line', 'sale_order_id')
    currency_id = fields.Many2one('res.currency')
    total_price = fields.Monetary('Total Price', readonly=True, store=True)
    payment_received = fields.Boolean('Payment Received', default=False)
    customer_note = fields.Text('Customer Note')
    sub_customer = fields.Char('Sub Customer')
    order_type = fields.Selection([
        ('mix', 'Mix'),
        ('solid', 'Solid'),
        ('classic', 'Classic')
    ])

    delivery_confirm = fields.Selection([
        ('Yes', 'Yes'),
        ('No', 'No'),
        ('One Time', 'One Time'),
        ('Half', 'Half')
    ])

    total_roll = fields.Float('Total roll')




    # calculation of square feet in sale order line on the base of rolls and square feet formulla
    @api.onchange('order_line')
    def _onchange_oder_line(self):

        for rec in self.order_line:

            # calculation of sutotal on the base of price unit and square feet
            rec.price_subtotal = 0
            rec.price_subtotal = rec.square_foot * rec.price_unit

            rec.quality_id = rec.product_id.product_tmpl_id.carpet_quality_id.id
            rec.design_id = rec.product_id.product_tmpl_id.categ_id.id

            temp = self.env['product.template'].search([('id', '=', rec.product_id.product_tmpl_id.id)])
            if rec.product_uom_qty:
                if rec.product_id.digital_print_child:
                    rec.square_foot = rec.product_uom_qty * rec.product_id.product_tmpl_id.carpet_length * 3.281 * 12
                else:
                    rec.square_foot = rec.product_uom_qty * rec.product_id.product_tmpl_id.carpet_length * 3.281 * 12



    @api.onchange('color_line_id')
    def _onchange_line_color(self):
        for rec in self:
            order_total = 0

            for line in rec.color_line_id:

                total = 0
                total_foot = 0
                total_roll = 0
                # here we calculate total rolls for line

                total += line.color_0 + line.color_1 + line.color_2 + line.color_3 + line.color_4 + line.color_5 + line.color_6 + line.color_7 + line.color_8 + line.color_9 + line.color_10 + line.color_11 + line.color_12 + line.color_13 + line.color_14 + line.color_15 + line.color_16 + line.color_17 + line.color_18 + line.color_19 + line.color_20 +   line.color_1d + line.color_1r + line.color_3l + line.color_6d + line.color_6m + line.color_11r + line.color_13l + line.color_14d + line.color_17r
                total_roll += line.color_0 + line.color_1 + line.color_2 + line.color_3 + line.color_4 + line.color_5 + line.color_6 + line.color_7 + line.color_8 + line.color_9 + line.color_10 + line.color_11 + line.color_12 + line.color_13 + line.color_14 + line.color_15 + line.color_16 + line.color_17 + line.color_18 + line.color_19 + line.color_20 +   line. color_1d + line.color_1r + line.color_3l + line.color_6d + line.color_6m + line.color_11r + line.color_13l + line.color_14d + line.color_17r

                # this is the formula for square feet calculation
                total_foot += total_roll * 36 * 3.281  * 12
                line.square_foot = total_foot

                # calculate total roll for sale order
                self.total_roll = total_roll

                # caculate total roll for order  line
                line.total_qty = total
                line.total_price = line.square_foot * line.price_unit - (line.square_foot * line.price_unit * line.discount/100)

                # calculate line total price
                order_total += line.total_price
                self.total_price = order_total

                if line.design_id:
                    # if parent design is digital printed then we make child design required
                    if line.design_id.name == 'Digital Printed':
                        line.check_design = True
                    else:
                        line.check_design = False

                    # here we load the parent design image in order booking line
                    line.image = line.design_id.design_image

                    if line.child_design_id and line.design_id.name == 'Digital Printed':
                        line.child_image = line.child_design_id.image
                    else:
                        line.child_image = False

                    # if both design and quality selected then we concatenate the both to create product name
                    if line.design_id and line.quality_id:
                        if line.design_id.name == 'Digital Printed':
                            line.product_id = line.design_id.name + " / " + line.child_design_id.name + " / " + line.quality_id.name
                        else:
                            line.product_id = line.design_id.name  + " " + line.quality_id.name

class CarpetColorline(models.Model):
    _name = 'carpet.color.line'

    add_line_control = fields.Char()
    add_section_control = fields.Char()
    sequence = fields.Integer(string='Sequence', default=10)
    display_type = fields.Selection([
        ('line_section', "Section"),
        ('line_note', "Note")], default=False, help="Technical field for UX purpose.")


    square_foot = fields.Float('Square Foot')
    discount = fields.Float('Discount %')
    sale_order_id = fields.Many2one("sale.order")
    product_id = fields.Char("Product")
    design_id = fields.Many2one('product.category', required=True)
    child_design_id = fields.Many2one('digital.print.child', 'Child Design')
    child_image = fields.Binary('Child Image')
    check_design = fields.Boolean(default=False)
    quality_id = fields.Many2one('carpet.product.quality')
    color_0 = fields.Integer("0")
    color_1 = fields.Integer("1")
    color_2 = fields.Integer("2")
    color_3 = fields.Integer("3")
    color_4 = fields.Integer("4")
    color_5 = fields.Integer("5")
    color_6 = fields.Integer("6")
    color_7 = fields.Integer("7")
    color_8 = fields.Integer("8")
    color_9 = fields.Integer("9")
    color_10 = fields.Integer("10")
    color_11 = fields.Integer("11")
    color_12 = fields.Integer("12")
    color_13 = fields.Integer("13")
    color_14 = fields.Integer("14")
    color_15 = fields.Integer("15")
    color_16 = fields.Integer("16")
    color_17 = fields.Integer("17")
    color_18 = fields.Integer("18")
    color_19 = fields.Integer("19")
    color_20 = fields.Integer("20")
    color_1d = fields.Integer("1D")
    color_1r = fields.Integer("1R")
    color_3l = fields.Integer("3L")
    color_6d = fields.Integer("6D")
    color_6m = fields.Integer("6M")
    color_11r = fields.Integer("11R")
    color_13l = fields.Integer("13L")
    color_14d = fields.Integer("14D")
    color_17r = fields.Integer("17R")
    total_qty = fields.Integer('Total qty')
    price_unit = fields.Float('Price', store=True)
    total_price = fields.Integer('Total Price', readonly=True, store=True)
    image = fields.Binary("Image")
    product_name = fields.Char("Name")
    line_id = fields.Char('Line id')


class InheritSaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    quality_id = fields.Many2one('carpet.product.quality', 'Quality')
    design_id = fields.Many2one('product.category', 'Design')
    square_foot = fields.Float('Square Foot')
    delivered = fields.Date('Delivered')


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



class StockMoveModel(models.Model):
    _inherit = 'stock.move.line'

    quality_id = fields.Many2one('carpet.product.quality')
    design_id = fields.Many2one('product.category')


class StockMoveModel(models.Model):
    _inherit = 'stock.move'

    quality_id = fields.Many2one('carpet.product.quality')
    design_id = fields.Many2one('product.category')


