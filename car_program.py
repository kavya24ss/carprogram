import sys

if len(sys.argv) > 3:
    script_name = sys.argv[0]
    car_name = sys.argv[1]
    engine_capacity = sys.argv[2]
    seating_capacity = sys.argv[3]
else:
    car_name = "BMW"
    engine_capacity = 120
    seating_capacity = 5

print("enter car name:", car_name)
print("enter the engine capacity of car:", engine_capacity)
print("enter seating capacity of car:", seating_capacity)

