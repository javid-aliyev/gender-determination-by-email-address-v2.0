import sys
from fuzzywuzzy import fuzz

from emails import Emails
from names import Names

class Determinator:
	min_ratio_coefficient = 40 # the minimum allowed value of fuzz.ratio(email)

	def __init__(self, argv):
		self.email_login = Emails.get_login_from_email_address(argv[1])
		self.male_names = Names.get_names("male")
		self.female_names = Names.get_names("female")

		self.main()

	def compare_login_with_names(self):
		"""Compares login with female and male names and returns gender
		:return: str
		"""
		for mname, fname in zip(self.male_names, self.female_names):
			if fuzz.ratio(mname.lower(), self.email_login) >= Determinator.min_ratio_coefficient or \
				self.email_login in mname.lower():
				return "Male"
			elif fuzz.ratio(fname.lower(), self.email_login) >= Determinator.min_ratio_coefficient or \
				self.email_login in fname.lower():
				return "Female"
		return "Undefined"

	def main(self):
		print(self.compare_login_with_names())

if __name__ == "__main__":
	assert len(sys.argv) > 1
	Determinator(sys.argv)