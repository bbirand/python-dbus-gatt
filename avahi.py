import dbus
 
sys_bus = dbus.SystemBus()
 
# get an object called / in org.freedesktop.Avahi to talk to
#raw_server = sys_bus.get_object('org.freedesktop.Avahi', '/')
raw_server = sys_bus.get_object('org.bluez', '/hci0')
 
# objects support interfaces. get the org.freedesktop.Avahi.Server interface to our org.freedesktop.Avahi object.
server = dbus.Interface(raw_server, 'org.bluez.Adapter1')
 
# The so-called documentation is at /usr/share/avahi/introspection/Server.introspect
print server
print server.StartDiscovery()
#print server.GetVersionString()
#print server.GetHostName()
