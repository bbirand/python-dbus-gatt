#!/usr/bin/env python
#
# This file is part of python-tdbus. Python-tdbus is free software
# available under the terms of the MIT license. See the file "LICENSE" that
# was provided together with this source file for the licensing terms.
#
# Copyright (c) 2012 the python-tdbus authors. See the file "AUTHORS" for a
# complete list.

# This example shows how to access Avahi on the D-BUS.


from tdbus import SimpleDBusConnection, DBUS_BUS_SYSTEM, DBusHandler, signal_handler, DBusError

import logging

logging.basicConfig(level=logging.DEBUG)

# = 'org.freedesktop.Avahi'
#PATH_SERVER = '/'
#IFACE_SERVER = 'org.freedesktop.Avahi.Server'

conn = SimpleDBusConnection(DBUS_BUS_SYSTEM)

try:
    bluez = conn.call_method('/', 'GetManagedObjects',
              interface='org.freedesktop.DBus.ObjectManager', 
              destination='org.bluez')
except DBusError:
    print "Bluez not available"
    raise

var = bluez.get_args()[0]
for p, dev  in var.iteritems():
    if 'org.bluez.Adapter1' in dev:
        print "Found adapter {}".format(p)
        adapter = p


#
# Get device name
#
bluez = conn.call_method(adapter, 'Get',
          interface='org.freedesktop.DBus.Properties', 
          format = 'ss', 
          args=('org.bluez.Adapter1', 'Powered'),
          destination='org.bluez')

print bluez.get_args()[0]
# Returns:
# ('b', False)

bluez = conn.call_method(adapter, 'Set',
          interface='org.freedesktop.DBus.Properties', 
          format = 'ssu', 
          args=('org.bluez.Adapter1', 'Powered', True),
          destination='org.bluez')


import sys
sys.exit()

print 'Avahi is available at %s' % CONN_AVAHI
print 'Avahi version: %s' % result.get_args()[0]
print
print 'Browsing service types on domain: local'
print 'Press CTRL-c to exit'
print

result = conn.call_method('/', 'ServiceTypeBrowserNew', interface=IFACE_SERVER,
                    destination=CONN_AVAHI, format='iisu', args=(-1, 0, 'local', 0))
browser = result.get_args()[0]
print browser
class AvahiHandler(DBusHandler):

    @signal_handler()
    def ItemNew(self, message):
	args = message.get_args()
    	print 'service %s exists on domain %s' % (args[2], args[3])

conn.add_handler(AvahiHandler())
conn.dispatch()
