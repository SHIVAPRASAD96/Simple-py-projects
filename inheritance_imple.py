class Parent:
    value1 = "The 1st Vaiable 1 is created"

    value2 = "The 2nd Variable 2 is created"

class child(Parent):
    pass

child_01= child()
print(child_01.value1)
print(child_01.value2)
