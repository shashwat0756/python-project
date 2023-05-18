import PySimpleGUI as sg
from zip_creator import make_achive

label1 = sg.Text("Select files to compress")
input1 = sg.Input()
button_1 = sg.FileBrowse("Choose",key="files")
label2 = sg.Text("select destination folder")
input2 = sg.Input()
button_2 = sg.FolderBrowse("choose",key = "folder")
button = sg.Button("compress")
window = sg.Window("File compressor",layout = [[label1,input1,button_1],[label2,input2,button_2],[button]])
while True:
   event,values = window.read()
   print(event,values)
   filepaths = values["files"].split(";")
   folder = values["folder"]
   make_achive(filepaths,folder)

window.close()



