#!/usr/bin/env python3
"""
PDF merge(r)
$ pip install PyPDF2
"""
import os
from PyPDF2 import PdfMerger 

__version__ = "0.2.0" # 2023/02

path = "pdf2merge/" # os.curdir
output_name = "final.pdf"

files = [file for file in os.listdir(path) if file.endswith(".pdf")]
sorted_files = sorted(files)
print(sorted_files)

merger = PdfMerger() #PdfFileMerger
"""
PdfFileMerger is deprecated and was removed 
in PyPDF2 3.0.0. Use PdfMerger instead.
"""

#for file in os.listdir(path):
for file in sorted_files:
    print(file)
    merger.append(path + file)
    
merger.write(path + output_name)
