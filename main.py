import math
import os
import subprocess
import sys
import urllib.request
import pytube
from pytube import YouTube
import pytube.exceptions
from PIL import Image
from PySide2 import QtCore, QtGui
from PySide2.QtGui import (QColor)
from PySide2.QtWidgets import *
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3, APIC, error
from mutagen.mp3 import MP3

# loading screen ui
from converter_outside import Ui_LoadingWindow
# main app ui
from converter_ui import Ui_Jazzie

# import pytube
# from pytube import YouTube

# stores a list of words that need to be taken out of artist name so user does not have to change it
blacklistAuthor = ["Topic", "topic"]
blacklistTitle = ["(Official Audio)",
                  "(OFFICIAL AUDIO)"
                  "(Official Music Video)",
                  "[Official Audio]",
                  "[Official Music Video]",
                  "[Audio Only]",
                  "[Audio]"]

blacklistChar = ["#", "%", "&", "{", "}", "\'", "\\", "<", ">", "*", "?", "/", "$", "!", "'", "\"", ":", "@", "+", "`",
                 "|", "=", "~", "^", ";", "[", "]", "(", ")", ",", "."]


# globals
cnt = 0
savePath = os.path.expanduser('~/Downloads/')
authorName = ""
titleName = ""
fullName = ""
thumbnailPath = ""
newFile = ""
oldFile = ""
id3 = None
length = ''
tempNewFile = ''


# loading screen
class LoadingScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.main = MainWindow()
        self.ui = Ui_LoadingWindow()
        self.ui.setupUi(self)

        # remove title bar for clean ui
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Drop shadow effect
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        # start qtimer and connect event to ui progress bar
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)

        # timer in ms
        self.timer.start(30)

        # initial subtitle
        self.ui.subtitleLabel.setText("Converting made <strong>easy</strong>")

        # varying subtitle change 1500 to a different time period
        QtCore.QTimer.singleShot(1500, lambda: self.ui.subtitleLabel.setText("Loading backend"))
        QtCore.QTimer.singleShot(2000, lambda: self.ui.subtitleLabel.setText("Loading backend."))
        QtCore.QTimer.singleShot(2500, lambda: self.ui.subtitleLabel.setText("Loading backend.."))
        QtCore.QTimer.singleShot(3000, lambda: self.ui.subtitleLabel.setText("Loading backend..."))

        self.show()
        # END

    def progress(self):
        global cnt

        # Set value to progress bar
        self.ui.progressBar.setValue(cnt)

        # close load screen and open actual app
        if cnt > 100:

            # stop cnt
            self.timer.stop()

            # show main application
            self.main.show()
            self.close()
        cnt += 1


# main app
def cropTN(imgPath):
    img = Image.open(imgPath)

    # 720x720 square for the thumbnail

    left = 280
    top = 0
    right = 1000
    bottom = 720
    cropped = img.crop((left, top, right, bottom))
    # cropped.show()

    # try to remove prior to saving
    try:
        os.remove(imgPath)
    except FileNotFoundError:
        pass

    cropped.save(imgPath)


class MainWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.msg = QMessageBox()  # error message box
        self.complete = QMessageBox()  # on complete conversion message box
        self.msg.setWindowIcon(QtGui.QIcon('j.png'))
        self.complete.setWindowIcon(QtGui.QIcon('j.png'))
        self.ui = Ui_Jazzie()
        self.ui.setupUi(self)
        self.setWindowTitle('Jazzie YT to MP3 Converter')
        self.setWindowIcon(QtGui.QIcon('j.png'))

        # gui events
        self.ui.urlEntry.textChanged.connect(self.urlChanged)
        self.ui.convertButton.clicked.connect(self.buttonClicked)

    def urlChanged(self):
        url = self.ui.urlEntry.text()
        split = url.split("=")
        id = split[1]
        try:
            global titleName, authorName, fullName, thumbnailPath, tempNewFile, oldFile, newFile, length
            yt = YouTube(url)
            length = yt.length
            maxMinutes = math.floor(length / 60)
            maxSeconds = (length / 60 - math.floor(length / 60)) * 60
            titleName = yt.title
            authorName = yt.author
            authorName = cleanup_author(authorName)
            titleName = cleanup_title(titleName, authorName)
            thumbnailURL = yt.thumbnail_url
            fullName = authorName + '-' + titleName  # name of file before prefix
            thumbnailPath = savePath + fullName + '.jpeg'
            urllib.request.urlretrieve("https://img.youtube.com/vi/" + id + "/maxresdefault.jpg", thumbnailPath)  # saves thumbnail
            cropTN(thumbnailPath)
            audio = yt.streams.get_audio_only()
            audio.download(savePath, fullName + "1.mp3")  # saves mp4 file

            # new save paths
            oldFile = savePath + fullName + '1.mp3'
            newFile = savePath + fullName + '.mp3'

            # autofill text fields
            self.ui.titleEntry.setText(cleanup_title_og(titleName))
            self.ui.authorEntry.setText(cleanup_author_og(authorName))
            self.ui.albumEntry.setText('Provided by Jazzie MP3')

            # calculate formatting of string for input to ffmpeg
            mins = stringMin(maxMinutes)
            secs = stringSec(maxSeconds)

            # autofill start and stop entries
            self.ui.startEntry.setText('00:00:00.00')
            self.ui.stopEntry.setText(mins + secs)

            # allow user to change id3 parameters
            self.ui.authorEntry.setEnabled(True)
            self.ui.titleEntry.setEnabled(True)
            self.ui.albumEntry.setEnabled(True)
            self.ui.comboBox.setEnabled(True)
            self.ui.stopEntry.setEnabled(True)
            self.ui.startEntry.setEnabled(True)

            # set focus to start
            self.ui.startEntry.setFocus()
        except (KeyError, pytube.exceptions.RegexMatchError):
            pass

    def buttonClicked(self):

        if self.ui.comboBox.currentText() == "--Select--":
            self.msg.setIcon(QMessageBox.Critical)
            self.msg.setText('Please select a genre')
            self.msg.setWindowTitle('Error Occurred')
            self.msg.exec_()
            return

        # variables for math arithmetic to compute difference in seconds from start to stop
        try:
            startMin = int(self.ui.startEntry.text()[3:5])
            startSec = int(self.ui.startEntry.text()[6:8])
            stopMin = int(self.ui.stopEntry.text()[3:5])
            stopSec = int(self.ui.stopEntry.text()[6:8])
        except ValueError:
            self.msg.setIcon(QMessageBox.Critical)
            self.msg.setText('Please input correctly formatted start and end times')
            self.msg.setWindowTitle('Error Occurred')
            self.msg.exec_()
            return
        
        #print("before convert")
        # convert
        subprocess.run('ffmpeg -hide_banner -loglevel error -y -i ' + oldFile + ' ' + newFile, shell=True)
        #print("in the middle of conversion")
        # trim mp3 file
        # subprocess.run('ffmpeg -hide_banner -loglevel error -y -i ' + oldFile +
        #                 ' -ss ' + self.ui.startEntry.text() +
        #                 ' -t ' + str((((stopMin - startMin) * 60) + stopSec - startSec)) +
        #                 ' -acodec copy ' + newFile)

        #print("after convert")
        # remove old file and thumbnail after creation
        try:
            os.remove(oldFile)
        except FileNotFoundError:
            pass

        # grab mp3 file
        mp3 = MP3(newFile, ID3=ID3)
        try:
            mp3.add_tags()
        except error:
            print("tags error")
            pass

        # embed thumbnail into mp3 file
        try:
            mp3.tags.add(APIC(mime='image/jpeg', type=3, desc=u'Cover (front)', data=open(thumbnailPath, 'rb').read()))
            mp3.save()
        except error:
            print("embed thumbnail failed")
            pass

        # change id3 tags
        global id3
        id3 = EasyID3(newFile)
        id3['genre'] = str(self.ui.comboBox.currentText())
        id3['album'] = str(self.ui.albumEntry.text())
        id3['artist'] = str(self.ui.authorEntry.text())
        id3['title'] = str(self.ui.titleEntry.text())
        id3.save()

        # remove thumbnail and mp4 file from downloads
        try:
            os.remove(thumbnailPath)
            os.remove(oldFile)
        except FileNotFoundError:
            pass

        # clear selections and allow for new entry
        self.ui.comboBox.setCurrentIndex(0)
        self.ui.authorEntry.clear()
        self.ui.titleEntry.clear()
        self.ui.albumEntry.clear()
        self.ui.urlEntry.clear()
        self.ui.startEntry.clear()
        self.ui.stopEntry.clear()
        self.ui.urlEntry.setFocus()
        # display message box
        self.complete.setIcon(QMessageBox.Information)
        self.complete.setText('Enter in a new song!')
        self.complete.setWindowTitle("Conversion Completed!")
        self.complete.exec_()


def cleanup_title_og(title_name):
    name = title_name

    # replace underscores for spaces
    for char in name:
        if char == '_':
            name = name.replace(char, ' ')
    return name


def cleanup_author_og(author_name):
    name = author_name

    # replace underscores for spaces
    for char in name:
        if char == '_':
            name = name.replace(char, ' ')
    return name


def cleanup_title(title_name, author_name):
    temp = author_name
    for char in temp:
        if char == '_':
            temp = temp.replace(char, ' ')
    name = title_name

    # remove author name if it is in title
    if temp in name:
        name = name.replace(temp, '')

    # remove unwanted words if they are in title
    for word in blacklistTitle:
        if word in name:
            name = name.replace(word, '')

    # remove unwanted hyphens
    for char in name:
        if char == '-':
            name = name.replace(char, '')
    name = name.lstrip(' ')
    name = name.rstrip(' ')

    # remove illegal directory characters
    for char in name:
        if char in blacklistChar:
            name = name.replace(char, '')

    # replace spaces in title with underscores
    for char in name:
        if char == ' ':
            name = name.replace(char, '_')

    return name


def cleanup_author(author_name):
    name = author_name

    # remove words like 'topic' etc from author
    for word in blacklistAuthor:
        if word in name:
            name = name.replace(word, '')

    # get rid of spaces after name
    for char in name[::-1]:
        if char == " ":
            name = name.replace(char, '')
        else:
            break

    # put an underscore for each space in the name
    for char in name:
        if char == " ":
            name = name.replace(char, '_')

    # remove illegal characters
    for char in name:
        if char in blacklistChar:
            name = name.replace(char, '')

    return name


def stringMin(maxMinutes):
    stmin = ''
    if maxMinutes < 10:
        stmin = '00:0' + str(maxMinutes) + ':'
    else:
        stmin = '00:' + str(maxMinutes) + ':'

    return stmin


def stringSec(maxSeconds):
    stsec = ''
    if maxSeconds < 10:
        stsec = '0' + str(int(maxSeconds))
    else:
        stsec = str('%.2f' % maxSeconds)

    return stsec


if __name__ == "__main__":
    app = QApplication()
    window = LoadingScreen()
    sys.exit(app.exec_())
