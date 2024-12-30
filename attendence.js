frappe.ui.form.on('Attendance', {
    validate: function(frm) {
        if (!frm.doc.student || !frm.doc.date) {
            frappe.msgprint(__('Student and Date are required to mark attendance.'));
            frappe.validated = false;
        }
    }
});
