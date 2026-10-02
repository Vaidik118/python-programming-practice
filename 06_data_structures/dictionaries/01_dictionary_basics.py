shoes = {
    "adidas": 1200,
    "nike": 1800,
    "sketchers": 3000
}

print("Shoes:", shoes)


print("Nike price:", shoes["nike"])


shoes["puma"] = 1500


shoes["nike"] = 2000


if "adidas" in shoes:
    print("Adidas is available")

print("Updated shoes:", shoes)