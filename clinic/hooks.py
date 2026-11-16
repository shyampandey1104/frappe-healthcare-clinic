# Copyright (c) 2026, Shyamkumar Pandey and contributors
# For license information, please see license.txt

app_name = "clinic"
app_title = "Frappe Healthcare Clinic"
app_publisher = "Shyamkumar Pandey"
app_description = "Frappe Healthcare Clinic for Frappe and ERPNext"
app_email = "shyampandey1104@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------
app_include_css = "/assets/clinic/css/clinic.bundle.css"
app_include_js = "/assets/clinic/js/clinic.bundle.js"

# Document Events
# ---------------
doc_events = {
    "DocType Event": {
        "on_submit": "clinic.engine.on_document_submit",
        "on_cancel": "clinic.engine.on_document_cancel"
    }
}

# Scheduled Tasks
# ---------------
scheduler_events = {
    "daily": [
        "clinic.engine.daily_scheduled_sync"
    ]
}
