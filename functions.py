
#1 Write simple function

def greet(name):
    return f"hello,, {name}"




#2 If/else statement
def goldilocks(BedSize):
    if BedSize < 140:
        return "Too small!"
    elif BedSize > 150:
            return "Too big!"
    else:
            return "Just right. :)"



#3 For loops
def square_list(numbers):
      squared_numbers = []
      for num in numbers:
            squared_numbers.append(num**2)
      
      return squared_numbers



#While loops
def fibonacci_stop(max_value):
      fibonacci_numbers = [1,1]
      while True:
            next_number= fibonacci_numbers[-1] + fibonacci_numbers[-2] #sum of last two numbers
            if next_number > max_value:
                  break
            fibonacci_numbers.append(next_number)
      return fibonacci_numbers




#Logical operators
def clean_pitch(pitch_angles, status_signals):
      cleaned_data =[]
      for angle, status in zip(pitch_angles, status_signals):
            if (angle <0 or angle >90) and status >0:
                  cleaned_data.append(-999)
            else:
                  cleaned_data.append(angle)
      return cleaned_data



