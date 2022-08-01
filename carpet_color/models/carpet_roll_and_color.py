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
        ('Mix', 'Mix'),
        ('Print', 'Print'),
    ], required=True)

    delivery_confirm = fields.Selection([
        ('Non-Delivered', 'Non Delivered'),
        ('Delivered', 'Delivered'),
        ('One-Time', 'One Time'),
        ('Half-Paid', 'Half Paid')
    ], required=True)

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

                total += line.color_0 + line.color_1 + line.color_2 + line.color_3 + line.color_4 + line.color_5 + line.color_6 + line.color_7 + line.color_8 + line.color_9 + line.color_10 + line.color_11 + line.color_12 + line.color_13 + line.color_14 + line.color_15 + line.color_16 + line.color_17 + line.color_18 + line.color_19 + line.color_20 + line.color_21 + line.color_22 + line.color_23 + line.color_24 + line.color_25 + line.color_26 + line.color_27 + line.color_28 + line.color_29 + line.color_30 + line.color_31 + line.color_32 + line.color_33 + line.color_34 + line.color_35 + line.color_36 + line.color_37 + line.color_38 + line.color_39 + line.color_40 + line.color_41 + line.color_42 + line.color_43 + line.color_44 + line.color_45 + line.color_46 + line.color_47 + line.color_48 + line.color_1d + line.color_1l + line.color_1r + line.color_3d + line.color_3l + line.color_4l + line.color_5l + line.color_6l + line.color_6d + line.color_6m + line.color_7l + line.color_10d + line.color_11l + line.color_11r + line.color_12r + line.color_13l + line.color_14d + line.color_17r
                total_roll += line.color_0 + line.color_1 + line.color_2 + line.color_3 + line.color_4 + line.color_5 + line.color_6 + line.color_7 + line.color_8 + line.color_9 + line.color_10 + line.color_11 + line.color_12 + line.color_13 + line.color_14 + line.color_15 + line.color_16 + line.color_17 + line.color_18 + line.color_19 + line.color_20 + line.color_21 + line.color_22 + line.color_23 + line.color_24 + line.color_25 + line.color_26 + line.color_27 + line.color_28 + line.color_29 + line.color_30 + line.color_31 + line.color_32 + line.color_33 + line.color_34 + line.color_35 + line.color_36 + line.color_37 + line.color_38 + line.color_39 + line.color_40 + line.color_41 + line.color_42 + line.color_43 + line.color_44 + line.color_45 + line.color_46 + line.color_47 + line.color_48 + line.color_1d + line.color_1l + line.color_1r + line.color_3d + line.color_3l + line.color_4l + line.color_5l + line.color_6l + line.color_6d + line.color_6m + line.color_7l + line.color_10d + line.color_11l + line.color_11r + line.color_12r + line.color_13l + line.color_14d + line.color_17r

                # this is the formula for square feet calculation
                total_foot += total_roll * 36 * 3.281 * 12
                line.square_foot = total_foot

                # calculate total roll for sale order
                self.total_roll = total_roll

                # caculate total roll for order  line
                line.total_qty = total
                line.total_price = line.square_foot * line.price_unit - (
                        line.square_foot * line.price_unit * line.discount / 100)

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
                    if line.design_id.name == 'Digital Printed' or line.design_id.name == 'Tufted':
                        line.child_image = line.child_design_id.image
                    else:
                        line.child_image = False

                    # if both design and quality selected then we concatenate the both to create product name
                    if line.design_id and line.quality_id:
                        if line.design_id.name == 'Digital Printed' or line.design_id.name == 'Tufted':
                            line.product_id = line.design_id.name + " / " + line.child_design_id.name + " / " + line.quality_id.name
                        else:
                            line.product_id = line.design_id.name + " " + line.quality_id.name


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
    color_1r = fields.Integer("1R")
    color_1d = fields.Integer("1D")
    color_1l = fields.Integer("1L")
    color_2 = fields.Integer("2")
    color_3 = fields.Integer("3")
    color_3l = fields.Integer("3L")
    color_3d = fields.Integer("3D")
    color_4 = fields.Integer("4")
    color_4l = fields.Integer("4L")
    color_5 = fields.Integer("5")
    color_5l = fields.Integer("5L")
    color_6 = fields.Integer("6")
    color_6d = fields.Integer("6D")
    color_6m = fields.Integer("6M")
    color_6l = fields.Integer("6L")
    color_7 = fields.Integer("7")
    color_7l = fields.Integer("7L")
    color_8 = fields.Integer("8")
    color_9 = fields.Integer("9")
    color_10 = fields.Integer("10")
    color_10d = fields.Integer("10D")
    color_11 = fields.Integer("11")
    color_11r = fields.Integer("11R")
    color_11l = fields.Integer("11L")
    color_12 = fields.Integer("12")
    color_12r = fields.Integer("12R")
    color_13 = fields.Integer("13")
    color_13l = fields.Integer("13L")
    color_14 = fields.Integer("14")
    color_14d = fields.Integer("14D")
    color_15 = fields.Integer("15")
    color_16 = fields.Integer("16")
    color_17 = fields.Integer("17")
    color_17r = fields.Integer("17R")
    color_18 = fields.Integer("18")
    color_19 = fields.Integer("19")
    color_20 = fields.Integer("20")
    color_21 = fields.Integer("21")
    color_22 = fields.Integer("22")
    color_23 = fields.Integer("23")
    color_24 = fields.Integer("24")
    color_25 = fields.Integer("25")
    color_26 = fields.Integer("26")
    color_27 = fields.Integer("27")
    color_28 = fields.Integer("28")
    color_29 = fields.Integer("29")
    color_30 = fields.Integer("30")
    color_31 = fields.Integer("31")
    color_32 = fields.Integer("32")
    color_33 = fields.Integer("33")
    color_34 = fields.Integer("34")
    color_35 = fields.Integer("35")
    color_36 = fields.Integer("36")
    color_37 = fields.Integer("37")
    color_38 = fields.Integer("38")
    color_39 = fields.Integer("39")
    color_40 = fields.Integer("40")
    color_41 = fields.Integer("41")
    color_42 = fields.Integer("42")
    color_43 = fields.Integer("43")
    color_44 = fields.Integer("44")
    color_45 = fields.Integer("45")
    color_46 = fields.Integer("46")
    color_47 = fields.Integer("47")
    color_48 = fields.Integer("48")

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


class InheritSaleOrder(models.Model):
    _inherit = 'sale.order'

    def _create_invoices(self, grouped=False, final=False, date=None):
        res = super(InheritSaleOrder, self)._create_invoices(grouped, final)
        line_sum_up = []
        actual_line_dict = res.invoice_line_ids.read()
        o = 90
        existing_ids = res.invoice_line_ids.ids
        existing_line_ids = res.line_ids.ids
        for each_dict in actual_line_dict:
            dict_exist = next(
                (item for item in line_sum_up if item[2]['quality_id'][0] ==
                 each_dict['quality_id'][0]), None)
            if not dict_exist:
                each_dict['account_id'] = each_dict['account_id'][0]
                line_sum_up.append(((0, 0, each_dict)))
            else:
                dict_exist[2]['quantity'] += each_dict['quantity']
                dict_exist[2]['price_subtotal'] += each_dict['price_subtotal']
                dict_exist[2]['credit'] += each_dict['credit']
                dict_exist[2]['debit'] += each_dict['debit']

        # res.line_ids.unlink()
        res.invoice_line_ids = line_sum_up

        # we will remove the old id's data here

        # ids = set(res.invoice_line_ids.ids) - set(existing_ids)
        # o = res.write({'invoice_line_ids': next(iter(ids))})
        # for line in res.invoice_line_ids:
        #     if line.id in existing_ids:
        #         line.unlink()
        #
        # for line in res.line_ids:
        #     if line.id in existing_ids:
        #         line.unlink()
        return res


class StockMoveModel(models.Model):
    _inherit = 'stock.move.line'

    quality_id = fields.Many2one('carpet.product.quality')
    design_id = fields.Many2one('product.category')


class StockMoveModel(models.Model):
    _inherit = 'stock.move'

    quality_id = fields.Many2one('carpet.product.quality')
    design_id = fields.Many2one('product.category')
