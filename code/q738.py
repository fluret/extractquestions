class HoursToDaysConverter:
    def __init__(self, hours):
        self.hours = hours
 
    def convert_to_days(self):
        days = self.hours / 24
        return days
try:
    hours_input = float(input("Enter the Number of Hours : "))# Get the number of hours from the user
except ValueError:
    print("Invalid input. Please enter a valid number of hours.")
else:    
    obj = HoursToDaysConverter(hours_input) # Create an instance of the HoursToDaysConverter class
    days_result = obj.convert_to_days() #Call the Convert hours to days method   
    print(hours_input, "hours is equal to", days_result, "days.") # Display the result