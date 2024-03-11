# week 3 assignment

def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

original_price = float(input("Enter the original price: "))
discount_percentage = float(input("Enter the discount percentage: "))

final_price = calculate_discount(original_price, discount_percentage)
print(f"The final price after applying the discount is: ${final_price:.2f}")
