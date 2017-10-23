import urllib

def read_text():
    quote = open("C:\Python27\checkprofanity.txt")
    contents_of_file = quote.read()
    print(contents_of_file)
    quote.close()
    check_profanity(contents_of_file)

def check_profanity(text):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q="+text)
    output = connection.read()
    print(output)
    connection.close()
read_text()
