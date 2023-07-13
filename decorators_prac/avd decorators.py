

class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in =False

def is_authenticated(function):
    def wrapper(*args):
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper

@is_authenticated
def create_post(user):
    print(f"this is {user.name}'s post")

use = User("Ram")
use.is_logged_in = True
create_post(use)



