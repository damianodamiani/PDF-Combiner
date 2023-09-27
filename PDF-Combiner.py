import PyPDF2
import os

# List of PDF files to combine
pdf_files = ["file1.pdf", "file2.pdf", "file3.pdf"]  # Replace with the actual file paths of the PDFs you want to merge

# Create a PDF merger object
pdf_merger = PyPDF2.PdfMerger()

# Add each PDF to the merger
for pdf_file in pdf_files:
    pdf_merger.append(pdf_file)

# Output file name
output_pdf_name = "PDF_combined.pdf"  # Replace with the desired name for the merged PDF file

# Specify the output directory for the merged PDF file
output_directory = "/path/to/output/directory/"  # Replace with your desired output directory path

# Ensure the output directory exists or create it
os.makedirs(output_directory, exist_ok=True)

# Create the full output PDF file path
output_pdf = os.path.join(output_directory, output_pdf_name)

# Write the merged PDF to the output file
pdf_merger.write(output_pdf)

# Close the merger
pdf_merger.close()

print(f"PDFs merged into {output_pdf}")
