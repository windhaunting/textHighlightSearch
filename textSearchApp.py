import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox,QFileDialog,QPlainTextEdit,QTextEdit,QFormLayout, QApplication
from PyQt5.QtGui import QIcon, QTextCursor, QTextCharFormat, QBrush, QColor
from PyQt5.QtCore import pyqtSlot, QRect, QRegExp

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'TextHighlighter-fubao'
        self.left = 10
        self.top = 10
        self.width = 1200
        self.height = 840
        self.fileContentText = None
        self.inputSearchText = None
        self.openFileButton = None
        self.lastStart = 0

        #self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create textbox
        self.fileContentText = QTextEdit(self)
        self.fileContentText.move(20, 20)
        self.fileContentText.resize(780, 740)

        # Create a button in the window

        self.openFileButton = QPushButton('Open File', self)
        self.openFileButton.resize(100, 40)
        self.openFileButton.move(800, 30)


        # Create textbox         #search in two or more keywords in one line, use  comma ',' to separate
        self.inputSearchText = QLineEdit(self)
        self.inputSearchText.move(800, 90)
        self.inputSearchText.resize(200, 30)
        self.inputSearchText.textChanged.connect(self.searchInputTextChanged)

        self.searchButton = QPushButton('Search', self)
        self.searchButton.move(1000, 90)
        self.searchButton.resize(100, 30)

        # connect button to function on_click
       # self.button.clicked.connect(self.on_click)
       # self.show()
    def searchInputTextChanged(self, text):
        print ("contents of text box: " + text)
        #return text


    '''
    @pyqtSlot()
    def on_click(self):
        textboxValue = self.textbox.text()
        QMessageBox.question(self, 'Message - pythonspot.com', "You typed: " + textboxValue, QMessageBox.Ok,
                             QMessageBox.Ok)
        self.textbox.setText("")
    '''

    def on_clickOpenFile(self):
        # The QWidget widget is the base class of all user interface objects in PyQt4.
        w = QWidget()

        # Set window size.
        w.resize(320, 240)

        # Set window title
        w.setWindowTitle("Hello World!")

        # Get filename using QFileDialog
        filename = QFileDialog.getOpenFileName(w, 'Open File', '/')
        print('53filename: ', filename[0])

       # text_edit = QTextEdit()

        # print file contents
        textContent = open(filename[0]).read()
        #text_edit.setGeometry(QRect(0, 0, 390, 190))

        self.fileContentText.setText(textContent)
        #print('62 textContent: ', textContent)
        # Show window
        w.show()


    def readFileDialog(self):
        self.initUI()
        # connect button to function on_click
        self.openFileButton.clicked.connect(self.on_clickOpenFile)
        self.show()

        self.searchButton.clicked.connect(self.findContent)

    '''
    # find and highlight
    def findContent(self):
        searchedStr = self.inputSearchText.text()
        print('100 searchedStr: ', searchedStr)
        text = self.fileContentText.toPlainText()

        regex = QRegExp(searchedStr)

        format = QTextCharFormat()
        format.setBackground(QBrush(QColor("red")))
        pos = 0
        index = regex.indexIn(text, pos)
        cursor = self.fileContentText.textCursor()

        while (index != -1):
            # Select the matched text and apply the desired format
            cursor.setPosition(index)
            cursor.movePosition(QTextCursor.EndOfWord, 1)
            cursor.mergeCharFormat(format)
            #Move to the next match
            pos = index + regex.matchedLength()
            index = regex.indexIn(text, pos)

        print ("114 findContent not find ")
    '''


    # find and highlight
    def findContent(self):
        searchedStr = self.inputSearchText.text()
        print('100 searchedStr: ', searchedStr)
        text = self.fileContentText.toPlainText()

        cursor = self.fileContentText.textCursor()
        format = QTextCharFormat()
        format.setBackground(QBrush(QColor("red")))

        while(self.lastStart >= 0):

            end = self.lastStart + len(searchedStr)
            self.moveCursor(cursor, self.lastStart, end)
            self.lastStart = text.find(searchedStr, self.lastStart + 1)
            cursor.mergeCharFormat(format)

        self.notFound()
        print("114 findContent not find ")


    def moveCursor(self,cursor, start,end):

        # We retrieve the QTextCursor object from the parent's QTextEdit
        #

        # Then we set the position to the beginning of the last match
        cursor.setPosition(start)

        # Next we move the cursor over the match and pass the KeepAnchor parameter
        # which will make the cursor select the the match's text
        cursor.movePosition(QTextCursor.Right,QTextCursor.KeepAnchor,end - start)

        # And finally we set this new cursor as the parent's
        self.fileContentText.setTextCursor(cursor)

    def notFound(self):

        self.lastStart = 0

        # We set the cursor to the end if the search was unsuccessful
        self.fileContentText.moveCursor(QTextCursor.End)

        # Make system beep
        QApplication.beep()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.readFileDialog()

    sys.exit(app.exec_())