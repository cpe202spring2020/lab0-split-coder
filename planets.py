def weight_on_planets():
   # write your code here
   input_weight = float(input("What do you weigh on earth? "))
   print("\nOn Mars you would weigh {:.2f} pounds.\nOn Jupiter you would weigh {:.2f} pounds.".format(input_weight*0.38, input_weight*2.34))
   
   
   
if __name__ == '__main__':
   weight_on_planets()