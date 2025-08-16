!/bin/bash 

clear

echo ========VERSIONS 2024/04/03===========================
echo ========VERSIONS 2025/07/19===========================
echo 
echo 
echo ====================================================
echo ========List Changes Info===========================
read -p "Continue? (Y/N): " confirm && [[ $confirm == [yY] || $confirm == [yY][eE][sS] ]] || exit 1

cat pi4.txt

echo 
echo ====================================================
echo =====Copy all py programs into ports/search2collection from github 
read -p "Continue? (Y/N): " confirm && [[ $confirm == [yY] || $confirm == [yY][eE][sS] ]] || exit 1

rootsource=https://raw.githubusercontent.com/pestami/search2collection/
branch=main/


source01=pi4.txt  
target01=/home/pi/RetroPie/roms/ports/search2collection/pi4.txt
source01=pi3Bp.txt  
target01=/home/pi/RetroPie/roms/ports/search2collection/pi4.txt

source02=colors.py 
target02=/home/pi/RetroPie/roms/ports/search2collection/colors.py 

source03=search2collection.py 
target03=/home/pi/RetroPie/roms/ports/search2collection/search2collection.py 

source04=s2c_search_rich.py
target04=/home/pi/RetroPie/roms/ports/search2collection/s2c_search_rich.py

source05=s2c_db.py
target05=/home/pi/RetroPie/roms/ports/search2collection/s2c_db.py

#===list of files in text file=====
# wget -i update.txt

echo $rootsource$source01 
wget -O $target01 $rootsource$branch$source01 
wget -O $target02 $rootsource$branch$source02 
wget -O $target03 $rootsource$branch$source03
wget -O $target04 $rootsource$branch$source04
wget -O $target05 $rootsource$branch$source05


read -p "Continue? (Y/N): " confirm && [[ $confirm == [yY] || $confirm == [yY][eE][sS] ]] || exit 1
echo ========Script Completed===========================
