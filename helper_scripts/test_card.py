import card_checker

res1 = card_checker.is_valid_card("4532015112830366")
res2 = card_checker.is_valid_expiry(12, 2023)
res3 = card_checker.is_valid_cvc("123", res1)
print(res1)
print(res2)
print(res3)