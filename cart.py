cart5 = {
  "id": 5,
  "userId": 3,
  "date": "2020-03-01T00:00:00.000Z",
  "products": [
    {
      "productId": 7,
      "quantity": 1
    },
    {
      "productId": 8,
      "quantity": 3
    },
    {
      "productId": 2,
      "quantity": 5
    }
  ]
}
# prints 7
# print(cart5["products"][0]["productId"])

# print(cart5["products"])

# product = the loop variable? note by Brad.
for product in cart5["products"]:
    print(f"ProductId: {product["productId"]}")
    print(f"Quantity: {product["quantity"]} \n")


# getting an unknown error with my code when run. Even when i copy paste the complete code from Simon's lesson. Super strange.