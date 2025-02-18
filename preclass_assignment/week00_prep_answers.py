#Task_1
def greet(s):
     print ('Hello,',s,'!')
greet('world')
#Task_2
def goldilocks(num):
    height=135
    if  (num<height+5):
          print("Too small!")
    elif num>(height+15):
         print("Too large")
    else:
          print("Just right. : )")
goldilocks(150) 
#task_3
def square_list(x):
     num=[]
     for i in x:
        num.append(i*i)
     print(num) 
square_list([1,2,3])
#task 4 
def fibonacci_stop(x):
     f=[0,1]
     while True:
        next_fib = f[-1] + f[-2]
        if next_fib > x:
            break  # Stop if the next number exceeds max_value
        f.append(next_fib)
     return f
print(fibonacci_stop(30))     
#task 5

def clean_pitch(x,stat):
   clean=[]
   for angle,status in zip(x,stat):
       if (angle<0 or angle>90) and status>0:
           clean.append(-999)
       else:
           clean.append(angle)

   return clean
x = [-1, 2, 6, 95]  
status = [1, 0, 0, 0]  
print(clean_pitch(x, status))



    
    

