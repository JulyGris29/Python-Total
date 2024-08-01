python = {1, 2, 3}
cool = {1, 2, 2, 3}

for _ in python:
    print(python is cool)
    if python == cool:
        break
else:
    print(python is not cool)