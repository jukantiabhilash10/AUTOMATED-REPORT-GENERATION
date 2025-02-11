import os
import pandas as pd
from fpdf import FPDF

def read_data(file_path):
    """Reads AI-related data from a CSV file into a Pandas DataFrame."""
    return pd.read_csv(file_path)

def analyze_data(df):
    """Performs analysis on AI-related data."""
    return {
        'Total AI Topics': len(df),
        'Average Impact Score': df['Impact Score'].mean(),
        'Key Areas': df['Topic'].tolist(),
        'Descriptions': dict(zip(df['Topic'], df['Description']))
    }

def generate_pdf_report(summary, output_file):
    """Generates a PDF report on the Importance of AI using FPDF."""
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, "The Importance of AI", ln=True, align='C')
    pdf.ln(10)

    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, f"Total AI Topics Covered: {summary['Total AI Topics']}", ln=True)
    pdf.cell(200, 10, f"Average Impact Score: {summary['Average Impact Score']:.2f}", ln=True)
    pdf.ln(10)

    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, "Key Areas Where AI is Important:", ln=True)
    pdf.set_font("Arial", size=12)
    
    for topic in summary['Key Areas']:
        pdf.cell(200, 10, f"- {topic}", ln=True)
    pdf.ln(10)

    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, "Brief Descriptions:", ln=True)
    pdf.set_font("Arial", size=12)

    for topic, desc in summary['Descriptions'].items():
        pdf.cell(200, 10, f"{topic}: {desc}", ln=True)
        pdf.ln(5)

    pdf.output(output_file)
    print(f"Report generated: {output_file}")
    os.system(f'code "{output_file}"')  # Open in VS Code

if __name__ == "__main__":
    file_path = "data.csv"  # Input CSV file with AI-related topics
    output_file = "AI_Report.pdf"  # Output PDF file
    
    try:
        df = read_data(file_path)
        summary = analyze_data(df)
        generate_pdf_report(summary, output_file)
    except FileNotFoundError:
        print("Error: ai_data.csv not found. Please make sure the file exists in the same directory.")
    except Exception as e:
        print(f"An error occurred: {e}")
