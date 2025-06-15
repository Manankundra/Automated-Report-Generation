*topic : Automated-Report-Generation
*COMPANY: CODTECH IT SOLUTIONS 
*NAME: Manan Kundra 
*INTERN ID: : CT04DM447 
*DOMAIN:: Python Programming 
*DURATION: 4 weeks 
*MENTOR: NEELA SANTOSH

# 📊 Automated Employee Report Generator using Python

This Python script reads employee data from a CSV file, analyzes key salary statistics, and automatically generates a well-formatted PDF report using the `FPDF` library.

## 🧰 Features

- Reads and processes employee data from a `.csv` file
- Computes:
  - Total number of employees
  - Average salary
  - Highest and lowest salary
  - Top earning employee
- Displays details of the most recent 5 hires
- Creates a visually styled PDF report with all statistics and a summary table

## ⚙️ Tech Stack

- Python 3
- `pandas` for data handling
- `fpdf` for PDF generation

## 📁 Input Format

The input CSV file should be named `employees.csv` and include the following columns:
- `FIRST_NAME`
- `LAST_NAME`
- `HIRE_DATE`
- `SALARY`
