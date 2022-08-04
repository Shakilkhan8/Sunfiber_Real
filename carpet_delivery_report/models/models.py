from odoo import api, fields, models


class DeliveryPackingModel(models.Model):
    _name = 'report.carpet_delivery_report.carpet_delivery_report'

    def _get_report_values(self, docids, data=None):
        order =  self.env['stock.picking'].browse(docids)

        data = []
        count = 0
        for line in order.move_ids_without_package:

            if count != 20:
                data.append({
                'design_name': line.design_id.name,
                'quality_name': line.quality_id.name,
                'color': line.color,
                'length': line.length,
                'width': line.width,
                'color': line.product_id.carpet_color,
            })


        return {
            'record1': data,
            'check': count,
            'order': order
        }
