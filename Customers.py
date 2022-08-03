from Shop import BikeRental
class Customer:

    def __init__(self):
        self.bike = 0
        self.issue_time = 0
        self.rental_choice = 0
        self.bill = 0

    def requestBike(self):
        bike = input("Please enter the amount of bikes you would like to rent.")
        bike = int(bike)
        if bike <= 0:
            print("Please enter a valid number.")
        else:
            self.bike = bike
        return self.bike
     
    def returnBike(self):
        if self.rental_choice and self.issue_time and self.bike:
            return self.rental_choice, self.issue_time, self.bike  
        else:
            return None

            