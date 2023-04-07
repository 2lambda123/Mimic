from os import environ
import sqlite3
# or: from autobahn.asyncio.wamp import ApplicationSession

conn = sqlite3.connect('/dev/shm/tdrs.db')
conn.isolation_level = None
c = conn.cursor()



c.execute("UPDATE tdrs SET TDRS1 = %s" % str("TDRS-10"));
c.execute("UPDATE tdrs SET TDRS2 = %s" % str("TDRS-7"));
c.execute("UPDATE tdrs SET Timestamp = %s" % str(5));
