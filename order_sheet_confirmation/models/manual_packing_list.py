from odoo import api, fields, models

class ManualPackingListModel(models.TransientModel):
    _name = 'report.order_sheet_confirmation.manual_packing_list_id'

    def _get_report_values(self, docids, data=None):
        order = self.env['sale.order'].browse(docids)
        lst = []
        data_list = []
        for item in order.color_line_id:
            if item.color_0 !=0:
                lst.append({
                    'color': '0',
                    'design_name': item.design_id.name,
                    'quality_id': item.quality_id.name,
                })

            if item.color_1 !=0:
                lst.append({
                    'color':'1',
                    'design_name': item.design_id.name,
                    'quality_id': item.quality_id.name,
                })
            if item.color_2 !=0:
                lst.append({
                    'color': '2',
                    'design_name': item.design_id.name,
                    'quality_id': item.quality_id.name,
                })
            if item.color_3 !=0:
                lst.append({
                    'color': '3',
                    'design_name': item.design_id.name,
                    'quality_id': item.quality_id.name,
                })
            if item.color_4 !=0:
                lst.append({
                    'color': '4',
                    'design_name': item.design_id.name,
                    'quality_id': item.quality_id.name,
                })
            if item.color_5 !=0:
                lst.append({
                    'color': '5',
                    'design_name': item.design_id.name,
                    'quality_id': item.quality_id.name,
                })
            if item.color_6 !=0:
                lst.append({
                    'color': '6',
                    'design_name': item.design_id.name,
                    'quality_id': item.quality_id.name,
                })
            if item.color_7 !=0:
                lst.append({
                    'color': '7',
                    'design_name': item.design_id.name,
                    'quality_id': item.quality_id.name,
                })
            if item.color_8 !=0:
                lst.append({
                    'color': '8',
                    'design_name': item.design_id.name,
                    'quality_id': item.quality_id.name,
                })
            if item.color_9 !=0:
                lst.append({
                    'color': '9',
                    'design_name': item.design_id.name,
                    'quality_id': item.quality_id.name,
                })
            if item.color_10 !=0:
                lst.append({
                    'color': '10',
                    'design_name': item.design_id.name,
                    'quality_id': item.quality_id.name,
                })
            if item.color_11 !=0:
                lst.append({
                    'color': '11',
                    'design_name': item.design_id.name,
                    'quality_id': item.quality_id.name,
                })
            if item.color_12 !=0:
                lst.append({
                    'color': '12',
                    'design_name': item.design_id.name,
                    'quality_id': item.quality_id.name
                })

            if item.color_13 !=0:
                lst.append({
                    'color': '13',
                    'design_name': item.design_id.name,
                    'quality_id': item.quality_id.name
                })
            if item.color_14 !=0:
                lst.append({
                    'color': '14',
                    'design_name': item.design_id.name,
                    'quality_id': item.quality_id.name
                })
            if item.color_15 !=0:
                lst.append({
                    'color': '15',
                    'design_name': item.design_id.name,
                    'quality_id': item.quality_id.name
                })
            if item.color_16 !=0:
                lst.append({
                    'color': '16',
                    'design_name': item.design_id.name,
                    'quality_id': item.quality_id.name
                })
            if item.color_17 !=0:
                lst.append({
                    'color': '17',
                    'design_name': item.design_id.name,
                    'quality_id': item.quality_id.name
                })
            if item.color_18 !=0:
                lst.append({
                    'color': '18',
                    'design_name': item.design_id.name,
                    'quality_id': item.quality_id.name
                })
            if item.color_19 !=0:
                lst.append({
                    'color': '19',
                    'design_name': item.design_id.name,
                    'quality_id': item.quality_id.name
                })
            if item.color_20 !=0:
                lst.append({
                    'color': '20',
                    'design_name': item.design_id.name,
                    'quality_id': item.quality_id.name
                })
            if item.color_1d !=0:
                lst.append({
                    'color': '1d',
                    'design_name': item.design_id.name,
                    'quality_id': item.quality_id.name
                })
            if item.color_1r !=0:
                lst.append({
                    'color': '1r',
                    'design_name': item.design_id.name,
                    'quality_id': item.quality_id.name
                })
            if item.color_3l !=0:
                lst.append({
                    'color': '3l',
                    'design_name': item.design_id.name,
                    'quality_id': item.quality_id.name
                })
            if item.color_6d !=0:
                lst.append({
                    'color': '6d',
                    'design_name': item.design_id.name,
                    'quality_id': item.quality_id.name
                })
            if item.color_6m !=0:
                lst.append({
                    'color': '6m',
                    'design_name': item.design_id.name,
                    'quality_id': item.quality_id.name
                })
            if item.color_11r !=0:
                lst.append({
                    'color': '11r',
                    'design_name': item.design_id.name,
                    'quality_id': item.quality_id.name
                })
            if item.color_13l !=0:
                lst.append({
                    'color': '13l',
                    'design_name': item.design_id.name,
                    'quality_id': item.quality_id.name
                })
            if item.color_14d !=0:
                lst.append({
                    'color': '14d',
                    'design_name': item.design_id.name,
                    'quality_id': item.quality_id.name
                })
            if item.color_17r !=0:
                lst.append({
                    'color': '17r',
                    'design_name': item.design_id.name,
                    'quality_id': item.quality_id.name
                })


        return {
            'data': lst
        }






