class Distance:
    def __init__(self, km=0, m=0, cm=0):
        self.km = km
        self.m = m
        self.cm = cm
 
    def add(self, other_distance):
        total_km = self.km + other_distance.km
        total_m = self.m + other_distance.m
        total_cm = self.cm + other_distance.cm
 
        # Adjust units if necessary
        if total_cm >= 100:
            total_m += total_cm // 100
            total_cm %= 100
        if total_m >= 1000:
            total_km += total_m // 1000
            total_m %= 1000
 
        return Distance(total_km, total_m, total_cm)
 
    def display(self):
       return f"{self.km} KM {self.m} M {self.cm} CM"
 
print("Enter First Distance")
km1 = int(input("Enter Kilometers : "))
m1 = int(input("Enter Meters : "))
cm1 = int(input("Enter Centimeters : "))
distance1 = Distance(km1, m1, cm1)
 
print("\nEnter Second Distance")
km2 = int(input("Enter Kilometers : "))
m2 = int(input("Enter Meters : "))
cm2 = int(input("Enter Centimeters : "))
distance2 = Distance(km2, m2, cm2)
 
# Add the distances
result_distance = distance1.add(distance2)
 
# Display the result
print("Sum of both Distances is :",result_distance.display())