frappe.ui.form.on("Sales Invoice", {
    "sales_tax": function(frm) {
        frappe.call({
		"method": "group_multitech.group_multitech.sales_tax_series.sales_tax_series",
		args: {
			sales_tax: frm.doc.sales_tax,
			company: frm.doc.company
		},
		callback:function(r){
		frm.set_value("tax_series",r.message);
		;}
	});
    }
});

frappe.ui.form.on("Sales Invoice", {
    "company": function(frm) {
        frappe.call({
		"method": "group_multitech.group_multitech.sales_tax_series.sales_tax_series",
		args: {
			sales_tax: frm.doc.sales_tax,
			company: frm.doc.company
		},
		callback:function(r){
		frm.set_value("tax_series",r.message);
		;}
	});
    }
});
