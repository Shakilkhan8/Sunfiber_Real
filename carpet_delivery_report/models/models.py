from odoo import api, fields, models


class DeliveryPackingModel(models.Model):
    _name = 'report.carpet_delivery_report.carpet_delivery_report'

    def _get_report_values(self, docids, data=None):
        order =  self.env['stock.picking'].browse(docids)

        data = []

        for line in order.move_ids_without_package:

                data.append({
                'design_name': line.product_id.name,
                'quality_name': line.quality_id.name,
                'child_design': line.product_id.digital_print_child.name if line.product_id.digital_print_child.name else '-',
                'length': line.product_id.carpet_length,
                'width': line.product_id.carpet_width,
                'color': line.product_id.carpet_color,
                'grade': line.product_id.carpet_grade_id.name,
            })


        return {
            'record1': data,
            'order': order,
            'number': order.name,
            'order_number': order.origin,
        }
