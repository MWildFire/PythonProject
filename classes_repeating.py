class User:

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def __repr__(self):
        return f'{self.username}'


class Vehicle:

    def __init__(self, max_speed, max_win):
        self.max_speed = max_speed
        self.max_win = max_win


    def upgrade(self):
        self.max_speed += 10


class Auto(Vehicle):

    def __init__(self):
        pass


mitya = User("Mitya", "<PASSWORD>", "<EMAIL>")

moto = Vehicle(max_speed=150, max_win=12)
moto.upgrade()


audi = Auto()
audi.upgrade()
a = 5

print(type(a))
print(type(mitya))
print(mitya)
print(mitya.password)
print(mitya.username)


