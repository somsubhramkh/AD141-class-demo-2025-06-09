#!/usr/bin/env python3

class Address:
    def __init__(self, street, city, state, zip):
        self.street = street
        self.city = city
        self.state = state
        self.zip = zip

    def __str__(self):
        return "".join([self.street, "\n", self.city, ", ", self.state, " ",
                       self.zip])


class Customer:
    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

    def __str__(self):
        return "".join([self.first_name, " ", self.last_name, "\n",
                       str(self.address)])


def get_customers():
    customer_list = []
    with open("customers.txt", "r") as thefile:
        for customer_txt in thefile:
            c = customer_txt.rstrip().split(",")
            address = Address(c[2], c[3], c[4], c[5])
            customer = Customer(c[0], c[1], address)
            customer_list.append(customer)
    return customer_list

def sortby(customer):
    return (customer.address.state, customer.last_name, customer.first_name)

def get_info(customers):
    print("Nested Structure:", type(customers),
          type(customers[0]), type(customers[0][0]))
    # partial contents of customers
    print(customers[0], customers[1], sep="\n", end="\n\n")

def get_dictionary(customers):
    # Convert to dictionary using a dictionary comprehension
    return {"{} {}".format(cust[0], cust[1]): cust for cust in customers}

def print_customernames(customer_names):
    print("Customer names:")
    for i, name in enumerate(customer_names):
        print("{0:20}".format(name), end="|")
        if i % 4 == 3:
            print()
    print("\n")

def user_interaction(customers):
    tags = ["FirstName", "LastName", "Street", "City", "State", "ZipCode"]
    fmt = "{:16}{:16}{:20}{:16}{:6}{:5}"
    while True:
        name = input("Enter a name (or 'quit' to quit):")
        if name == "quit":
            break
        data = customers.get(name)
        if data:
            print(fmt.format(*tags))
            print(fmt.format(*data))

def main():
    # customer_list = get_customers()
    # customer_list.sort(key=lambda x: (x[4], x[1], x[0]))
    # for customer in customer_list:
    #     print(customer)
    # get_info(customer_list)
    # customer_map = get_dictionary(customer_list)
    # print_customernames(customer_map.keys())
    # user_interaction(customer_map)

    customer_list = get_customers()
    customer_list.sort(key=sortby)
    for customer in customer_list:
        print(customer, end="\n\n")


if __name__ == "__main__":
    main()