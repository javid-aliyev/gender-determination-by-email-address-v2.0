import sys

class Determinator:
    def __init__(self, argv):
        self.email = argv[1]
        #self.male_names = Emails.get_names("male")
        #self.female_names = Emails.get_names("female")

        self.min_ratio_coefficient = 50 # the minimum allowed value of fuzz.ratio(email)

        self.main()

    def main():
        pass

if __name__ == "__main__":
    Determinator(sys.argv)