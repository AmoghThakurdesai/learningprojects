# on windows only and must have word installed
import win32com.client
import docx
wordFilename=input('your_word_document.docx')
pdfFilename=input('your_pdf_filename.pdf')

doc=docx.Document()
#code to create word doc goes here
doc.save(wordFilename)

wdFormatPDF=17#words numeric code for pdfs
wordObj=win32com.client.Dispatch('Word.Application')
docObj=wordObj.Documents.Open(wordFilename)
docObj.SaveAs(pdfFilename,FileFormat=wdFormatPDF)
docObj.Close()
wordObj.Quit()
