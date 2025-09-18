# AUTOMATED-REPORT-GENERATION
COMPANY: CODTECH IT SOLUTIONS NAME: Rishabh Ramesh Singh INTERN ID: CTO8DZ264 DOMAIN: PYTHON DURATION: 8 WEEK MENTOR: NEELA SANTOSH



---

# Sales Report Generator

## 📌 Overview

This project reads sales data from a CSV file, analyzes it, and generates a PDF report containing:

* Individual sales details
* Total sales
* Average sales
* Top seller information

The PDF output is neatly formatted for easy reading.

## 🗂 Project Structure

```
.
├── data.csv               # Input CSV file containing sales data
├── task2.py               # Main Python script for processing data and generating PDF
├── sales_report.pdf       # Generated PDF report with analyzed sales data
└── README.md              # Project documentation
```

## ⚙️ How It Works

1. **Read CSV Data**

   * The script reads sales data from `data.csv`.
   * Extracts names and sales values.

2. **Analyze Data**

   * Calculates total sales.
   * Finds average sales.
   * Identifies the top seller and their sales amount.

3. **Generate PDF Report**

   * Creates a PDF titled **"Sales Report"**.
   * Lists each person's sales, total, average, and top seller details.

## 📊 Example Output (From `sales_report.pdf`)

```
Sales Report

Riya: 1500  
Harshita: 1500  
Satish: 2000  

Total Sales: 5000  
Average Sales: 1666.67  
Top Seller: Satish (2000)
```

## 🚀 How to Run the Script

1. **Install Dependencies**

   ```bash
   pip install fpdf
   ```
2. **Run the Script**

   ```bash
   python task2.py
   ```
3. **View the PDF**

   * The report will be saved as `sales_report.pdf` in the project folder.

## 🛠 Requirements

* Python 3.x
* `fpdf` library for PDF generation
* A CSV file (`data.csv`) with columns:

  ```
  Name,Sales
  ```

## ✨ Features

* Simple and easy to use.
* Automatically calculates sales statistics.
* Generates a clean, ready-to-share PDF report.

---

If you want, I can also **add a code block in README that shows a sample `data.csv`** so users can test your script immediately. Would you like me to do that?
