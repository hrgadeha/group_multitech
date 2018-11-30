from __future__ import unicode_literals
import frappe
from frappe import msgprint
from frappe.model.document import Document
from frappe.utils import flt
import erpnext.controllers.taxes_and_totals

@frappe.whitelist(allow_guest=True)
def sales_tax_series(sales_tax,company):
	query= frappe.db.sql("SELECT MAX(tax_number) FROM  `tabSales Invoice` WHERE  sales_tax = '"+str(sales_tax)+"' and company = '"+str(company)+"';")
	return query
