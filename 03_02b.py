from collections import namedtuple
from csv import reader
def main():
    #read data/Customer.csv
    with open("data/Customer.csv", "r") as open_csv:
        read = reader(open_csv)
        Person = namedtuple("Person", next(read))
    #Create workable objects with each line
        for line in read:
            person = Person(*line)
            print(person.Email)
    return

if __name__ == "__main__":
    main()