from datetime import date
import pandas as pd
import json
import xlwt
from xlwt import Workbook
from flask import Flask , render_template
import xlsxwriter


skills_app = Flask(__name__)

# workbook = xlsxwriter.Workbook('Book1.xlsx')
# worksheet = workbook.add_worksheet()

# my_list = ["HTML","JS"]

# for row_num, data in enumerate(my_list):
#     worksheet.write(0, row_num , data)

# workbook.close() 


#MyCourrses=['oop','Math','ds','english']

data = pd.read_excel (r'C:\Users\Mai Mostafa\Desktop\python\Book1.xlsx') 


@skills_app.route("/")

def homepage():
    return render_template("courses.html", 
                            pagetitle="courses",
                            page_head="Courses Page",
                            custom_css="home",
                            course=data)



if __name__ =="__main__":
    skills_app.run(debug=True,port=9000)


