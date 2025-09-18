import csv
from fpdf import FPDF

# Step 1: Read and analyze data from CSV
def analyze_data(file_path):
    names = []
    sales = []
    
    with open("D:\internship task\Task 2\Task 2\data.csv", 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            names.append(row['Name'])
            sales.append(int(row['Sales']))
    
    total_sales = sum(sales)
    average_sales = total_sales / len(sales)
    max_sale = max(sales)
    max_person = names[sales.index(max_sale)]

    return {
        "names": names,
        "sales": sales,
        "total_sales": total_sales,
        "average_sales": average_sales,
        "top_seller": max_person,
        "top_sale": max_sale
    }

# Step 2: Generate PDF report
def generate_pdf_report(data, output_file):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Sales Report", ln=True, align='C')
    pdf.ln(10)

    for name, sale in zip(data["names"], data["sales"]):
        pdf.cell(200, 10, txt=f"{name}: {sale}", ln=True)

    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Total Sales: {data['total_sales']}", ln=True)
    pdf.cell(200, 10, txt=f"Average Sales: {data['average_sales']:.2f}", ln=True)
    pdf.cell(200, 10, txt=f"Top Seller: {data['top_seller']} ({data['top_sale']})", ln=True)

    pdf.output(output_file)

# Step 3: Run the functions
if __name__ == "__main__":
    file_path = "D:\internship task\Task 2\Task 2\data.csv"
    report_data = analyze_data(file_path)
    generate_pdf_report(report_data, "sales_report.pdf")
    print("Report generated: sales_report.pdf")