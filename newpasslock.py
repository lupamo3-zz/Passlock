class Login:
    """
    Class that generates username, email and password
    """

    login_list=[] #Empty login list 

    def __init__(self, username, email, password):
        '''
        __init__ method helps us to define our properties
        '''
        self.username=username
        self.email=email
        self.password=password

