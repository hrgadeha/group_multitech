from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Daily Wages Labour"),
			"items": [
				{
					"type": "doctype",
					"name": "Daily Wages Labour Year Master",
				},
				{
					"type": "doctype",
					"name": "Daily Wages Labour Month Master",
				},
				{
					"type": "doctype",
					"name": "Cluster",
				},
				{
					"type": "doctype",
					"name": "Daily Wages Labour"
				}
				
			]
		},
		{
			"label": _("Customer Contract Masters"),
			"items": [
				{
					"type": "doctype",
					"name": "Customer Contract",
				},
				{
					"type": "doctype",
					"name": "Company Enlistment",
				}
			]
		},
	]
