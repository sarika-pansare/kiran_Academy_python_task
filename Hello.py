#a) Print Hello World  
print("Hello World")

#b) Create two variables and print their addition
a = 5
b = 10
print(a + b)

#c) Print their difference  
print(a - b)


#d) Print their multiplication
print(a * b)

#e) Print their division  
print(a / b)

#f) Print their modulus
print(a % b)





def calculateElectronicsGST(a, b):
    total = a + b
    gst = total * 18 / 100
    return total + gst


dtotal * 13 / 100
    return total + gst


def calculateFoodGST(e):
    gst = e * 7 / 100
    return e + gst


def totalBill(a, b, c, d, e):
    electronics = calculateElectronicsGST(a, b)
    fashion = calculateFashionGST(c, d)
    food = calculateFoodGST(e)

    return electronics + fashion + food


def calculateDiscountedBill(a, b, c, d, e):
    total = totalBill(a, b, c, d, e)
    discount = total * 20 / 100
    final_amount = total - discount

    print("Total after GST: ₹{:.2f}".format(total))
    print("Discount: ₹{:.2f}".format(discount))
    print("Final payable amount: ₹{:.2f}".format(final_amount))

    return final_amount


# Main functio
    n call with the given values
calculateDiscountedBill(100, 100, 100, 100, 100)

