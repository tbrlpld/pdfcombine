from PyPDF2 import PdfFileWriter, PdfFileReader
import argparse

#-----------------------------------------------------------------------
# Argument Parser
#-----------------------------------------------------------------------

parser = argparse.ArgumentParser(description='Merge two PDF files.')
parser.add_argument('pdf', type=str, nargs=2,
                    help='filepaths to the two PDF files to be merged')

args = parser.parse_args()
first_pdf_filepath = args.pdf[0]
second_pdf_filepath = args.pdf[1]

#-----------------------------------------------------------------------
# Run
#-----------------------------------------------------------------------

# Creating PDF objects
page_fronts_file = PdfFileReader(first_pdf_filepath, 'rb')
page_backs_file = PdfFileReader(second_pdf_filepath, 'rb')

output = PdfFileWriter()

# Get list of pages
page_fronts = page_fronts_file.pages
page_backs = page_backs_file.pages

# Number of pages
num_page_fronts = page_fronts_file.getNumPages()
num_page_backs = page_backs_file.getNumPages()

if num_page_backs != num_page_fronts:
    print("Number of page fronts and backs does not match.")
    raise ValueError
else:
    # Reverse page backs
    page_backs = page_backs[::-1]
    
    # Merging
    for i in range(0, page_fronts_file.getNumPages()):
        output.addPage(page_fronts[i])
        output.addPage(page_backs[i])
    
    with open('combined.pdf', 'wb') as f:
        output.write(f)