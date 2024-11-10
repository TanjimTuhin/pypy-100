class User:
    def __init__(self,user_id,user_name):
        self.id=user_id
        self.username=user_name
        self.follower=0      
        self.following=0
    def follow(self,user):
        user.follower +=1
        self.following +=1
        
user_1 = User("001","Yuhan")
# user_1.id='001'
# user_1.username='Yuhan'

# print(user_1.username)

user_2=User("002","Frankestine")
# user_2.id='002'
# user_2.username='Frankestine'

user_1.follow(user_2)
print(user_1.follower)
print(user_1.following)
print(user_2.follower)
print(user_2.following)