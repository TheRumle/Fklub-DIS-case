# Methods
import psycopg2
import pygrametl

pgconn = psycopg2.connect(user='postgres', password='admin', host='localhost', database='f-klub')
connection = pygrametl.ConnectionWrapper(pgconn)
connection.setasdefault()
connection.execute('set search_path to public')

def pgcopybulkloader(name, atts, fieldsep, rowsep, nullval, filehandle):
    # Here we use driver-specific code to get fast bulk loading.
    # You can change this method if you use another driver or you can
    # use the FactTable or BatchFactTable classes (which don't require
    # use of driver-specifc code) instead of the BulkFactTable class.
    global connection
    curs = connection.cursor()
    curs.copy_from(file=filehandle, table=name, sep=fieldsep,
                   null=str(nullval), columns=atts)