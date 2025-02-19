from os import name
from functions import greet, goldilocks, square_list, fibonacci_stop, clean_pitch

# Call the function
greet("Tessa")
print(f"Hello, {name}!")

goldilocks(139)
goldilocks(140)
goldilocks(151)
goldilocks(150)

print(square_list([1,2,3]))

print(fibonacci_stop(30))
angle = [-2, 3, 6, 95]  # "raw" pitch angles
status = [1, 0, 0, 0]  # status signals
print(clean_pitch(angle, status)) 

