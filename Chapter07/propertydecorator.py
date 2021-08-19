
class Tank(object):
    def __init__(self, name, ammunition):
        self.__name = name
        self.__ammunition = ammunition

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def ammunition(self):
        return self.__ammunition
    
    @ammunition.setter
    def ammunition(self, new_ammo):
        self.__ammunition += new_ammo

    @property
    def fire(self):
        self.ammunition -= 10
        print(f"10 units of ammunition were used, remaining: {self.ammunition}")

    @property
    def reload(self):
        self.ammunition += 10
        print(f"50 units of ammunition were added to the reserve, remaining: {self.ammunition}")

Sherman = Tank(name = "Sherman", ammunition=1000)

print(Sherman.name)
print(Sherman.ammunition)
print(Sherman.fire)
print(Sherman.fire)
print(Sherman.fire)
print(Sherman.fire)
print(Sherman.fire)
print(Sherman.reload)

