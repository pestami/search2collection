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
from s2c_db import s2c_db

class s2c_r:

#-------------------------------------------------------------------------------
    
#============================================================================
#============================================================================
# ID='0123456789'0-clscr; 1-heading; 2-systems; 3-collections; 4-search keywrd; 5-save search; 6-admin
# Help(ID)     
# black; red; green; yellow; blue; magenta; cyan; white; bright_black; bright_red; bright_green; 
# bright_yellow; bright_blue; bright_magenta; bright_cyan; bright_white
    def Help(ID): 
        
            sHelp=""
            
            if ID=='':
                ID='0123456789'
            #sHelp+=chr(27) + "[2J")
            
            if '0' in ID:
                os.system('cls||clear')
                os.system('cls||clear')
                
            if '1' in ID:
                sHelp+= '[green]'
                sHelp+='=========================================================='
                sHelp+='\n==Program to generate a playlist=======V20250613=========='
                sHelp+='\n=========================================================='
                sHelp+= '[/green]'
           
            if '2' in ID:
                #sHelp+= colors.fg.lightred
                sHelp+='[magenta]'
                sHelp+='\n\n..UPDATE SEARCH DATABASE..............................'
                sHelp+='\ntype ls to list installed game Systems (MAME ,ATARI etc.)'
                sHelp+='\ntype ws to scrape Systems information to Search-DataBase'
                sHelp+='\ntype ds <item> to delete a Systems from the search DataBase'
                sHelp+= '[/magenta]'
           
            if '3' in ID:
                #sHelp+= colors.fg.purple, "...")
                sHelp+= '[cyan]'
                sHelp+='\n\n..MANAGE COLLECTIONS...................................'
                sHelp+='\ntype lc to list collections'
                sHelp+='\ntype dc <item> to delete a collection'
                sHelp+= '[/cyan]'
           
            if '4' in ID:
                #sHelp+= colors.fg.lightblue, "...")
                sHelp+= '[yellow]'
                sHelp+='\n\n..SEARCH for ROMS.....................................'
                sHelp+='\ntype s keyword1+keyword2 to search for game in Name of ROM'
                sHelp+='\ntype sd keyword1+keyword2 to search for games in description'
                sHelp+= '[/yellow]'
            
            if '5' in ID:
                #sHelp+= colors.fg.lightblue, "...")
                sHelp+= '[bright_white]'
                sHelp+='\n\n..SEARCH RESULTS.......................................'
                sHelp+='\ntype l  list last plalists resulting from Search criteria'
                sHelp+='\ntype wr <item> to write playlist to a collection + rename'
                sHelp+='\ntype w  to write playlist to default named collection list'
                sHelp+= '[/bright_white]'
           
            if '6' in ID:
                #sHelp+= colors.fg.green, "...")
                sHelp+= '[green]'
                sHelp+='\n\n.......................................................'
                sHelp+='\ntype h  to help'
                sHelp+='\ntype x  to quit'
                sHelp+='\n\n=========================================================='
                sHelp+= '[/green]'
                
            return sHelp
#-------------------------------------------------------------------------------
#============================================================================
#===========================================================================
    def DisplayGameLists(): # ----------------------------------MIGRATED
               
                pathcollections='/home/pi/.emulationstation/gamelists/'
                sGameLists=''

                dir_list = os.listdir(pathcollections)
                i=0
               
                # prints all files
                # os.system('cls||clear')
                # sGameLists+='..................................\n'
                # sGameLists+='-----GAME Lists FOUND---------------\n'
                # sGameLists+="Directory= \n"
                # sGameLists+= pathcollections +'\n'
                
                for sfiles in dir_list:                   
                    sGameLists+=str(i) + ":" + sfiles +'\n'
                    i=i+1
                    
                return sGameLists, dir_list
#-------------------------------------------------------------------------------
#============================================================================
#===========================================================================
    def DisplayCollections(): # ----------------------------------MIGRATED
               
                pathcollections='/home/pi/.emulationstation/collections/'             
                sCollectionsLists=''
                
                dir_list = os.listdir(pathcollections)
                i=0
               
                # prints all files
                # os.system('cls||clear')
                # print('.........................................................')
                # print('-----COLLECTIONS FOUND------------------')
                # print("Directory= '", pathcollections, "' :")
                
                for sfiles in dir_list:                   
                    sCollectionsLists+=str(i) + ":" + sfiles +'\n'
                    i=i+1
                return sCollectionsLists, dir_list
#===========================================================================
    def DeleteCollection(collections_List,sIndex): # -------------MIGRATED
            
            pathcollections='/home/pi/.emulationstation/collections/' 
            file_path = pathcollections + collections_List[int(sIndex)]
            
            if os.path.exists(file_path):
                    os.remove(file_path)
                    sMessage="\nThe collection has been removed.\n"
                    sMessage+=file_path
            else:
                    sMessage="\nThe system cannot find the file specified. \n"
                    sMessage+=file_path
            return   sMessage               
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
    def Makeplaylist(skeywords,sCMD): # --------------------------MIGRATED
        
        sPathFileDB='/home/pi/RetroPie/roms/ports/search2collection/SearchRetroRoms.db'
    
        con = sqlite3.connect(sPathFileDB)
        con.text_factory = str
        cur = con.cursor()
        
        skeywordsDelimited=skeywords.replace('+','#OR#')
        skeywordsDelimited=skeywordsDelimited.replace(' ','#OR#')
        skeywordsDelimited=skeywordsDelimited.replace('*','#AND#')
        lKeywordsRAW = skeywordsDelimited.split('#')          
        
        lOperators =lKeywordsRAW[1::2]   #a[start:stop:step]    lKeywordsRAW=['sd' ,'space','+','invaders','*','new']                                
        lKeywords= lKeywordsRAW[0::2]     

        

        sSQLlike=''   
        
        i=0                                 
        for item in  lKeywords:
           
            if i==0:
               sSQLlike='like \'%' + item + '%\''  
            else:
                
                sSQLlike=sSQLlike + lOperators[i-1] + ' &COLUMN& like \'%' + item + '%\'' 
            i=i+1
                   
#----------------------------------------------------------                                        
        #NAMEROM like '%invader%' OR NAMEROM like '%asteroid%  
        if sCMD=='sd':   
                sCOLUMN='SEARCHTEXT'
        if sCMD=='s':     
                sCOLUMN='NAMEROM'   
                  
        sSQL='''
                        SELECT
                        COLLECTIONPATHFILE
                        FROM LIST_SEARCH_DB
                        WHERE 
                        &COLUMN& &LIKE&
                        ORDER BY
                        COLLECTIONPATHFILE ASC
                ''' 
         
  
#----------------------------------------------------------  
        sSQL=sSQL.replace('&LIKE&',sSQLlike)
        sSQL=sSQL.replace('&COLUMN&',sCOLUMN)

                                 
        cur.execute(sSQL)
        
        lGamesRomCollectionsList=cur.fetchall()
        
        con.commit()
        con.close()
        
        sGamesRomLists=''
        for games in lGamesRomCollectionsList:                   
            sGamesRomLists+=str(i) + ":" + games[0].replace('/home/pi/RetroPie/roms/','') +'\n'
            i=i+1
        
                
        # sMessage='=====================================================\n'
        sMessage='==SQL================================================\n'
        # sMessage+='=====================================================\n'
        # sMessage+=lKeywords +'\n'
        # sMessage+=lOperators         +'\n'                         
        # sMessage+='-----------------------------------------------------\n' 
        sMessage+=sSQL  +'\n'  
        sMessage+='Found:' + str(len(lGamesRomCollectionsList)) + ' games.' +'\n'
        sMessage+='=====================================================\n'
    
        return sGamesRomLists, sMessage, lGamesRomCollectionsList
#-------------------------------------------------------------------------------
#===========================================================================
#============================================================================
    def Displaylist(result_List): # ------------------------------MIGRATED IN WORK
        
        #print(chr(27) + "[2J")
        # os.system('cls||clear')
        
        sCMD=''
        
        while sCMD != 'x' and sCMD != 'X':
            
           
            print('---------------------------------------------------------')
            print('-----KEWORDS FOUND LIST----------------------------------')
            sFound=str(len(result_List))
            
           
            i=0
            nTotal=0
            for items in result_List:
                i=i+1
                nTotal=nTotal+1
                print(str(nTotal)+' : ' + items[0])
               
                if i==25:
                    i=0
                    print( colors.fg.lightblue, "...")
                    print('\nDisplayed: ' +str(nTotal) +'/'+ sFound +'  Press key to continue, x to exit.........')
                    sCMD = str(input())   
                    if sCMD =='x' or sCMD =='X':
                        break
            
        print('-----KEWORDS FOUND END-------------------')      
        print('---------------------------------------------------------')
    
#-------------------------------------------------------------------------------
#============================================================================   

#============================================================================
#============================================================================
    def WriteToCollectionRename(result,sName):
        
            # print('.........................................................')
            # print('Collection will be saved: custom-A-KEYWORD.cfg')
            # print('Type the keyword KEYWORD you would like to use to write the collection: ')
            # sName = str(input())
            # sName=sName.replace(' ','')

            PathFile='/home/pi/.emulationstation/collections/custom-A-KEYWORD.cfg'
            PathFile=PathFile.replace('KEYWORD',sName)
            
            with open(PathFile, 'w') as writer:  
                
                 writer.write('/home/pi/RetroPie/roms/ports/search2collection.sh\n')
                 nCount=0
                 for items in result:
                   #  print(items)   
                     writer.write(items[0] + '\n')
                     nCount=nCount+1
            writer.close
            sMessage='  '
            sMessage+='.........................................................'          
            sMessage+='Collection has been saved to: \n'
            sMessage+= PathFile+ ' \n'           
            sMessage+='Found:' + str(nCount) + ' games.\n'
            sMessage+='.........................................................\n'
            
            return sMessage
#-------------------------------------------------------------------------------
#============================================================================
#===========================================================================
    def WriteToCollection(result):

            
            PathFile='/home/pi/.emulationstation/collections/custom-A-search-KEYWORD.cfg'
            with open(PathFile, 'w') as writer:  
                
                 writer.write('/home/pi/RetroPie/roms/ports/search2collection.sh\n')
                 nCount=0
                 for items in result:
                   #  print(items)   
                     writer.write(items[0] + '\n')
                     nCount=nCount+1
            writer.close
            sMessage='.........................................................\n'
            sMessage+='Collection has been saved: custom-A-search-KEYWORD.cfg\n'
            sMessage+='Found:' + str(nCount) + ' games.\n'
            sMessage+='.........................................................\n'
            
            return sMessage
#-------------------------------------------------------------------------------
#============================================================================
#===========================================================================
    def DeleteSystem(sPathFileDB,sSystemName):
            print('.........................................................')
            print('Type systems name(NES, SNES etc.), it will be deleted: ')     
            sSystemName = str(input())
            sSystemName=sSystemName.replace(' ','')
            
            con = sqlite3.connect(sPathFileDB)
            con.text_factory = str
            cur = con.cursor()
            sSQL="DELETE FROM LIST_SEARCH_DB WHERE CONSOLE='" + sSystemName + "';"
            print(sSQL)
            cur.execute(sSQL)

            print('Rows Deleted =' + str(cur.rowcount))
##            sSQL_01="UPDATE LIST_GAMES_META SET CONSOLE = '"+console+"'; "
##            cur.execute(sSQL_01)

            con.commit()
            con.close()
        
#============================================================================
#============================================================================   
###############################################################################
if __name__ == '__main__':
    
    print ("======================================================")
    print ("TEST CODE s2c_search.py===============================")
    print ("======================================================")
    
    temp=s2c_r.Help('123456789')
    print (temp)
    
    
    print ("======================================================")