# pdf separator / extractor
import PyPDF2

__version__ = "0.1.5" # 2023/03


PAGE_NUM = 1
file = "hamikuvkoutek302"
input_file_path = f"data/{file}.pdf"
output_file_path = f"data/{file}_1.pdf"

with open(input_file_path, 'rb') as file: # Open in "rb" mode (read binary)
    #reader = PyPDF2.PdfFileReader(file)
    reader = PyPDF2.PdfReader(file)
    num_pages = len(reader.pages) # reader.numPages
    print(input_file_path, num_pages)
    page_number = PAGE_NUM - 1 # ? index
    
    # Check if the selected page is within the valid range of pages
    if page_number >= 0 and page_number < num_pages:
        # Create a new PDF writer object
        writer = PyPDF2.PdfWriter() # PyPDF2.PdfFileWriter()
        
        # Get the selected page and add it to the new PDF
        page = reader.pages[page_number] #reader.getPage(page_number)
        writer.add_page(page)
        
        # Save the new PDF to a file
        with open(output_file_path, 'wb') as output_file:
            writer.write(output_file)
            
        print('Page was successfully extracted.')
    else:
        print('Selected page is invalid.')
