# input#-------------------------------------------------------------------------------
# Name:      search2collection.py
# Purpose:
#
# Author:      MPA
#
# Created:     2024 05 03
#
#-------------------------------------------------------------------------------
import sqlite3
from colors import colors
import os
import re
from xml.dom.minidom import parse
import xml.dom.minidom

class s2c_db:

#-------------------------------------------------------------------------------
   
#============================================================================
#============================================================================
    def ROM_DB_LoadGameListsContents(sPathFileDB,lLIST_XML_GAMESLISTS_Metadata,console):

            # LIST_GAMES_META
            #(PATH,NAME,DES,IMAGE,RATING,RELEASE,DEVELOPER,PUBLISHER,GENERE,PLAYERS,PLAYCOUNT,LASTPLAYED)
            #/home/pi/RetroPie/roms/c64/Ping Pong.tap
            lLIST_SEARCH_DB=[]
            
            #print(lLIST_XML_GAMESLISTS_Metadata[1])
            
            for items in  lLIST_XML_GAMESLISTS_Metadata:
                NAMEROM= items[1]
                CONSOLE= console  # not in gameslist.xml
                SEARCHTEXT= items[1] +': '+ items[2]
                COLLECTIONPATHFILE = items[0].replace('./','/home/pi/RetroPie/roms/'+CONSOLE +'/')
                
                lLIST_SEARCH_DB.append([NAMEROM,CONSOLE,SEARCHTEXT,COLLECTIONPATHFILE])
            
            con = sqlite3.connect(sPathFileDB)
            con.text_factory = str
            cur = con.cursor()
            cur.executemany("INSERT OR IGNORE INTO LIST_SEARCH_DB (NAMEROM,CONSOLE,SEARCHTEXT,COLLECTIONPATHFILE) VALUES (?, ?, ?, ? );", lLIST_SEARCH_DB)

            print('Rows uploaded into SEARCH DataBase =' + str(cur.rowcount))
##            sSQL_01="UPDATE LIST_GAMES_META SET CONSOLE = '"+console+"'; "
##            cur.execute(sSQL_01)

            con.commit()
            con.close()
#============================================================================
#============================================================================

#============================================================================
#============================================================================
    def ExtractMetadatefromGameXML(xmlfile,sPathROMS, **kwargs):
        
        def GetElement(XMLElement,sTagName):
                try:
                    Name = XMLElement.getElementsByTagName(sTagName)[0]
                    sData=Name.childNodes[0].data
            ##        print(sTagName +" = " + sData)
                    return sData
                except:
            ##        print(sTagName + " = Does Not Exist")
                    return ''

    ##     xmlfile = 'G:\\roms\\mame\\gamelist.xml'
    ##    xmlfile = 'G:\\roms\\amstradcpc\\gamelist.xml'

        flagDebug=kwargs.get('flagDebug', None)
        #print ('.......................................................')
        #print ('...  Extract Metadata from Game XML ...')
        #print (xmlfile)
        #print ('...  lGamesListCollection...')
        #print ('.......................................................')

        lGamesListCollection=[]
        lGamesList=[]
        ncountgames=0
        if os.path.exists(sPathROMS):
            lgames = os.listdir(sPathROMS)

        # Open XML document using minidom parser
        DOMTree = xml.dom.minidom.parse(xmlfile)
        gameList = DOMTree.documentElement
        # Gamelist has no attributes typicaly
        #print ('LINE 271')
        if gameList.hasAttribute("system"):
           print ("Root element : %s" % gameList.getAttribute("system"))

        # Get all the movies in the collection
        GAMES = gameList.getElementsByTagName("game")

        for game in GAMES:
            lGamesList=[]
            #(PATH,NAME,DES,IMAGE,RATING,RELEASE,DEVELOPER,PUBLISHER,GENERE,PLAYERS,PLAYCOUNT,LASTPLAYED)
            if flagDebug: print ('...<GAME>' , xmlfile)
            sValue = GetElement(game,'path')
            sGameRom_File= re.split('/', sValue)[-1]   #last value in list]
            lGamesList.append(sValue)
            if flagDebug :print("path:"+sValue)

            sValue = GetElement(game,'name')
            lGamesList.append(sValue)
            if sValue and flagDebug: print("name:"+sValue)

            sValue = GetElement(game,'desc')
            lGamesList.append(sValue)
            if sValue and flagDebug: print("desc:"+sValue[:40])

            sValue = GetElement(game,'image')
            lGamesList.append(sValue)
            if sValue and flagDebug: print("image:"+sValue)

            sValue = GetElement(game,'rating')
            lGamesList.append(sValue)
            if sValue and flagDebug: print("rating:"+sValue)

            sValue = GetElement(game,'releasedate')
            lGamesList.append(sValue)
            if sValue and flagDebug: print("releasedate:"+sValue)

            sValue = GetElement(game,'developer')
            lGamesList.append(sValue)
            if sValue and flagDebug: print("developer:"+sValue)

            sValue = GetElement(game,'publisher')
            lGamesList.append(sValue)
            if sValue and flagDebug: print("publisher:"+sValue)

            sValue = GetElement(game,'genre')
            lGamesList.append(sValue)
            if sValue and flagDebug: print("genre:"+sValue)

            sValue = GetElement(game,'players')
            lGamesList.append(sValue)
            if sValue and flagDebug: print("players:"+sValue)

            sValue = GetElement(game,'playcount')
            lGamesList.append(sValue)
            if sValue and flagDebug: print("playcount:"+sValue)

            sValue = GetElement(game,'lastplayed')
            lGamesList.append(sValue)
            if sValue and flagDebug: print("lastplayed:"+sValue)
            if flagDebug: print ('...</GAME>')
                
            
            if sGameRom_File in lgames:
                lGamesListCollection.append(lGamesList)
                
            ncountgames+=1 
                
                
    ##        print (lGamesList)
    
        return lGamesListCollection, lgames, ncountgames
    
    
        if flagDebug: print ("Number of ROMS Detected in folder=" + lgames.count)
        if flagDebug: print ("Number of ROMS Listed in gamelist=" + lGamesListCollection.count)
        if flagDebug: print ("=============================================\n")
        



#============================================================================
#============================================================================
        
###############################################################################
if __name__ == '__main__':
    
    print ("======================================================")
    print ("TEST CODE s2c_search.py===============================")
    print ("======================================================")
