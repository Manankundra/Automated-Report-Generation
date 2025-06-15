# importing required liberaries
import pandas as pd
from fpdf import FPDF

# loading CSV
df = pd.read_csv("employees.csv")
# print(df)

# Analysis
Total_employees = len(df)
Average_salary = df["SALARY"].mean()
Max_salary = df["SALARY"].max()
Min_salary = df["SALARY"].min()

Top_earner = df[df["SALARY"] == Max_salary][["FIRST_NAME", "LAST_NAME"]].values[0]

Recent_hires = df.tail(5)

# creating PDF report 
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", 'B', 16) 

# color
pdf.set_fill_color(230, 240, 255)
pdf.rect(5, 5, 200, 287, 'F')   

# Title
pdf.set_font("Arial", 'B', 16)
pdf.cell(200 , 10 , "Employee Salary Report", ln = True , align = 'C' , border=1)
pdf.ln(10)

# Stats
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, f"Total Employees: {Total_employees}", ln=True ,border=1)
pdf.cell(200, 10, f"Average Salary: INR {round(Average_salary)}", ln=True ,border=1)
pdf.cell(200, 10, f"Highest Salary: INR {Max_salary} (by {Top_earner[0]} {Top_earner[1]})", ln=True ,border=1)
pdf.cell(200, 10, f"Lowest Salary: INR {Min_salary}", ln=True ,border=1)
pdf.ln(10)

recent_hires_text = Recent_hires[["FIRST_NAME", "LAST_NAME", "HIRE_DATE", "SALARY"]].to_string(index=False)
pdf.set_font("Arial", size=12)
pdf.multi_cell(0, 10, recent_hires_text ,border=1)

# Save the pdf
pdf.output("employee_report.pdf")
