import frappe
from frappe.model.document import Document

class Ticket(Document):
    def after_insert(self):
        # Notify the assigned agent of the new ticket
        if self.assigned_to:
            frappe.sendmail(
                recipients=self.assigned_to,
                subject=f"New Ticket Assigned: {self.title}",
                message=f"Ticket Details:\n\nTitle: {self.title}\nPriority: {self.priority}\nStatus: {self.status}\n\nPlease address it at your earliest."
            )

    def validate(self):
        # Ensure high-priority tickets are assigned to an agent
        if self.priority == "High" and not self.assigned_to:
            frappe.throw("High-priority tickets must be assigned to an agent.")
