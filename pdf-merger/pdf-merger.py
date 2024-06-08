import PyPDF2
import os

# Get the directory path containing the PDFs from the user
directory = input(r"Write the path of your PDFs>> ").strip('"')

# Get the output filename from the user
output_filename = input("Write the name of the output>> ")

# Ensure the output filename ends with '.pdf'
if not output_filename.endswith(".pdf"):
    output_filename += ".pdf"

# Create the full path for the output file
output_path = os.path.join(directory, output_filename)

# Initialize the PdfMerger object
merger = PyPDF2.PdfMerger()

try:
    # Iterate through each file in the directory
    for file in os.listdir(directory):
        # Check if the file is a PDF
        if file.endswith(".pdf"):
            # Get the full file path
            file_path = os.path.join(directory, file)
            # Append the PDF to the merger
            merger.append(file_path)

    # Write the merged PDF to the output file
    with open(output_path, "wb") as output_file:
        merger.write(output_file)

    print(f"Your PDFs are merged into {output_filename}")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the merger to free up resources
    merger.close()