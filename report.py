import frappe

def execute(filters=None):
    columns = [
        {"label": "Student", "fieldname": "student", "fieldtype": "Link", "options": "Student", "width": 150},
        {"label": "Subject", "fieldname": "subject", "fieldtype": "Link", "options": "Subject", "width": 150},
        {"label": "Score", "fieldname": "score", "fieldtype": "Float", "width": 100},
        {"label": "Weight", "fieldname": "weight", "fieldtype": "Float", "width": 100},
        {"label": "Total Score", "fieldname": "total_score", "fieldtype": "Float", "width": 120}
    ]
    data = frappe.db.sql("""
        SELECT student, subject, score, weight, (score * weight) AS total_score
        FROM `tabGrade`
        ORDER BY student, subject
    """, as_dict=1)
    return columns, data
