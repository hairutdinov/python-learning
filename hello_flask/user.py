class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False
    # @staticmethod
    # def is_authenticated_decorator(func, *args, **kwargs):
    #     print(args)
    #     user_obj = None
    #     if 'user' in kwargs:
    #         user_obj = kwargs['user']
    #     elif len(args) > 0:
    #         user_obj = args[0]
    #
    #     if getattr(user_obj, 'is_logged_in', False):
    #         return func(*args, **kwargs)
    #     else:
    #         raise Exception('Not allowed')

class IsAuthenticatedDecorator:
    def __init__(self, func):
        self.func = func
    def __call__(self, *args, user, **kwargs):
        if getattr(user, 'is_logged_in', False):
            return self.func(*args, user, **kwargs)
        else:
            raise Exception('Not allowed')


# @User.is_authenticated_decorator
@IsAuthenticatedDecorator
def create_blog_post(user):
    print(f'This is {user.name}\'s new blog post.')

class NotUser:pass
x = NotUser()
x.name = 'john'
x.is_logged_in = True

new_user = User('Ivan')
new_user.is_logged_in = True
create_blog_post(user=new_user)