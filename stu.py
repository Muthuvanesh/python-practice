students = (
    ("Ravi", 85),
    ("Kumar", 92),
    ("Arun", 65),
    ("Vijay", 95),
    ("Manoj", 78)
)
highest =0
highest_name =""
count = 0
lowest = 100
lowest_name = ""

for name, marks in students:

    if marks >= 80:
        print(f"Those who scored above 80 are: {name}")
        count += 1
    if marks > highest:
        highest = marks
        highest_name = name
    if  marks < lowest:
        lowest = marks
        lowest_name = name

print(f"Total number of students who scored above 80 are: {count}")
print(f"Highest scorer: {highest_name}\nHighest marks: {highest}")
print(f"Lowest scorer: {lowest_name}\nLowest marks: {lowest}")
