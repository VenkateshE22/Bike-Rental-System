import datetime
class BikeRental():
    def __init__(self,stock=0):
        self.stock=stock
    def availableBikes(self):
        print(f"The amount of bikes available for rent are {self.stock}")
        return self.stock   
    def hourlyBasis(self,num):
        if num <= 0:
            print("Please select a valid number.")
            return None
        elif num > self.stock:
            print(f"Sorry for the inconvenience. We only have {self.stock} bikes available at this moment.")
            return None
        else:
            now = datetime.datetime.now()
            self.stock=num
            print(f"You have selected to rent the bike on hourly basis today at {now.ctime()} {num} bikes.")
            print("You will have to pay $5 per hour of renting. Thank You for choosing us.")
            self.stock =- num
            return now
    def dailyBasis(self,num):
        if num <= 0:
            print("Please select a valid number.")
            return None
        elif num>self.stock:
            print(f"Sorry for the inconvenience. We only have {self.stock} bikes available at this moment.")
            return None
        else:
            now = datetime.datetime.now()
            self.stock = num
            print(f"You have selected to rent the bike on a daily basis today at {now.ctime()} {num} bikes.")
            print("You will have to pay $20 per day of renting. Thank You for choosing us.")
            self.stock =- num
            return now

    def weeklyBasis(self,num):
        if num <= 0:
            print("Please select a valid number.")
            return None
        elif num>self.stock:
            print(f"Sorry for the inconvenience. We only have {self.stock} bikes available at this moment.")
            return None
        else:
            now = datetime.datetime.now()
            self.stock = num
            print(f"You have selected to rent the bike on a weekly basis today at {now.ctime()} {num} bikes.")
            print("You will have to pay $50 per week of renting. Thank You for choosing us.")
            self.stock =- num
            return now
    
    def bikeReturn(self,request):
        issue_time = 0
        rental_choice = 0
        numofBike = 0
        request = 0
        bill =0

        if issue_time and rental_choice and numofBike:
            self.stock += numofBike
            now = datetime.datetime.now()
            rentalPeriod = now - issue_time
        
            if rental_choice == 1:
                bill = round(rentalPeriod.seconds / 3600) * 5 * numofBike
          
            elif rental_choice == 2:
                bill = round(rentalPeriod.days) * 20 * numofBike
             
            elif rental_choice == 3:
                bill = round(rentalPeriod.days / 7) * 60 * numofBike
            
            if (3 <= numofBike <= 5):
                print("COngratulations! You can successfully avail our group promotional offer.")
                bill = bill * 0.7

            print(f"Your total bill is $ {bill}")
            print("Thank you for choosing us. Please visit again.")
            return bill
        else:
            print("Sorry you are at the wrong place.")
            exit()
            