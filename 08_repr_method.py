class Person:
    def __init__(self, name, address, email):
        self.name = name
        self.address = address
        self.email = email
    
    def __str__(self):
        return f"Name: {self.name} Address: {self.address} Email: {self.email}"
    
    def __repr__(self):
        return self.name
    
tamas = Person("Kiss Tamás", "Pécs", "tamas@gmail.com")
csaba = Person("Nagy Csaba", "Budapest", "csaba@gmail.com")

my_friends = [tamas, csaba]
print(my_friends)