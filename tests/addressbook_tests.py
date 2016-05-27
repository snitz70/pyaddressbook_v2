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

    def test_add_address_to_contact(self, addrbook):
        contact = addrbook.add_contact('brian snyder')
        address = contact.add_address('512 2nd st se dyersville ia 52040')
        assert address.address == '512 2nd st se dyersville ia 52040'
        assert address.contact.name == 'brian snyder'

