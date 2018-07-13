def ground_weight_cost(weight):

  if(weight <= 2):
  	return (1.50 * weight) + 20.00;
  elif(weight >= 2 and weight <= 6):
    return (3.00 * weight) + 20.00;
  elif(weight >= 6 and weight <= 10):
    return (4.00 * weight) + 20.00;
  elif(weight >= 10):
    return (4.75 * weight) + 20.00;


def drone_weight_cost(weight):

  if(weight <= 2):
  	return (4.50 * weight) + 0.00;
  elif(weight >= 2 and weight <= 6):
    return (9.00 * weight) + 0.00;
  elif(weight >= 6 and weight <= 10):
    return (12.00 * weight) + 0.00;
  elif(weight >= 10):
    return (14.75 * weight) + 0.00;

#premium_shipping = 125.00;

def cheapest_shipping(weight):
  premium_shipping = 125.00;

  if(weight <= 2):
  	return (4.50 * weight) + 0.00;
  elif(weight >= 2 and weight <= 6):
    return (3.00 * weight) + 20.00;
  elif(weight >= 6 and weight <= 10):
    return (4.00 * weight) + 20.00;
  elif(weight >= 10):
    return (4.75 * weight) + 20.00;
  else:
  	return 125.00;


#print(ground_weight_cost(10));
#print(drone_weight_cost(10));
#print(cheapest_shipping(4.8));
print(cheapest_shipping(41.5));
