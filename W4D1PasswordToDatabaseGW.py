import uuid, hashlib, pymysql
username = input("Enter a username: ")
password = input("Enter a password: ")

salt = uuid.uuid4().hex
hashed_password = hashlib.sha512((password + salt).encode('utf-8')).hexdigest()
def setpassword():
    # Connect to the database
    connection = pymysql.connect(host='mrbartucz.com',
                             user='re7538jj',
                             password='re7538jj',
                             db='re7538jj_Passwords',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.Cursor)
    with connection.cursor() as cursor:
        insertSQL = "INSERT INTO Passwords (username, salt, hash) VALUES (%s,%s,%s)"
        insertVars = (username, salt, hashed_password)
        cursor.execute(insertSQL, insertVars)
        connection.commit()
    
setpassword()
usernameCheck = input("Please reenter your username: ")

def getSalt():
    # Connect to the database
    connection = pymysql.connect(host='mrbartucz.com',
                             user='re7538jj',
                             password='re7538jj',
                             db='re7538jj_Passwords',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.Cursor)

    with connection.cursor() as cursor:

        query = "SELECT Salt from Passwords WHERE username = %s "
        
        cursor.execute(query, usernameCheck)

        for result in cursor:
            foundSalt = ''.join(map(str, (result)))

        return foundSalt

def getHash():
    # Connect to the database
    connection = pymysql.connect(host='mrbartucz.com',
                             user='re7538jj',
                             password='re7538jj',
                             db='re7538jj_Passwords',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.Cursor)

    with connection.cursor() as cursor:

        query = "SELECT Hash from Passwords WHERE username LIKE %s "
        foundHash = ''
        cursor.execute(query, usernameCheck)
        for result in cursor:
            foundHash = ''.join(map(str, (result)))

        return foundHash

saltCheck = getSalt()
storedHash = getHash()
passwordCheck = input("Please reenter your password: ")
hashCheck = hashlib.sha512((passwordCheck + str(saltCheck)).encode('utf-8')).hexdigest()

if hashCheck == storedHash:
    print("your password is correct!")
else:
    print("your password is incorrect.")