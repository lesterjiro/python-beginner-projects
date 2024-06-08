import PyPDF2
import os

directory = input(r"Write the path of your PDFs>> ").strip('"')
output_filename = input("Write the name of the output>> ")

if not output_filename.endswith(".pdf"):
    output_filename += ".pdf"

output_path = os.path.join(directory, output_filename)
merger = PyPDF2.PdfMerger()

try:
    for file in os.listdir(directory):
        if file.endswith(".pdf"):
            file_path = os.path.join(directory, file)
            merger.append(file_path)

    with open(output_path, "wb") as ouput_file:
        merger.write(ouput_file)

    print(f"Your PDFs are merged into {output_filename}")

except Exception as e:
    print(e)
finally:
    merger.close()