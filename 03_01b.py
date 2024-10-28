from collections import namedtuple

def can_take_order(driver, num_packages):
    return driver.car_capacity >= num_packages
def main():
    #add code here
    #create a driver with a name, car type, and car capacity
    driver = namedtuple("driver", ["name", "car_type", "car_capacity"])
    #an example you can use to practice: "Iris", "Toyota Prius", 7
    bulma = driver("Bulma", "Prius", 7)
    yamcha = driver("Yamcha", "Tucson", 15)
    nappa = driver("Nappa", "Hummer", 26)
    #check if they can take a certain order, given their car's capacity.
    print(can_take_order(nappa, 20))
    print(can_take_order(yamcha, 20))
    return

if __name__ == "__main__":
    main()