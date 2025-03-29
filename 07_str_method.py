class Person:
    def __init__(self, name, address, email):
        self.name = name
        self.address = address
        self.email = email
    
    def __str__(self):
        return self.name


tamas = Person("Kiss Tamás", "Pécs", "tamas@gmail.com")
csaba = Person("Nagy Csaba", "Budapest", "csaba@gmail.com")

print(tamas)
print(csaba)