class User:
    def __init__(self, id, username):
        self.id = id
        self.username = username
    
    def announce_self(self):
        print(f'My name is {self.username} and my id is {self.id}')

class TutorialUser:
    def __init__(self, user_id, username) -> None:
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

# user_1 = User('001', 'tino')
# user_1.announce_self()

tutorial_user_1 = TutorialUser('010', 'tom')
tutorial_user_2 = TutorialUser('011', 'tim')

#print(tutorial_user_1.followers)

tutorial_user_1.follow(tutorial_user_2)

print(tutorial_user_1.following)
print(tutorial_user_1.followers)

print(tutorial_user_2.followers)

