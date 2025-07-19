

# search2collections  


[Screenshots Catalog](SCREENSHOTS.md)


## Prerequisites

**The following directories should exist:**

- /home/pi/Documents/Search2CollectionsRetropie/roms/ports
- /home/pi/.emulationstation/collections
- /home/pi/.emulationstation/gamelists

**Clone this repository so that the resultant directory exists:**

- /home/pi/Documents/Search2CollectionsRetropie/roms/ports/search2collection

**Each gameslist folders should also exist:**

<details>
<summary>Example of Games Lists with gamelist.xml</summary>

- /home/pi/.emulationstation/gameslists/amiga/gamelist.xml
- /home/pi/.emulationstation/gameslists/amstradcpc/gamelist.xml
- /home/pi/.emulationstation/gameslists/arcade/gamelist.xml
- /home/pi/.emulationstation/gameslists/atari2600/gamelist.xml
- /home/pi/.emulationstation/gameslists/atari5200/gamelist.xml
- /home/pi/.emulationstation/gameslists/atari7800/gamelist.xml
- /home/pi/.emulationstation/gameslists/c64/gamelist.xml
- /home/pi/.emulationstation/gameslists/coleco/gamelist.xml
- /home/pi/.emulationstation/gameslists/fba/gamelist.xml
- /home/pi/.emulationstation/gameslists/gamegear/gamelist.xml
- /home/pi/.emulationstation/gameslists/gba/gamelist.xml
- /home/pi/.emulationstation/gameslists/gbc/gamelist.xml
- /home/pi/.emulationstation/gameslists/intellivision/gamelist.xml
- /home/pi/.emulationstation/gameslists/mame/gamelist.xml
- /home/pi/.emulationstation/gameslists/mame-libretro/gamelist.xml
- /home/pi/.emulationstation/gameslists/mame-mame4all/gamelist.xml
- /home/pi/.emulationstation/gameslists/mastersystem/gamelist.xml
- /home/pi/.emulationstation/gameslists/megadrive/gamelist.xml
- /home/pi/.emulationstation/gameslists/msx/gamelist.xml
- /home/pi/.emulationstation/gameslists/n64/gamelist.xml
- /home/pi/.emulationstation/gameslists/nds/gamelist.xml
- /home/pi/.emulationstation/gameslists/neogeo/gamelist.xml
- /home/pi/.emulationstation/gameslists/nes/gamelist.xml
- /home/pi/.emulationstation/gameslists/pcengine/gamelist.xml
- /home/pi/.emulationstation/gameslists/ports/gamelist.xml
- /home/pi/.emulationstation/gameslists/ps2/gamelist.xml
- /home/pi/.emulationstation/gameslists/psp/gamelist.xml
- /home/pi/.emulationstation/gameslists/psx/gamelist.xml
- /home/pi/.emulationstation/gameslists/retropie/gamelist.xml
- /home/pi/.emulationstation/gameslists/sega32x/gamelist.xml
- /home/pi/.emulationstation/gameslists/sg-1000/gamelist.xml
- /home/pi/.emulationstation/gameslists/snes/gamelist.xml
- /home/pi/.emulationstation/gameslists/zxspectrum/gamelist.xml


</details>

The program also runs on LINUX without RetroPie installed.
Prerequisite is the required folders and several gamelist.xml files.


## Description of the Program  search2collection.py

### On Startup of Retropie
Emulationstation on startup detects the program:
*search2collection.sh* <BR>
in the folder: <BR>
*/home/pi/Documents/Search2CollectionsRetropie/roms/ports* <BR>
and then creates the corrsponding menue item: **SEARCH2COLLECTIONS**.<BR>
The menue when selected  item will start the PYTHON allication: 
*search2collection.py*


### Database of the gameslists
One of the programs functions is to scrape all the gamelist.xml files <BR>
and create a database available to query and generate a corresponding named Collection.
A collection is similar to a favorites list. <BR>

### Technical

The fields PATH,NAME,DES  are extracted from the gamelist.xml  file.

- PATH - Path to the game
- NAME - Name of the game
- DES - Description of the game

These are then packed into the fields:

- NAMEROM - name of the rom, this is required to build the collection.
- CONSOLE - the type of console ATARI, NES etc.
- SEARCHTEXT - This contains the name of game and the description text 
 and is used tomatch search criteria.
- COLLECTIONPATHFILE - name of the rom, this is required to build the collection.

### What the program does in brief

1. The program prompts for a search criteria.<BR>
Example: *Spaceinvaders*

2. Then searches its own database and creates a list of suggestion.

3. The programthem prompt for a appropriate name to be used for the collection.<BR>
Example: *Hits 80s Original*

4. The collection is then created.

**Example Contents of a collection file:** 
<details>
<summary>custom-Hits 80s Original.cfg</summary>
/home/pi/RetroPie/roms/megadrive/Space Invaders 90 (J) [x].zip
/home/pi/RetroPie/roms/sg-1000/Space Invaders (SG-1000).zip
/home/pi/RetroPie/roms/nes/Spaceinvaders.zip
/home/pi/RetroPie/roms/atari2600/Q-bert.bin
/home/pi/RetroPie/roms/atari2600/ElevatorAction.bin
</details>

5. The program allso has other supportive functions.


