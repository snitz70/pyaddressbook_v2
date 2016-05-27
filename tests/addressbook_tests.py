from models import Addressbook
import pytest


class TestAddressbook():

    @pytest.fixture
    def addrbook(self):
        return Addressbook(name='test addressbook')

    def test_addressbook_is_created(self, addrbook):
        assert addrbook.name == 'test addressbook'

    def test_add_name_to_addressbook(self, addrbook):
        contact = addrbook.add_contact('brian snyder')
        assert contact.name == 'brian snyder'
        assert contact.addressbook.name == 'test addressbook'

