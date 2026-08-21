print("-----ZOMATO FOOD DELIVERY-----")
order_amount = float(input("Enter order amount:"))
del_distance = float(input("Enter delivery distance:"))

customer_type = input("Enter customer type (regular/new/premium):")
customer_rating = float(input("Enter customer rating: "))
restaurant_rating = float(input("Enter restaurant rating:"))
prep_time = int(input("Enter preparation time:"))

pay_method = input("Enter payment method (cash/upi/card):")
weather = input("Enter weather (normal/rain/storm):")
demand = input("Enter demand (low/medium/high):")
peak_hour = input("Is it peak hour? (yes/no):")
cancellations = int(input("Enter previous cancellations:"))

if restaurant_rating >= 4.5:
    restaurant_status = "Excellent"
elif restaurant_rating >= 3.5:
    restaurant_status = "Good"
elif restaurant_rating >= 2.5:
    restaurant_status = "Average"
else:
    restaurant_status = "Poor"


if del_distance <= 4:
    delivery_charge = 40
elif del_distance <= 6:
    delivery_charge = 60
elif del_distance <= 10:
    delivery_charge = 100
else:
    delivery_charge = 140

if weather == "rain":
    delivery_charge = delivery_charge + 30
elif weather == "storm":
    delivery_charge = delivery_charge + 50

if customer_type == "premium":
    if order_amount >= 1000:
        discount = order_amount * 0.30
    elif order_amount >= 500:
        discount = order_amount * 0.20
    else:
        discount = order_amount * 0.10

elif customer_type == "regular":
    if order_amount >= 1000:
        discount = order_amount * 0.15
    elif order_amount >= 500:
        discount = order_amount * 0.10
    else:
        discount = order_amount * 0.05    

elif customer_type == "new":
    if order_amount >= 1000:
        discount = order_amount * 0.20
    if order_amount >= 500:
        discount = order_amount * 0.15    
    else:
        discount = order_amount * 0.10


priority = "Normal"

if customer_type == "premium" and order_amount >= 1000:
    priority = "Priority"
elif customer_rating >= 4.5 and order_amount >= 500:
    priority = "Priority"
elif demand == "high" and peak_hour == "yes":
    priority = "Priority"



if cancellations >= 5:
    cancellation_risk = "High"
elif cancellations >= 2:
    cancellation_risk = "Medium"
else:
    cancellation_risk = "Low"

manual_review = "No"

if customer_rating < 3.5:
    manual_review = "Yes"
elif restaurant_rating < 3.5:
     manual_review = "Yes"
elif cancellations >= 6:
     manual_review = "Yes"
elif weather == "storm" and del_distance > 10:
     manual_review = "Yes"
elif order_amount >= 2000 and pay_method == "cash":
    manual_review = "Yes"

if manual_review == "Yes":
    order_status = "Manual Review"
elif restaurant_rating < 3.5:
    order_status = "Rejected"
elif customer_rating < 2.5:
    order_status = "Rejected"
elif weather == "storm" and del_distance > 20:
    order_status = "Rejected"
elif prep_time > 100:
    order_status = "Rejected"
else:
    if pay_method == "cash" and order_amount > 2500:
        order_status = "Manual Review"
    elif pay_method == "upi" or pay_method == "card":
        order_status = "Accepted"
    else:
        order_status = "Accepted"

if order_status == "Rejected":
    order_category = "Rejected Order"
elif order_status == "Manual Review":
    order_category = "Verification Required"
elif priority == "Priority":
    order_category = "Priority Order"
elif cancellation_risk == "High":
    order_category = "High Risk Order"
else:
    order_category = "Normal Order"

final_amount = order_amount - discount + delivery_charge

if order_status == "Rejected" or order_status == "Manual Review":
    final_amount = 0

print("FINAL REPORT OF ORDER")

print("Order Status:", order_status)
print("Delivery Charge:", delivery_charge)
print("Discount:", discount)
print("Priority Status:", priority)
print("Cancellation Risk:", cancellation_risk)
print("Restaurant Status:", restaurant_status)
print("Manual Review:", manual_review)
print("Final Order Category:", order_category)
print("Final Payable Amount:", round(final_amount, 2))