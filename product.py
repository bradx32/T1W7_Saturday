# pasted from lesson 
product2 = {

  "id": 2,

  "title": "Mens Casual Premium Slim Fit T-Shirts ",

  "price": 22.3,

  "description": "Slim-fitting style, contrast raglan long sleeve, three-button henley placket, light weight & soft fabric for breathable and comfortable wearing. And Solid stitched shirts with round neck made for durability and a great fit for casual fashion wear and diehard baseball fans. The Henley style round neckline includes a three-button placket.",

  "category": "men's clothing",

  "image": "https://fakestoreapi.com/img/71-3HjGNDUL._AC_SY879._SX._UX._SY._UY_.jpg",

  "rating": {

    "rate": 4.1,

    "count": 259

  }

}

print(product2["price"])
# or use the .get method.... print(product2.get[])

# to get 'count' from the 'rating' keyword
print(product2["rating"]["count"])

print(product2["rating"]["rate"])
