#!/usr/bin/env bash

echo "Do you want to install dependencies ? [Y,n]"
read input
if [[ $input == "Y" || $input == "y" ]]; then
        ##dependencies
        sudo apt-get -y install python3
        sudo apt-get -y install python-pip
        sudo apt-get -y install xvfb
        sudo apt-get -y install unzip
        sudo apt-get install chromium-browser
        sudo pip innstall selenium
        sudo pip install pyvirtualdisplay
        wget https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip
        unzip -o chromedriver_linux64.zip > ./autoaccount/chromedriver

else
        echo "don't do that"
fi


echo "How many account you want to create?"
read limit
counter=1
while [ $counter -le $limit ]
do
python ./autoaccount/botAccountCreate.py
((counter++))
done

#generating so we can follow
cat ./instabut/examples/usernames.txt | while read LINE; do \
    echo $LINE \

done









