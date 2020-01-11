import estimatePrice as ep

# ep.plus()
# print(ep.estimatePrice(100))
# ep.plus()
# print(ep.estimatePrice(100))
km = 61789
price = 8290
print("init --- price for {}km : {}\n".format(km, ep.estimatePrice(km)))
for i in range(1):
	ep.training()
	print("{} | price for {}km : {}\n".format(i, km, ep.estimatePrice(km)))

print("real price for {}km = {}$".format(km, price))
