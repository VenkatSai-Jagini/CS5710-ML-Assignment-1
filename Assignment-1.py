### Assignment 1


import math
### Question 1

# The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# Sort the list and find the min and max age
# sorting list of ages
sorted_ages = sorted(ages)
print("Sorted ages list :", sorted_ages)
# finding min age from sorted ages list
min_age = min(sorted_ages)
print("Min age : ", min_age)
# finding max age from sorted ages list
max_age = max(sorted_ages)
print("Max age : ", max_age)

# Add the min age and the max age again to the list
sorted_ages.extend((min_age, max_age))
print("Sorted ages after adding min and max age : ", sorted_ages)

# calculating Median of Ages
sorted_ages = sorted(sorted_ages)
len_ages = len(sorted_ages)

if len_ages % 2 == 0:
    # median calculation for list with even numbers
    median_age = (sorted_ages[int(len_ages/2)-1] + sorted_ages[int(len_ages/2)]) / 2
else:
    # median calculation for list with odd numbers
    median_age = sorted_ages[math.ceil(len_ages/2)]
print("Median Age : ", median_age)
# calculating Average of Ages
avg_age = sum(sorted_ages)/len(sorted_ages)
print("Average Age : ", avg_age)
# calculating Range of Ages
range_age = max_age - min_age
print("Range of Age : ", range_age)

### Question 2

# Create an empty dictionary called dog
dog = dict()
# Adding data to dog dictionary
dog['name'] = 'Neo'
dog['color'] = 'Black'
dog['breed'] = 'German Shepherd'
dog['legs'] = 4
dog['age'] = 4
print("Dog dictionary : ", dog)
# creating student dictionary with data
student = {
    "first_name": "Venkat Sai",
    "last_name": "Jagini",
    "gender": "Male",
    "age": 23,
    "marital status": "Single",
    "skills": ["Python", "AI"],
    "country": "United States",
    "city": "Overland Park",
    "address": "11528 Floyd Dr"
}
print("Student dictionary : ", student)
# length of the student dictionary
len_student = len(student)
# skills of the student from the dictionary
skills = student['skills']
# type of skills
print("Type of skills :",type(skills))
# updating student skills
student['skills'].extend(["ML"])
print("Updated student skills : ", student["skills"])
# keys of student dictionary
print("Keys of student dictionary : ", list(student.keys()))
# values of student dictionary
print("Values of student dictionary : ", list(student.values()))

### Question 3

# creating tuple for brothers
brothers = ("Venu","Dheeraj")
print("Brothers : ", brothers)
# creating tuple for sisters
sisters =  ("Sushmitha","Nagamani")
print("Sisters : ", sisters)

# creating siblings by adding brothers and sisters
siblings = brothers + sisters
print("Siblings : ", siblings)

# length of siblings 
len_of_siblings = len(siblings)
print("Length of siblings : ", len_of_siblings)

# adding parents with siblings tuple creating new tuple
family_members = ("Someshwar Rao","Laxmi Durga") + siblings
print("Family members : ", family_members)

### Question 4

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# length of it_companies set
print("Length of the set it_companies : ", len(it_companies))
print("IT Companies : ", it_companies)
# adding Twitter company to it_companies
it_companies.add("Twitter")
print("IT Companies : ", it_companies)
# inserting multiple IT companies to it_companies
it_companies.update(["TCS", "Accenture", "Infosys"])
print("IT Companies : ", it_companies)
# removing one company from it_companies
it_companies.discard("Oracle")
print("IT Companies : ", it_companies)
print("""Remove vs Discard : 
Remove deletes the element from the list if not present it returns Key error, 
Discard deletes the element from the list otherwise return None """)
# joining A and B sets
print("Join of A and B : ", A.union(B))
# intersection of A and B sets
print("Intersection of A and B : ",A.intersection(B))
# checking if A is subset of B
print("Is A subset of B : ", A.issubset(B))
# check if A is disjoint of B
print("Is A disjoint of B : ", A.isdisjoint(B))
# A union B and B union A
print("A union B : ", A.union(B))
print("B union A : ", B.union(A))
# symmetric difference between A and B
print("Symmetric difference between A and B : ", A.difference(B))
# deleting sets A and B
A.clear()
B.clear()
# converting age list to set
set_ages = set(age)
# comparing length of list and length of set
print("Is length of age list same of length of age set : ", len(age) == len(set_ages))

### Question 5

# The radius(r) of a circle is 30 meters.
r = 30
# pi value constant
pi = 3.14
# calculating area of circle
_area_of_circle_ =  pi * r * r
print("Area of circle :", _area_of_circle_)
# calculating cirumference of circle
_circum_of_circle_ = 2 * pi * r
print("Circumference of circle :", _circum_of_circle_)
# taking input from user
r = float(input("Enter the radius of a circle : "))
# calculating area of circle from user inputs
area_of_circle = pi * r * r
print("Area of circle : ", area_of_circle)

### Question 6

sentence = """I am a teacher and I love to inspire and teach people"""
# splitting sentence into words
split_sent = sentence.split()
print("Words : ", split_sent)
# getting unique words using set
unique_words = set(split_sent)
print("Unique Words : ", unique_words)

### Question 7

# Using a tab escape sequence to get the following lines.
data = "Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki"
print(data)

### Question 8

radius = 10
area = 3.14 * radius ** 2
# using string formatting method
sent = "The area of a circle with radius {} is {} meters square.".format(radius, area)
print(sent)

### Question 9

# input number of students
N = int(input("Enter number of students : "))
# lb to kg conversion value
lbs_to_kg_conv_value = 0.4536
lbs_weights = []
kg_weights = []
# all students weights input
for i in range(0,N):
    lbs_weights.append(int(input("Enter Student Weight(lbs) : ")))

print("lbs_weights : ",lbs_weights)

# converting weights lbs to kg
for weight in lbs_weights:
    kg_weights.append(round(weight * lbs_to_kg_conv_value,2))

print("kg_weights : ", kg_weights)

