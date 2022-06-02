import mysql.connector

print("Please type your Answer in option 👍")
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="fav"
)
mycursor = mydb.cursor()

print("")
print("")
print("What is Your Favourite Cuisine?")
print("a)Chinese")
print("b)Italian")
print("c)French")
print("d)Indian")
print("e)South Indian")
bla=str(input("Option: "))
d=bla.lower()

print("")
print("")
print("What is Your Second Favourite Cuisine?")
print("a)Chinese")
print("b)Italian")
print("c)French")
print("d)Indian")
print("e)South Indian")
bla=str(input("Option: "))
e=bla.lower()
print("")

print("")
print("")
print("What is Your Favourite Landform?")
print("a)Mountains")
print("b)Cities")
print("c)Beaches")
print("d)Forest")
print("e)Desert")
bla=str(input("Option: "))
f=bla.lower()
print("")

print("")
print("")
print("What is Your Favourite Colour?")
print("a)Blue")
print("b)Yellow")
print("c)Green")
print("d)Orange")
print("e)Red")
bla=str(input("Option: "))
a=bla.lower()
print("")

print("")
print("")
print("What is Your Favourite Subject?")
print("a)Social Studies")
print("b)Math")
print("c)Computers")
print("d)Science")
print("e)English")
bla=str(input("Option: "))
b=bla.lower()
print("")

print("")
print("")
print("What is Your Second Favourite Subject?")
print("a)Social Studies")
print("b)Math")
print("c)Computers")
print("d)Science")
print("e)English")
bla=str(input("Option: "))
c=bla.lower()
print("")



print("")
print("")
print("What is Your Favourite Sport?")
print("a)Cricket")
print("b)Soccer/Football")
print("c)Hockey")
print("d)Tennis/Table Tennis")
print("e)Basketball")
bla=str(input("Option: "))
g=bla.lower()
print("")



ii="INSERT INTO `fav`(`colour`, `subject`, `2subject`, `cousine`, `2cousine`, `landform`, `sport`) VALUES ('"+a+"'," \
                                                                    "'"+b+"','"+c+"','"+d+"','"+e+"','"+f+"','"+g+"')"

query=ii
mycursor.execute(query)
mydb.commit()


nq=0
def results(a):

    query = "SELECT COUNT(cousine) AS o FROM fav;"
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    for x in myresult:
      re=x
    t=re[0]


    query="SELECT COUNT(cousine) AS o FROM fav Where "+a+" ='a';"
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    for x in myresult:
      re=x
    oa=re[0]
    print("Option 1: "+str(oa/t*100)+"%")

    query="SELECT COUNT(cousine) AS o FROM fav Where "+a+" ='b';"
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    for x in myresult:
      re=x
    oa=re[0]
    print("Option 2: "+str(oa/t*100)+"%")

    query="SELECT COUNT(cousine) AS o FROM fav Where "+a+" ='c';"
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    for x in myresult:
      re=x
    oa=re[0]
    print("Option 3: "+str(oa/t*100)+"%")

    query="SELECT COUNT(cousine) AS o FROM fav Where "+a+" ='d';"
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    for x in myresult:
      re=x
    oa=re[0]
    print("Option 4: "+str(oa/t*100)+"%")

    query="SELECT COUNT(cousine) AS o FROM fav Where "+a+" ='e';"
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    for x in myresult:
      re=x
    oa=re[0]
    print("Option 5: "+str(oa/t*100)+"%")

    print("")



print("Question 1:")
results("cousine")

print("Question 2:")
results("2cousine")

print("Question 3:")
results("landform")

print("Question 4:")
results("subject")

print("Question 5:")
results("2subject")

print("Question 6:")
results("sport")
mydb.close()

