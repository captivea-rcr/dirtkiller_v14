# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError ,Warning

class PrintChequeReportWizard(models.TransientModel):
	_name = 'dynamic.cheque.report.wizard'
	_description = "Print Dynamic Cheque Report"

	@api.model
	def default_get(self, fields):
		res = super(PrintChequeReportWizard, self).default_get(fields)
		cheque_format_id = self.env['dynamic.cheque'].search([], limit=1)
		res.update({'cheque_format': cheque_format_id.id})
		return res

	cheque_format = fields.Many2one('dynamic.cheque', string='Cheque Format', required = True)
	next_check_number = fields.Integer('Next Check Number', required=True)
	# payment_id 	= fields.Many2one('account.payment', string='Payment Id')


	def print_dynamic_cheque_report(self):
		data = self.read()
		datas = {
			 'ids': self._context.get('active_ids',[]),
			 'model': 'account.payment',
			 'form': data
		}
		self._create_paper_format()
		return self.env.ref('generate_dynamic_cheque_app.dynamic_cheque_print_report_action_wiz').report_action(self, datas)

	@api.model
	def _create_paper_format(self):
		report_action_id = self.env['ir.actions.report'].search([('report_name', '=', 'generate_dynamic_cheque_app.report_dynamic_check_wiz')])
		if not report_action_id:
			raise Warning('Someone has deleted the reference view of report, Please Update the module!')
		config_rec = self.env['dynamic.cheque'].search([], limit=1)
		if not config_rec:
			raise Warning(_("Report format not found! Please Update Module."))
		# page_height = config_rec.cheque_hight or 10
		# page_width = config_rec.cheque_width or 10
		page_height = self.cheque_format.cheque_hight or 80	
		page_width = self.cheque_format.cheque_width or 180

		margin_top =  5
		margin_bottom =  10
		margin_left =  10
		margin_right =  10
		dpi =  90
		header_spacing =  0
		orientation = 'Portrait'
		self._cr.execute(""" DELETE FROM report_paperformat WHERE custom_report=TRUE""")
		paperformat_id = self.env['report.paperformat'].create({
			'name': 'Custom Report',
			'format': 'A4',
			'page_height': 0.0,
			'page_width': 0.0,
			'dpi': dpi,
			'custom_report': True,
			'margin_top': margin_top,
			'margin_bottom': margin_bottom,
			'margin_left': margin_left,
			'margin_right': margin_right,
			'header_spacing': header_spacing,
			'orientation': orientation,
		})
		report_action_id.write({'paperformat_id': paperformat_id.id})
		return True

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
