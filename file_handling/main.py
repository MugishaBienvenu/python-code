# import csv
# try:
#     with open("workers.txt",mode="r") as file:
        
    
        
#       csv_reader=csv.DictReader(file)
        
#       data_list=[]
        
#       for row in csv_reader:
#           data_list.append(row)
            
            
#       for data in data_list:
#                 print(data)        
    
# except Error:
#     print("code have error")


import csv
try:
    
    
    fields=['name','class','date']

    rows=[['mugisha'],['l4sod'],['27/04/2025']]

    with open("workers.csv","w") as file:
        csv_writer=csv.writer(file)
        
        csv_writer.writerow(fields)
        csv_writer.writerows(rows)
        
except ErrorHandled:
    print("there is error in code")
    
else :
    print("there is no problem occured")          
    
finally:
    print("this code are pure")      
            