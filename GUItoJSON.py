#Added a new comment by Ramesh C - 29/05/2020
import tkinter as tk
from tkinter import ttk

if __name__ == "__main__": 

    def set_dpi_awareness():
        try:
            from ctypes import windll
            windll.shcore.SetProcessDpiAwareness(1)
        except:
            pass

    set_dpi_awareness()
    
    # create a GUI window 
    root = tk.Tk() 
    # set the configuration of GUI window 
    root.geometry("600x400")
    root.resizable(False,False)    

    # set the title of GUI window
    root.title("Student Academic information")

    # set the background colour of GUI window 
    root.configure()
    
    root.columnconfigure(0, weight=1)
        
    input_frame = ttk.Frame(root, padding=(20,10,20,0))
    input_frame.grid(row=0, column=0, sticky="EW")

    formheadingLabel = ttk.Label(input_frame, text="Student Information",font='Helvetica 10 bold')
    #formheadingLabel.config(font=("Segoe UI",10))
    formheadingLabel.grid(row=0, column=1 ,padx=(0,10))
     
    # create a Student ID label 
    StudentidLabel = ttk.Label(input_frame, text="Student ID", font='Helvetica') 
    StudentidLabel.grid(row=1, column=0, sticky="EW")
      
    # create a Student Name label 
    StudentnameLabel = ttk.Label(input_frame, text="Student Name", font='Helvetica') 
    StudentnameLabel.grid(row=2, column=0, sticky="EW")
    
    # create a Student Course label 
    StudentcourseLabel = ttk.Label(input_frame, text="Student Course", font='Helvetica') 
    StudentcourseLabel.grid(row=3, column=0, sticky="EW")
      
    # create a Student Email lable 
    StudentemailLabel = ttk.Label(input_frame, text="Student Email", font='Helvetica') 
    StudentemailLabel.grid(row=4, column=0, sticky="EW")
      
       
    # create a text entry box 
    # for typing the information 
    StudentidEntry = ttk.Entry(input_frame,width=15)
    StudentidEntry.grid(row=1, column=1)
    StudentidEntry.focus()
    
    StudentnameEntry = ttk.Entry(input_frame,width=15) 
    StudentnameEntry.grid(row=2, column=1)
    
    
    StudentcourseEntry = ttk.Entry(input_frame,width=15) 
    StudentcourseEntry.grid(row=3, column=1)
    

    StudentemailEntry = ttk.Entry(input_frame,width=15)
    StudentemailEntry.grid(row=4, column=1)

    labels = ttk.Frame(root, padding=(20,10))
    labels.grid()

    lblMsg = ttk.Label(labels, font='Helvetica') 
    lblMsg.grid(row=8, column=1)
    
    # Function for clearing the 
    # contents of text entry boxes 

    def clear(): 
          
        # clear the content of text entry box 
        
        StudentidEntry.delete(0, END) 
        StudentnameEntry.delete(0, END) 
        StudentcourseEntry.delete(0, END) 
        StudentemailEntry.delete(0, END) 
        
#--------------------------------------------------------------------------------
    def insert(): 
                
        InStudid = StudentidEntry.get()
        InStudname = StudentnameEntry.get()
        InStudcourse = StudentcourseEntry.get()
        InStudemail = StudentemailEntry.get()
        #print("%s %s %s %s" %(InStudid,InStudname,InStudcourse, InStudemail))

        
        #-----------------------------------Python code to create a txt file from console.--------------------------------------------------
        import os
            
            #python code to create a txt file from console.

        if(os.path.exists("studrecord.txt")):
            
            fob1=open("studrecord.txt","a")
            fob1.write("%s\t %s\t %s\t %s\n" %(InStudid,InStudname,InStudcourse,InStudemail))
            fob1.close() # saves data in file and then exits
            #print("Record appended to the existing record in the txt file sucessfully.....")
            lblMsg.configure(text="Record appended to the existing record in the txt file sucessfully.....")
        else:

            fob1=open("studrecord.txt","w")
            fob1.write("%s\t %s\t %s\t %s\n" %(InStudid,InStudname,InStudcourse,InStudemail))
            #print("Text file created sucessfully.....")
            lblMsg.configure(text="Text file created sucessfully.....")
            fob1.close() # saves data in file and then exits

        #------------------------------Python code to write the data from the text file to csv.----------------------------------------------

        #Before writing make sure to check the csv in the path and also check the existing records in the csv file.

        #Python code to read the data from the csv file to check for the existing records.

        #import re #Calling the regular expression.

        class Student:
            def __init__(self, idno, name, course, email):
                self.idno = idno
                self.name = name
                self.course = course
                self.email = email
            def __str__(self):
                return str(self.__dict__)
            
        if(os.path.exists("studrecord.csv")): 
            csvobj1=open("studrecord.csv","r")
            data1=csvobj1.readlines()
            csvobj1.close()

            listStudents = []
            newlist1 = []
            
            for l in data1:
                ln=l.title()  #Read as string data
                #result=re.sub(',',' ',ln) #To remove the comma from the string using regular expression.
                ln = ln.replace("\t", "").replace("\n","").replace("\"","")
                data = ln.split(",")
                s1 = Student(data[0],data[1],data[2],data[3])
                if (s1.idno != "Studid"):
                    newlist1.append(s1.idno)
                    listStudents.append(s1)


        #python code to read the file created above and write to a csv.

        fob2=open("studrecord.txt","r")
        data=fob2.readlines()#Read the line from the txt file.
        fob2.close()
        u=0
        for line in data:

            word = line.split() #split the line into words store it as list.
             
            if(os.path.exists("studrecord.csv")):
                csvobj=open("studrecord.csv","a")
                if any(word[0] == s for s in newlist1):
                    pass
                else:
                    for j in word:
                        csvobj.writelines("%s\t," %(j))
                    csvobj.writelines("\n")
                    s2 = Student(word[0],word[1],word[2],word[3])
                    listStudents.append(s2)
                    #print("Record appended to the existing record in the csv sucessfully.....")
                    lblMsg.configure(text="Record appended to the existing record in the csv sucessfully.....")
                    csvobj.close()
            else:
                csvobj=open("studrecord.csv","w")
                csvobj.write("studid\t, studname\t, Studcourse\t, studemailid\n") #Header data added to indentify the data in excel.
                for j in word:
                    csvobj.writelines("%s\t," %(j))
                csvobj.writelines("\n")
                #print("CSV Created Sucessfully")
                lblMsg.configure(text="CSV Created Sucessfully")
                csvobj.close()


        #--------------------------Python code to insert the data from CSV to Mysql database.-----------------------------------------------

        import mysql.connector
        from mysql.connector import connect

        #First i am connecting to the mysql database server
        connection = mysql.connector.connect(host='localhost',database='university',user='ramesh',password='ramRAT001$')
                                     
        #Opening the cursor for select to check for duplicate
        c1 = connection.cursor()

        c1.execute("select studid from studinfo")
        v1=c1.fetchall()

        #Opening the cursor for Insert
        c2 = connection.cursor()  #create cursor object to execute the sql queryies from python code
          

        #Set the query

        for x in listStudents:
            sidno=int(x.idno)
            sname=x.name 
            scourse=x.course
            semail=x.email
            #print("%d %s %s %s" %(sidno,sname,scourse,semail))
            try:
                insertquery="insert into studinfo values('%d','%s','%s','%s')"%(sidno,sname,scourse,semail)
                #execute the queries
                c2.execute(insertquery)    
                #print("Record sucessfully inserted into MySql Table studinfo")
                lblMsg.configure(text="Record sucessfully inserted into MySql Table studinfo")
            except:
                #print("Duplicate record...")
                continue

        connection.commit() #to save the changes in the database table.
        c1.close()
        c2.close()
        connection.close()

        #--------------------Python code to read the record from MySql and create xml using ElementTree.--------------------------------------

        import xml.etree.cElementTree as ET

        connection = mysql.connector.connect(host='localhost',database='university',user='ramesh',password='ramRAT001$')
        c3 = connection.cursor()
        c3.execute("select * from studinfo")
        record = c3.fetchall()

        StudInfo = ET.Element("StudInfo")
           
        for d1 in record:
            #print("%d %s %s %s" %(d1[0],d1[1],d1[2],d1[3]))
            StudentRec = ET.SubElement(StudInfo,"StudentRec")
            studid = ET.SubElement(StudentRec,"studid")
            studname = ET.SubElement(StudentRec,"studname")
            studcourse = ET.SubElement(StudentRec,"studcourse")
            studemailid = ET.SubElement(StudentRec,"studemailid")

            studid.text=str(d1[0])
            #print(studid.text)
            studname.text=str(d1[1])
            #print(studname.text)
            studcourse.text=str(d1[2])
            #print(studcourse.text)
            studemailid.text=str(d1[3])
            #print(studemailid.text)
            
        tree = ET.ElementTree(StudInfo)
        tree.write("studinfo.xml")
        #print("Moved the data from MySQL table StudInfo to XML using ElementTree")
        lblMsg.configure(text="Moved the data from MySQL table StudInfo to XML using ElementTree")
        c3.close()
        connection.close()

        #Student Info XML format.
        """
        <StudentInfo>
            <StudentRec>
                <studid>content</studid>
                <studname>content</studname>
                <studcourse>content</studcourse>
                <studemail>content</studemail>
            </StudentRec>
        </StudentInfo>

        """
        #-------------------------Python code to read the XML using DOM API and create a JSON file.----------------------------------------

        from xml.dom import minidom
        import json as js

        myxml = minidom.parse('studinfo.xml')

        def serialize(obj):
            return obj.__dict__

        Sr1 = myxml.getElementsByTagName("StudentRec")
        fjson = open('studinfo.json', 'w')
        slfordom = []
        for StudentRec in Sr1:
                studid = StudentRec.getElementsByTagName("studid")[0]
                studname = StudentRec.getElementsByTagName("studname")[0]
                studcourse = StudentRec.getElementsByTagName("studcourse")[0]
                studemailid = StudentRec.getElementsByTagName("studemailid")[0]
                s3 = Student(studid.firstChild.data,studname.firstChild.data,studcourse.firstChild.data,studemailid.firstChild.data)
                slfordom.append(s3)
                
        fjson.write(js.dumps(slfordom,default=serialize,sort_keys=False, indent=4))
        #print("JSON file created from XML using DOM API")
        lblMsg.configure(text="JSON file created from XML using DOM API")
        fjson.close()

        #JSON format

        """
        [
            {
                "idno": "1",
                "name": "Ramesh",
                "course": "Phd",
                "email": "Ramesh@Gmail.Com"
            },
            {
                "idno": "2",
                "name": "Rathnavs",
                "course": "Phd",
                "email": "Rathnavs@Gmail.Com"
            }

        ]

        """
        #----------------------------------------------------------END--------------------------------------------------------------------

    def qExit(): 
        root.destroy() 

    buttons = ttk.Frame(root, padding=(20,10))
    buttons.grid(sticky="EW")

    buttons.columnconfigure(0,weight=1)
    buttons.columnconfigure(1,weight=1)
    buttons.columnconfigure(2,weight=1)
    
    submit = ttk.Button(buttons, text="Submit", command=insert)
    submit.grid(row=6, column=0, sticky="EW")
    
    clearbutton = ttk.Button(buttons, text="Clear", command=clear)
    clearbutton.grid(row=6, column=1, sticky="EW")
            
    btnExit = ttk.Button(buttons, text = "Exit", command = qExit)
    btnExit.grid(row=6, column=2, sticky="EW")
  
    root.mainloop() 



