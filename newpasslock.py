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

    def save_newpasslock(self):
        '''
        save_newpasslock method saves newpasslock objects into newpasslock_method
        '''
        Login.login_list.append(self)

class Pword:
    """
    Class that stores password and user ids
    """
    pword_list=[] #Empty pword list

    def __init__(self, userid, website, password):
        '''
        __init__ method helps us to store user details
        '''
        self.userid=userid
        self.website=website
        self.password=password

    def addpassword (self):
        """
        creating a method that creates username and password
        """
        Pword.pword_list.append(self)

