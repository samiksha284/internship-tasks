frappe.ui.form.on('Ticket', {
    refresh: function(frm) {
        if (frm.doc.status === 'Resolved') {
            frm.add_custom_button('Close Ticket', () => {
                frm.set_value('status', 'Closed');
                frm.save();
            });
        }
    },
    validate: function(frm) {
        if (frm.doc.priority === 'High' && !frm.doc.assigned_to) {
            frappe.msgprint(__('High-priority tickets must be assigned to an agent.'));
            frappe.validated = false;
        }
    }
});
