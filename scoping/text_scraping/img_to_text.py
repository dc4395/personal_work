import pandas as pd
import easyocr

###############################################################

#JPEG Example

###############################################################

jpg_path = r"./scoping/text_scraping/sale_label_example.jpg"

reader = easyocr.Reader(['en'])

result = reader.readtext(jpg_path, detail = 0)

print(result) 