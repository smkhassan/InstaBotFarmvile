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
        sudo pip install Pillow
        wget https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip
        unzip -o chromedriver_linux64.zip > ./autoaccount/chromedriver

else
        echo "don't do that"
fi



limit=10
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


#storing user and password to variable and using this as main loop for other scripts

cat < ./instabut/examples/secret.txt | while IFS=: read -r userName password; do \
 echo "$userName"
 echo "$password";
limit=10
counter=1
while [ $counter -le $limit ]
do
##upload pictures
python ./instabut/examples/photos/upload_photos.py -u $userName -p $password
##follows users from a file
python ./instabut/examples/follow_users_from_file.py -u $userName -p $password filepath ./instabut/examples/usernames.txt
##likes last images from hashtags
python ./instabut/examples/like_hashtags.py -u $userName -p $password hashtags hkrestaurant,hkrestaurants,hkstartup,hkbusiness,hkcafe
done



done








