#
#
#
## Create Class in Python
## class use PascalCase -> UserPayment
#
#
#
#class User:
#
#
#user_1 = User()
#
#
#create attribute
#user_1.id= "001"
#user_1.username="Molly"
#
#print(user_1.username)
#
#this way -> easy to make typo error eg -> name/username
#user_1.id= "002"
#user_1.name="Jess"
#
#To prevent build class :
#class User:
#    def __int__(self):
#        self.username

# attribute -> what a objects has
# methods -> what a objects dose

#class Car:
#
#    def __init__(self, car_seats):
#        self.seats = car_seats
#
#    def enter_race_mode(self):
#        self.seats = 2
#
#
#my_car=Car(4)
#print(my_car.seats)
#my_car.enter_race_mode()
#print(my_car.seats)



class User:

    def __init__(self, user_id, user_name):
        self.id = user_id
        self.username = user_name
        #set default value
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("1","Molly")
user_2 = User("2","Jess")

user_1.follow(user_2)


print(f"Id: {user_1.id}, Username: {user_1.username}, Followers: {user_1.followers} Following: {user_1.following}")
