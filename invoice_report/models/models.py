from odoo import api, fields, models


# class InvoiceReportModel(models.TransientModel):
#     _name = 'report.invoice_report.invoice_report_template_id'
#
#     def _get_report_values(self, docids, data=None):
#
#         inv = self.env['account.move'].search([('id', '=', docids)])
#         a = 0