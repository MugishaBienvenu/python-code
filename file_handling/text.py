# file=open("my_file.txt","w")
# try:
    
#     for i in range(3):
#        file.write("in python you must be know file handling and exception handling ,\n in file handling have some keyword : read,write and open ,close file ,\n in exception have some keyword: try,except,else and finally : No:%d  \n" % i)


# finally:
#     file.close()

# with open("D:\\files\\my_file.txt","w") as file :
#      for i in range(3):
#          file.write("in python you must be know file handling and exception handling ,\n in file handling have some keyword : read,write and open ,close file ,\n in exception have some keyword: try,except,else and finally : No:%d  \n" % i)

try:
     with open("workers.csv","r") as file:

           x =file.read()
           print(x)

     file.close()
except:
      print("no file found")     