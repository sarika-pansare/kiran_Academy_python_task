
def calculateElectronicsGST(a, b):
    total = a + b
    gst = total * 18 / 100
    return total + gst


def calculateFashionGST(c, d):
    total = c + d
    gst = total * 13 / 100
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


calculateDiscountedBill(100, 100, 100, 100, 100)

