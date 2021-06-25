#normal way to use
a = {"hey": 1, "ho": 2, "lets": 3, "go": 4}
b = {}

for k, v in a.items():
    b[k] = v

print(b)

#dictionary comprehensions
a = {"hey": 1, "ho": 2, "lets": 3, "go": 4}
b = {k: v for k, v in a.items()}
print(b)

# continua...