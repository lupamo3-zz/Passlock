import unittest,pyperclip #Importing the unittest module
from newpasslock import Login #Import the login class

class TestLogin(unittest.TestCase):
    '''
    Testclass that defines login class behaviours
    Args: unittest.Testcase class helps in creating test cases.
    '''

    def setUp(self):
        '''
        Setup method to run each test cases.
        '''
        self.new_user=Login("skankhunt42", "picklerick@gmail.com", "123456") #create login object

    def test_init(self):
        '''
        test_init test case to test if object is initialized properly
        '''
        self.assertEqual(self.new_user.username, "skankhunt42")
        self.assertEqual(self.new_user.email, "picklerick@gmail.com")
        self.assertEqual(self.new_user.password, "123456")

    def test_usercreation(self):
        '''
        test_save_passlock test case to test if the password object is saved into the login list
        '''
        self.new_user.usercreation() #saving the new password 
        self.assertEqual(len(Login.login_list),1)

    def tearDown(self):
        '''
        cleans up after each test has run
        '''
        Login.login_list=[]

    def test_verify(self):
        '''
        Testing to see if it can sign in a user
        '''
        self.new_user.usercreation()
        test_account=Login("skank", "picklerick", "password")
        test_account.usercreation()

        found_user=Login.loginverify("picklerick", "password")
        self.assertEqual(found_user.username, test_account.username)


class Pword(unittest.TestCase):
    '''
    Test class that defines testcases for creating login details
    '''
    def setUp(self):
        '''
        Setting up the structure before each test
        '''
        self.new_data=Pword(1, "jumia.com", 1)

    def tearDown(self):
        '''
        Cleans up the test after test is complete
        '''
        Pword.pword_list=[]

    def test_init(self):
        '''
        Test case to evaluate if the case has been initialized properly
        '''
        self.assertEqual(self.new_data.userid, 1)
        self.assertEqual(self.new_data.webkey, 1)
        self.assertEqual(self.new_data.website "jumia.com")

    def test_add_password(self):
        '''
        Testing if the new website and password can be saved
        '''
        self.new_data.add_password()
        self.assertEqual(len(Pword.pword_list),1)

if __name__ == '__main__':
    unittest.main()