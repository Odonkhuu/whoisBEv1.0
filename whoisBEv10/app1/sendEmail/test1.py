import psycopg2 



pgDbName   = "dbwhois"
pgUser     = "uwhois"
pgHost     = "202.131.254.138"
pgPassword = "whoispass"
pgPort     = "5938"

def connectDB():
    con = psycopg2.connect(
        dbname   = pgDbName,
        user     = pgUser,
        host     = pgHost,
        password = pgPassword,
        port     = pgPort,
    )
    return con

def disconnectDB(con):
    if(con):
        con.close()
        # is email overlaped
def emailExists(email):
    myCon = connectDB()
    userCursor = myCon.cursor()
    # userCursor.execute('SELECT COUNT(*) FROM "f_user" WHERE "email" = %s', (email,))
    # result = userCursor.fetchone()
    userCursor.execute('UPDATE "f_user" SET "pass" = %s WHERE "email" = %s', ('passs', email,))
    myCon.commit()
    userCursor.close()
    disconnectDB(myCon)
    # return result[0] > 0
        # userCursor.execute('SELECT * FROM "f_user" WHERE "id" = %s', (id,))
        # user = userCursor.fetchone()
        
        # # Update the password
        # userCursor.execute('UPDATE "f_user" SET "pass" = %s WHERE "id" = %s', (pas, id))
        

myCon = connectDB()

# print(myCon)

print(emailExists('odonkhuu4@gmail.com'))

disconnectDB(myCon)