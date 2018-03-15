import sqlite3, os, datetime

class Nibbler:
    def __init__(self, paramfile):
        self.file=paramfile
        if(os.path.exists(self.file)):
            pass
        else:
            self.creator()
    def creator(self):
        createconn = sqlite3.connect(self.file)
        createc = createconn.cursor()
        createc.execute('''CREATE TABLE shelf (BookID INTEGER PRIMARY KEY autoincrement, Title text, min INT, SeriesID INT, SeriesNum INT, PurchaseDate text, ReadDate text)''')
        createc.execute('''CREATE TABLE serieslist (SeriesID INTEGER PRIMARY KEY autoincrement, Name text)''')
        createconn.commit()
        createconn.close()
        print('Created DB')
    def newseries(self, seriesname):
        newseriesconn = sqlite3.connect(self.file)
        newseriesc = newseriesconn.cursor()
        newseriesc.execute('INSERT INTO serieslist (Name) VALUES (?);',(seriesname,))
        newseriesconn.commit()
        newseriesconn.close()
    def newbook(self, info):
        #date = datetime.date(dateyear,datemonth,dateday).isoformat()
        newbookconn = sqlite3.connect(self.file)
        newbookc = newbookconn.cursor()
        newbookc.execute('INSERT INTO shelf (Title, min, SeriesID, SeriesNum, PurchaseDate) VALUES (?,?,?,?,?)',(info))
        newbookconn.commit()
        newbookconn.close()
    def finishbook(self, name,isodate):
        updateconn = sqlite3.connect(self.file)
        updatec = updateconn.cursor()
        updatec.execute('update shelf set ReadDate = ? where Title = ? and Datetime(PurchaseDate) =< Datetime(?)', (isodate,name,isodate))
        updateconn.commit()
        updateconn.close()
   

if __name__ == '__main__':
    file = os.path.abspath('C:/users/bwagn/test.db')
    nibs = Nibbler(file)
    pass
