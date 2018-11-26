#from __future__ import unicode_literals
#import frappe
#from frappe import msgprint
#from frappe.model.document import Document
#from frappe.utils import flt
#import erpnext.controllers.taxes_and_totals


#@frappe.whitelist(allow_guest=True)
#def sales_tax_series(doc,method):
#	doctype = frappe.get_last_doc('Sales Invoice')
#	series = doctype.sales_tax
#	series_number = series.split(':')
#	tax = series_number[0]
#	tax_number = int(series_number[1])
#	if tax == doc.taxes_and_charges:		
#		tax_number = tax_number + 1
#		doc.sales_tax = doc.taxes_and_charges + ' : ' + str(tax_number)
#	else:
#		doc.sales_tax = doc.taxes_and_charges + ' : ' + str(doc.tax_series)

#def diduction(doc,method):
#	for d in doc.items:
#		total = 0.0
#		d.inches_not_excavated = 39 - d.actual_depth_excavated
#		d.cost_of_inches_not_excavated = d.inches_not_excavated * d.cost_of_one_inch_of_excavation
#		d.less_amount = d.qty * d.cost_of_inches_not_excavated
#		total = d.amount - d.less_amount
#		doc.total = total
#	doc.calculate_taxes_and_totals()		
