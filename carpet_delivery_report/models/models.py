from odoo import api, fields, models


class DeliveryPackingModel(models.Model):
    _name = 'report.carpet_delivery_report.carpet_delivery_report'

    def _get_report_values(self, docids, data=None):
        order =  self.env['stock.picking'].browse(docids)

        lst_one = []
        lst_two = []
        count = 0
        for line in order.move_ids_without_package:

            count = count + 1
            if count != 20:
                lst_one.append({
                'design_name': line.design_id.name,
                'quality_name': line.quality_id.name,
                'color': line.color,
                'digital_design': 'Digital Printed' if line.design_id.name == 'Digital Printed' else None
            })
            if count > 2:
                lst_two.append({
                    'design_name': line.design_id.name,
                    'quality_name': line.quality_id.name,
                    'color': line.color,
                    'digital_design': 'Digital Printed' if line.design_id.name == 'Digital Printed' else None
                })

        return {
            'data_one': lst_one,
            'data_two': lst_two,
            'check': count,
            'order': order
        }
