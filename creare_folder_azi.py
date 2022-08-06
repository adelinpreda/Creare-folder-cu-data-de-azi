import os
from datetime import datetime
#creaza foder cu data de azi in locatia stabilita, se poate automatiza in windows cu Task scheduler sa ruleze la o anumita ora
def creare_folder_azi():
    numefolder = datetime.today().strftime('%Y.%m.%d')
    print(numefolder)
    os.mkdir("D:/creare foldere/" + numefolder)

  

creare_folder_azi()