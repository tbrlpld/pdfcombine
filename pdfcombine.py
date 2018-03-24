from PyPDF2 import PdfFileWriter, PdfFileReader

page_fronts_file = PdfFileReader('example/fronts123.pdf', 'rb')
page_backs_file = PdfFileReader('example/backs321.pdf', 'rb')

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