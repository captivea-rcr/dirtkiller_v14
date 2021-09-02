# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from num2words import num2words
import re

class dynamic_cheque_template(models.AbstractModel):
	_name='report.generate_dynamic_cheque_app.report_dynamic_check_print'
	_description="Dynamic Cheque Report Template"


	def get_payment_account_invoice(self, payment_id):
		invoice_ids = self.env['account.move'].search([('id', 'in', payment_id.reconciled_bill_ids.ids)])
		return invoice_ids

	def get_rendom_check_no(self, wizard):
		number_random = wizard.next_check_number
		wizard.payment_id.update({'next_check_number': number_random})
		return number_random

	def get_check_micr_font(self, wizard):
		number_random = wizard.next_check_number
		number_random_str = str(number_random)
		# replaced = re.sub('[0-9]', '#', number_random_str)
		micr_font_str = 'C' + str(number_random_str) + 'C'
		micr_font_strdict = {
			'first_line' : micr_font_str,
			'second_line': str(wizard.cheque_format.micr_font)
		}
		return micr_font_strdict

	def get_amount_in_word_line(self, payment_id, cheque_format):
		amount = str("{0:.2f}".format(payment_id.amount))     
		split_amount  = amount.split(".")
		first_amount_n2w = num2words(split_amount[0], lang=self._context.get('lang'))
		if split_amount[1] != "00":
			amount_word = first_amount_n2w + " and " + split_amount[1] + " / 100"
		else:
			amount_word = first_amount_n2w
		first_line = (amount_word[0:cheque_format.words_in_fl_line])
		s1 = cheque_format.words_in_fl_line
		s2 = cheque_format.words_in_fl_line + cheque_format.words_in_sc_line
		second_line = (amount_word[s1:s2])
		localdict = {
			'first_line' : first_line,
			'second_line': second_line
		}
		return localdict


	def _get_report_values(self, docids, data=None):
		active_ids = data.get('ids')
		wizard_id = data.get('form')[0]
		docids = wizard_id.get('id')
		wizard  = self.env['dynamic.cheque.wizard'].browse(docids)
		payment_id = self.env['account.payment'].browse(active_ids)
		return {
				'doc_model': 'dynamic.cheque',
				'cheque_format' : wizard.cheque_format,
				'payment_id' : payment_id,
				'get_account_invoice': self.get_payment_account_invoice,
				'get_amount_in_word_line': self.get_amount_in_word_line,
				'get_rendom_check_no': self.get_rendom_check_no(wizard),
				'get_check_micr_font': self.get_check_micr_font(wizard),
				}

class report_paperformat(models.Model):
	_inherit = "report.paperformat"

	custom_report = fields.Boolean('Temp Formats', default=False)


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: