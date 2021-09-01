
# Copyright (c) 2021, kang kimchhay and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class HotelBooking(Document):
	def before_save(self):
		if self.from_date > self.to_date:
			frappe.throw("From date must be smaller than to date")
	def before_submit(self):
		booking = frappe.db.get_list(
				"Hotel Booking",
					filters = {
						"docstatus":1,
						"status" : "Booking",
						"hotel_room": self.hotel_room
					})
		if 1 <= len(booking):
			frappe.throw("Room already Booking")
	
