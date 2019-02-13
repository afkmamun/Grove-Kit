#!/bin/bash              
echo "                        888        d8b888"    
echo "                        888        Y8P888"    
echo "                        888           888"    
echo "88888b. .d8888b 88888b. 888 .d88b. 888888888" 
echo "888  88b88K     888  88b888d88  88b888888"   
echo "888  888 Y8888b.888  888888888  888888888"    
echo "888 d88P     X88888 d88P888Y88..88P888Y88b."  
echo "88888P   88888P'88888P  888  Y88P  888  Y888" 
echo "888             888"                          
echo "888             888"                         
echo "888             888"                          
while read -r line; do
ip="$line"
chmod +x pret.py
./pret.py $ip pjl -q -i command.txt
done < "printeri.txt"
