"""
The module stores Emails class
"""

class Emails:
	"""
	The Emails class has methods to parse name from email, etc
	"""
	@staticmethod
	def get_login_from_email_address(email):
		"""Returns login from email. javid15@gmail.com -> javid15
		:param email: str
		:return: str
		"""
		result = ""
		for char in email:
			if char != "@":
				result += char
			else:
				break
		return result
