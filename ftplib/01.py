from ftplib import FTP

# ftp = FTP('domainname.com')
ftp = FTP('ftp.nluug.nl/os/Linux/distr/manjaro/')
# ftp.login(user='username',passwd='password')

ftp.cwd('/testing/')

def grabFile():
    filename = '.config'
    localfile = open(filename, 'wb')
    ftp.retrbinary('RETR' + filename, localfile.write, 1024)
    ftp.quit()
    localfile.close()

# def placeFile():
#     filename = 'fileName.txt'
#     ftp.storbinary('STOR' + filename, open(filename, 'rb'))
#     ftp.quit()
