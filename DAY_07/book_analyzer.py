from functools import reduce
prices = [120, 250, 80, 300, 150, 90]
gst_prices = list(map(lambda x: x + 20, prices))
expensive_books = list(filter(lambda x: x > 150, gst_prices))
total = reduce(lambda a, b: a + b, expensive_books)
print("Prices after GST:", gst_prices)
print("Books above ₹150:", expensive_books)
print("Total Price:", total)