from debus.objects import DBusInterface, DBusObject, dbus_method

class PropertiesInterface(DBusInterface):
    name = 'org.freedesktop.DBus.Properties'

    @dbus_method('ss', 'v')
    def Get(self, iface: str, name: str):
        return ['']

    @dbus_method('ssv', '')
    def Set(self, iface: str, name: str, value):
        pass

    @dbus_method('s', 'a{sv}')
    def GetAll(self, iface: str):
        return [[]]
