"""This module is responsible for getting names"""

class Names:
	"""This class allows get names"""
	@staticmethod
	def get_names(gender):
		"""Returns all male/female names in names/male.txt file.
		:param gender: str
		:return: list
		"""

		# reading names
		with open(f"names/{gender}.txt", "rt") as fl:
			lines = fl.readlines()

		# deleting all \n from 'lines' list elements
		result = list()
		for i in range(len(lines)):
			line = lines[i]
			line = line.replace("\n", "")
			result.append(line)

		return tuple(result)