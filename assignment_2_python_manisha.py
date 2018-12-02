## Accessing mysql database from python

#import modules
import pymysql

#open a database connection
db = pymysql.connect("localhost", "root", "mysql*11", "sakila")

# prepare a cursor object
cursor = db.cursor()

## Homework Query

# sql query

sql = """ select F.title, F.description, A.first_name, A.last_name from sakila.film F, sakila.film_actor FA ,sakila.actor A where lower(F.title) like lower('y%') and FA.film_id = F.film_id and FA.actor_id = A.actor_id """

# try exception block
try:

    # execute the sql command
    cursor.execute(sql)

    # fetch all of the rows in a list of lists
    results = cursor.fetchall()

    # print header
    print("Title\t\tDescription\t\t\t\t\t\t\t\t\t\t\t\t\t\tFirst\tLastNaame")

    # print result
    for row in results:
        title = row[0]
        Desc = row[1]
        first_name =row[2]
        last_name = row[3]

        # print each row
        print("%s\t%s\t%s\t%s" % (title, Desc, first_name, last_name ))

except:
    print("Error: unable to fetch data")

    
        
    


    
