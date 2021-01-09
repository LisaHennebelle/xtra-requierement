import unittest
#importer la methode de verification verify_password
from quick_tools import verify_password
from quick_tools import verify_room_type
import random
import string


class TestQuickToolsMethods(unittest.TestCase):

    def setUp(self):
        #Creation de BDD
        self.db_path = 'test_chat.db'
        self.connect = sqlite3.connect(self.db_path)
        self.cursor = self.connect.cursor()
        tool.create_db(self.db_path)

    def tearDown(self):
        #Suppression de BDD
        tool.delete_db(self.db_path)

    def test_verify_password(self):
        self.assertFalse(verify_password('whateve'))  #mdp de longueur inferieure a 8 caracteres
        self.assertFalse(verify_password('3ightcar')) #pas de caractere special
        self.assertFalse(verify_password('€ightcar')) #pas de chiffre
        correct_passw = ""
        str_len=3
        for i in range(str_len):
            correct_passw += random.choice(string.ascii_lowercase)
            correct_passw += random.choice(string.digits)
            correct_passw += random.choice(string.punctuation)
        self.assertTrue(verify_password(correct_passw))

    def test_verify_room_type(self):
        #Rooms (room_name,room_type)
        wrong_room_type = "PUB"
        self.assertFalse(verify_room_type(wrong_room_type))

        self.assertTrue(verify_room_type('private'))
        self.assertTrue(verify_room_type('public'))

