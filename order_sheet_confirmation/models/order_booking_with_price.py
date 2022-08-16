from odoo import api, fields, models

class CarpetColorReport(models.AbstractModel):
    _name = 'report.order_sheet_confirmation.order_booking_with_price'

    def _get_report_values(self, docids, data=None):
        order = self.env['sale.order'].browse(docids)
        domain = [('color_0', '!=',0), ('color_1', '!=',0), ('color_2', '!=',0), ('color_3', '!=',0), ('color_4', '!=',0), ('color_5', '!=',0), ('color_6', '!=',0), ('color_7', '!=',0), ('color_8', '!=',0), ('color_9', '!=',0), ('color_10', '!=',0), ('color_12', '!=',0), ('color_0', '!=',0)]
        lst = []
        check = 0
        comp = self.env['res.company'].search([])
        for rec in order:
            for line in rec.color_line_id:
                if line.child_image:
                    check = 1
                lst.append({

                    'product_name': line.product_id,
                    'color_0': line.color_0,
                    'color_1': line.color_1,
                    'color_1d': line.color_1d,
                    'color_1l': line.color_1l,
                    'color_1r': line.color_1r,
                    'color_2': line.color_2,
                    'color_3': line.color_3,
                    'color_3d': line.color_3d,
                    'color_3l': line.color_3l,
                    'color_4': line.color_4,
                    'color_4l': line.color_4l,
                    'color_5': line.color_5,
                    'color_5l': line.color_5l,
                    'color_6': line.color_6,
                    'color_6d': line.color_6d,
                    'color_6l': line.color_6l,
                    'color_6m': line.color_6m,
                    'color_7': line.color_7,
                    'color_7l': line.color_7l,
                    'color_8': line.color_8,
                    'color_9': line.color_9,
                    'color_10': line.color_10,
                    'color_10d': line.color_10d,
                    'color_11': line.color_11,
                    'color_11r': line.color_11r,
                    'color_11l': line.color_11l,
                    'color_12': line.color_12,
                    'color_12r': line.color_12r,
                    'color_13': line.color_13,
                    'color_13l': line.color_13l,
                    'color_14': line.color_14,
                    'color_14d': line.color_14d,
                    'color_15': line.color_15,
                    'color_16': line.color_16,
                    'color_17': line.color_17,
                    'color_17r': line.color_17r,
                    'color_18': line.color_18,
                    'color_19': line.color_19,
                    'color_20': line.color_20,
                    'color_21': line.color_21,
                    'color_22': line.color_22,
                    'color_23': line.color_23,
                    'color_24': line.color_24,
                    'color_25': line.color_25,
                    'color_26': line.color_26,
                    'color_27': line.color_27,
                    'color_28': line.color_28,
                    'color_29': line.color_29,
                    'color_30': line.color_30,
                    'color_31': line.color_31,
                    'color_32': line.color_32,
                    'color_33': line.color_33,
                    'color_34': line.color_34,
                    'color_35': line.color_35,
                    'color_36': line.color_36,
                    'color_37': line.color_37,
                    'color_38': line.color_38,
                    'color_39': line.color_39,
                    'color_40': line.color_40,
                    'color_41': line.color_41,
                    'color_42': line.color_42,
                    'color_43': line.color_43,
                    'color_44': line.color_44,
                    'color_45': line.color_45,
                    'color_46': line.color_46,
                    'color_47': line.color_47,
                    'color_48': line.color_48,
                    # 'digital_print': line.design_id.name,
                    'total_qty': line.total_qty,
                    'image': line.image,
                    'total_price': line.total_price,
                    'discount': line.discount,
                    'square_foot': line.square_foot,
                    'price_unit': line.price_unit,
                    'child_image': line.child_image,
                })

        return {
            'data': lst,
            'customer_name':  order.partner_id.name,
            'customer_note': order.customer_note,
            'sub_customer': order.sub_customer,
            'order_date': order.date_order,
            'delivery_confirm': order.delivery_confirm,
            'check': check,
            'number': order.name,

        }