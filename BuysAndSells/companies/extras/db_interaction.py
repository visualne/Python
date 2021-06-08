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

    '''This function create insert query based on values sent in.'''
    def create_insert_query(self,**kwargs):

        #  Check to see what type of table it is
        if kwargs['table'] == 'russell3000':
            insert_query = (
                    'INSERT INTO russell3000' +
                    ' (SYMBOL,COMPANY) VALUES (\'' +
                    kwargs['data']['ticker'] + '\'' + ',' + '\'' +
                    kwargs['data']['company'] + '\'') + ');'
        elif kwargs['table'] == 'transactions':
            insert_query = (
                    'INSERT INTO transactions' +
                    ' (DATE,SYMBOL,TITLE,STORY_URL,PAGE_URL) VALUES (\'' +
                    data['date'] + '\'' + ',' + '\'' + data['symbol'] + '\'' +
                    ',' + '\'' + data['title'] + '\'' + ',' + '\'' +
                    data['link'] + '\'' + ',' + '\'' + data['page_url'] +
                    '\'' + ');')
        else:
            pass

        print(insert_query)

    '''This function inserts a specific record into a database.'''
    def insert(self,**kwargs):

        #  Creating insert query.
        insert_query = self.create_insert_query(**kwargs)

        print('Attempting to insert data')
        self.execute(insert_query)

    def execute(self,command):

        #  Changing database to webapp.
        self.cnx.database = 'webapp'

        #  Getting cursor object.
        cur = self.cnx.cursor(buffered=True)

        #  Executing mysql command
        try:
            #  Executing query
            cur.execute(command)
            self.cnx.commit()
            cur.close()
        except:
            print('Failure trying to insert data...')
            cur.close()


    def drop_create_table(self,**kwargs):
        if kwargs['table'] == 'russell3000':
            drop_russell3000_cmd = 'drop table russell3000;'
            self.execute(drop_russell3000_cmd)
            create_russell3000_table = ('create table russell3000(SYMBOL VARCHAR(10) NOT NULL,COMPANY VARCHAR(60) NOT NULL,PRIMARY KEY ( SYMBOL ))')
            self.execute(create_russell3000_table)
        else:
            pass