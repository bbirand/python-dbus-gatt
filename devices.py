from __future__ import absolute_import, unicode_literals

import dbus
import bluezutils

ADAPTER_DEV = "hci0"

bus = dbus.SystemBus()
manager = dbus.Interface(bus.get_object("org.bluez", "/"),
                 "org.freedesktop.DBus.ObjectManager")

objects = manager.GetManagedObjects()

for path in objects.keys():
    print "[ %s ]" % (path)
    interfaces = objects[path]
    for interface in interfaces.keys():
        #jif interface in ["org.freedesktop.DBus.Introspectable", "org.freedesktop.DBus.Properties"]:
        #j    continue

        if interface == 'org.bluez.Adapter1':
            print " %s" % (interface)
            properties = interfaces[interface]
            for key in properties.keys():
                print " %s = %s" % (key, properties[key]) 


# Get the device
adapter = dbus.Interface(bus.get_object("org.bluez", "/org/bluez/" + ADAPTER_DEV),
        "org.freedesktop.DBus.Properties")
#adapter = dbus.Interface(bus.get_object("org.bluez", "/org/bluez/hci0"),
#                 "org.bluez.Adapter1")

# Make sure the device is powered on
adapter.Set("org.bluez.Adapter1", "Powered", dbus.Boolean(1))
#print "Powered ", adapter.Get("org.bluez.Adapter1", "Powered") 

# Get the adapter interface for discovery
adapter = dbus.Interface(bus.get_object("org.bluez", "/org/bluez/hci0"),
                 "org.bluez.Adapter1")
adapter.StartDiscovery()
