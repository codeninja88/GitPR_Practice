"""
A simple dictionary example for demo purposes of git PR.
"""


def main():
    ages_dict = {"Bill": 21, "Jane": 34, "Jack": 56}
    name = input("Name: ")
    age = int(input("Age:"))
    ages_dict[name] = age
    for key, value in ages_dict.items():
        print("{:8} - {:8}".format(key, value))


main()
