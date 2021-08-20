# -*- coding: utf-8 -*-

{
	'name': "Print Dynamic Cheque",
	"author": "Edge Technologies",
	'version': "14.0.1.1",
	"live_test_url":'https://youtu.be/IIJ-Lu1S0_0',
	"images":['static/description/main_screenshot.png'],
	'summary': "This apps helps to print the cheque and also can configure different bank's cheque formats.",
	'description': """
						Dynamic cheque cheque print Dynamic cheque print odoo dynamic cheque odoo dynamic cheque print
     dynamic check
dynamic bank check
bank check print
print bank check
bank cheque print
print bank cheque
odoo cheque
odoo bank cheque
cheque print
account cheque
generate Dynamic cheque
Odoo Dynamic Bank Cheque Print
Dynamic Print Cheque - Check writing
print cheque/check dynamically
Cheque format
Odoo 12 Dynamic Cheque Print
cheque different bank
odoo Dynamic Bank Check Print
print check
print cheque
print bank cheque
print bank check




					""",
    "license" : "OPL-1",
    'depends': ['base','account','account_check_printing'],
	'data': [
			'security/ir.model.access.csv',
			'data/cheque_format_data.xml',
			'reports/dynamic_cheque_report.xml',
			'reports/dynamic_cheque_templete_action.xml',
			'wizard/print_dynamic_cheque_report_wizard_view.xml',
			'wizard/print_dynamic_cheque_report_action_view.xml',
			'views/dynamic_cheque_view.xml',
			],
	'installable': True,
	'auto_install': False,
	'application': False,
	"price": 22,
	"currency": 'EUR',
	'category': "Accounting",
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
