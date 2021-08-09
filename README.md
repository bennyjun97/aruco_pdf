# aruco_pdf
Python code for creating pdf with Aruco Markers. User can write the text file for each pdf either manually or with another python code.

Below is a sample text file, also included in this repository as 'sample.txt'.


FORMAT: A4
ORIENTATION: PORTRAIT
UNIT: mm
LIBRARY: DICT_6X6_250

5 48 200 1

5 48 200 2


This file will create pdf with A4 format, portrait orientation, unit in mm, and markers with dictionary 'DICT_6X6_250'.
Running pdf_generator.py with filename as 'sample' will generate a pdf with two pages with one marker on each page.

For each line, first two numbers denote the x and y coordinates within the page with defined unit.
Third number denotes the size of each marker, also with defined unit.
Last number denotes the ID of each marker.
Blank line creates a new blank page.

To create a custom pdf, either manually create a file with the same format, or run txt_generator.py after editing the settings and the write() function.
