#code on python dictionary
#dictionary in python is a compund that type that works with key-value pairs
#Example
nature = {"Mountains":"peak", "Forest":"jungle"}
print ("1.", nature["Mountains"])
print ("2.", nature["Forest"])

#to remove an item using pop() method
native_wears = {"Yoruba":"Agbada", "Hausa":"Babban Riga"}
output = native_wears.pop("Hausa")
print("3.", native_wears)

#using the passs,break,continue statement and range at the same time
#Example:
for number in range (1,10):
    if number == 5:
        pass
    print (number)

for number in range (1,10):
    if number == 5:
        break
    print (number)

for number in range (1,10):
    if number == 5:
        continue
    print(number)

#The pass statement actually does nothing to the iteration of the loop
#The break statement exits the loop entirely when it meets its condition
#The continue statement skips the current iteration and moves to the next one
#range is commonly used in loops to generate a sequence of numbers. it is used iterating over a sequence of numbers within a specified range. The syntax for range is:
#range(start,stop,step). Step is the increment or decrement between each number in the sequence.

distance_km = float(input("Enter the distance: "))
conversion_rate = 0.621371
distance_miles = distance_km * conversion_rate
print ("The distance in mies is", distance_miles)




