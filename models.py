from peewee import Model, MySQLDatabase, CharField, ForeignKeyField


database = MySQLDatabase(None)


class BaseModel(Model):
    class Meta:
        database = database


class Addressbook(BaseModel):
    name = CharField(unique=True)

    def add_contact(self, name):
        return Contact(addressbook=self, name=name)


class Contact(BaseModel):
    name = CharField(unique=False)
    addressbook = ForeignKeyField(Addressbook, related_name='contacts')
