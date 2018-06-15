import unittest #Importing the unittest module
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
        self.new_newpasslock=Login("skankhunt42", "picklerick@gmail.com", "123456") #create login object

    def test_init(self):
        '''
        test_init test case to test if object is initialized properly
        '''
        self.assertEqual(self.new_newpasslock.username, "skankhunt42")
        self.assertEqual(self.new_newpasslock.email, "picklerick@gmail.com")
        self.assertEqual(self.new_newpasslock.password, "123456")

    def test_save_newpasslock(self):
        '''
        test_save_passlock test case to test if the password object is saved into the login list
        '''
        self.new_newpasslock.save_newpasslock() #saving the new password 
        self.assertEqual(len(Login.login_list),1)

    def tearDown(self):
        '''
        cleans up after each test has run
        '''
        Login.login_list=[]


if __name__ == '__main__':
    unittest.main()