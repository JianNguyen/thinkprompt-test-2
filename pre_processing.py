import os


def list_file(path):
    for f in os.listdir(path):
        if os.path.isdir(path + "/" + f):
            list_file(path + "/" + f)
        else:
            f = f.split(".")
            if f[-1] == "pdf":
                print(path)
            if f[-1] not in d_format:
                d_format.append(f[-1])

data_path = "data"
folders = os.listdir(data_path)
d_format = []
text_file = ["txt", "csv", "json", "xml"]
data_file = ["csv", "xlsx", "tsv", "json"]
image_file = ["jpg", "jpeg", "png", "png", "tiff"]
audio_file = ["wav", "aiff", "mp3"]
video_file = ["mp4", "avi", "mov"]
document_file = ["pdf", "docx", "xlsx", "pptx"]
spreadsheet_file = ["xls", "xlsx"]
notebook_file = ["py", "js", "html", "css"]
binary_file = ["bin", "dat"]
dataset_file = ["arff", "data", "database"]


for folder in folders:
    if os.path.isdir(data_path + "/" + folder):
        list_file(data_path + "/" + folder)
    else:
        folder = folder.split(".")
        print(folder)
        if folder[-1] == "pdf":
                print(data_path)
        if folder[-1] not in d_format:
            d_format.append(folder[-1])

print(d_format)