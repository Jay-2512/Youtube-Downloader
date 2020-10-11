from tkinter import *
import youtube_dl
import os
import shutil


root = Tk()
root.title("You Tube Downloader")
root.geometry("700x500")
root.configure(bg="#0f1f3b")
root.resizable(FALSE,FALSE)
global path
path = r"C:\Users\Public\Music\YT_Music"


global dest
dest = path

#--functions--#
def makeDirectory(file, path):      
    try:
        os.mkdir(path)
        print("Directory created")
    except FileExistsError:
        print("Folder Found")
    
    moveFile(file, dest)


def moveFile(file, dest):
    for file in os.listdir("./"):
        if file.startswith("YoutubeAudioDownloader"):
            shutil.move(file, dest)

def downloadAudio():

    url  = get_urlEntry.get()
    try:
        configLabel.config(text="Downloaded : C:\\Users\\Public\\Public Music\\YT_Music")
        ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                print("Download audio now. \n")
                ydl.download([url])

        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                old_file_name = file
                new_file_name = "YoutubeAudioDownloader " + old_file_name
                print(new_file_name)
                os.rename(old_file_name, new_file_name)
                makeDirectory(file, path)
    except:
        if url == " ":
            print("EE")



#--heading--#
heading = Label(root,bg="#0f1f3b",fg="white", text="YT DOWN")
heading.config(font=("Courier", 33))
heading.pack()
footer = Label(root,bg="#0f1f3b",fg="white",text="github.com/Jay-2512").pack(side=BOTTOM)

#--underline--#
underlineLabel = Label(root,text="-------------------------------------")
underlineLabel.config(bg="#0f1f3b",fg="white",font=("Courier", 44))
underlineLabel.pack()

#--get url label--#
get_urlLabel = Label(root, text="Enter the URL : ")
get_urlLabel.config(bg="#0f1f3b",fg="white",font=("Courier",15))
get_urlLabel.pack(pady=10)

#--get url entry--#

get_urlEntry = Entry(root, width="50")
get_urlEntry.pack(pady=10)


#--get url button--#

get_messageButton = Button(root,text="Download!",bg="red",fg="white", font=("Arial", 12), command = (lambda: downloadAudio()))
get_messageButton.pack()

#--config label--#

configLabel = Label(root, text="")
configLabel.config(bg="#0f1f3b",fg="white",font=("Courier",15))
configLabel.pack(pady=10)

#--exit button--#
exit_button = Button(root,text="Quit", bg="#0f1f3b", fg="white", font=("Courier", 9), command=(lambda: exit()))
exit_button.pack()

root.mainloop()