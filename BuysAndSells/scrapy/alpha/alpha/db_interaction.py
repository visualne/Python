import mysql.connector
#  This class will
#     Connect to a database - mysql used right now.
#     Retrieve data from the database.
#     Store data in a database.

class db_interaction:
    def __init__(self,host,username,password):
        self.host = host
        self.username = username
        self.password = password


    def connect(self):
        try:
            self.cnx = mysql.connector.connect(user=self.username,
                                               password=self.password,
                                               host=self.host)

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)

    '''This function inserts a specific record into a database.'''
    def insert(self,**kwargs):

        #  Changing database to webapp.
        self.cnx.database = 'webapp'

        #  Getting cursor object.
        cur = self.cnx.cursor(buffered=True)

        #  Arguments for inserting into transactions table.

        #  Arguments for inserting data from file into a table.
        insert_transactions_table_args = ['table','data']


        #  Checking for insert into table.
        if sorted(insert_transactions_table_args) == sorted(list(kwargs.keys())):
            table = kwargs['table']
            data = kwargs['data']

            for k,v in data.items():
                print(k,v)

            insert_query = (
                    'INSERT INTO ' + table +
                    ' (DATE,SYMBOL,TITLE,STORY_URL,PAGE_URL) VALUES (\'' +
                    data['date'] + '\'' + ',' + '\'' + data['symbol'] + '\'' +
                    ',' + '\'' + data['title'] + '\'' + ',' + '\'' +
                    data['link'] + '\'' + ',' + '\'' + data['page_url'] +
                    '\'' + ')')

            #  Adding entry to table.
            print(insert_query)

        #  Inserting data
        try:
            #  Executing query
            cur.execute(insert_query)
            self.cnx.commit()
            cur.close()
        except:
            print('Failure trying to insert data...')
            cur.close()