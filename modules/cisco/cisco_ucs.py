# This python module expands on the host
#
#

from host import Host

from ucsmsdk.ucshandle import UcsHandle

class CiscoUCS(Host):
    def __init__(self, name):
        super().__init__(name)

    def connect(self, user, password):
        self.handler = UcsHandle(self.name, user, password)
        self.handler.login()

    def queryH(self, dn):
        obj_list = self.handler.query_dn(dn, hierarchy=True)
        for obj in obj_list:
            print(obj)

    def query(self, dn):
        obj = self.handler.query_dn(dn)
        print(obj)

    def remove(self, dn):
        obj = self.handler.query_dn(dn)
        try:
            self.handler.remove_mo(obj)
        except:
            print("OBJ Not Defined")

    def disconnect(self):
        self.handler.logout()

class VlanGroup():
    vlans = []
    def __init__(self, name):
        self.name = name
        self.dn = 'fabric/lan/net-group-{}'.format(name)
        # TODO: Init Vlans List

    def removeVlan(self, handler, id):
        handler.query_dn(self.name)
        handler.remove_mo()

    @classmethod
    def initFromObj(self, obj):
        pass