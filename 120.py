# This problem was asked by Microsoft.
# Implement the singleton pattern with a twist. First, instead of storing one instance, store two instances.
# And in every even call of getInstance(), return the first instance and in every odd call of getInstance(),
# return the second instance.
####
# A singleton pattern apparently entails, the same instance of the class returned across all declarations.
# i.e. only a single class object exists across all calls.
####
class Twister:
    instance = []
    i = 1
    def get_instance(self):
        Twister.i += 1
        return Twister.instance[Twister.i % 2]

    def __init__(self):
        if len(Twister.instance) < 2:
            Twister.instance.append(self)

####
a = Twister()
a.val = 0
b = Twister()
b.val = 2
c = Twister()
c.val = 4
print(a.get_instance().val)
print(a.get_instance().val)
print(a.get_instance().val)
print(b.get_instance().val)
print(b.get_instance().val)
print(b.get_instance().val)
print(c.get_instance().val)
print(c.get_instance().val)
print(c.get_instance().val)
