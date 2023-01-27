bill_total = +int(input("enter total number of bill:"))
discount1 = 10;
discount2 = 20;
discount3 = +int(bill_total/2);

if bill_total>100 and bill_total<200:
  print("bill is greater than 100! ")
  bill_total = bill_total - discount1;
elif bill_total>200 and bill_total<500:
    print("bill is greater than 200!")
    bill_total = bill_total - discount2;
elif bill_total>500 :
    print("bill is greater than 500!")
    bill_total = bill_total - discount3;
else:
      print("bill is less than 100!")
      
      
print("total bill: "+str(bill_total))      

# Let's say you want to give a certain discount to customers if they spend over $100. 
# You will also provide an extra discount if that customer is part of a loyalty program. 
# If the customer is not part of the loyalty program and did not spend over a $100, 
# a service charge of 5% is applied.
loyalty_customer = True
total_bill = 124

if loyalty_customer and total_bill > 100:
    #give 20% discount
    total_bill = total_bill - (float(total_bill)/ 100) * 20
elif total_bill > 100:
    #give 10% discount
    total_bill = total_bill - (float(total_bill)/ 100) * 10
else:
    #sorry no discount, 5% service charge applied.
    print('Sorry, no discount ...')

print('Total Bill: ', float(total_bill))