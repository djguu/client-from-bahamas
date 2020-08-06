import unittest
from unittest import TestCase
from app import ClientGateway


class Test(TestCase):
    # def test_register(self):
    #     # self.fail()
    #     self.run()

    def test_valid_email(self):
        self.assertTrue(ClientGateway.valid_email("teste@teste.pt"))
        self.assertFalse(ClientGateway.valid_email("teste@.pt"))
        self.assertFalse(ClientGateway.valid_email("teste.pt"))
