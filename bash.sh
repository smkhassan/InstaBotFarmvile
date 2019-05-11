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
        sudo pip install instabot
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


cd ./instabut/examples/
#storing user and password to variable and using this as main loop for other scripts

cat < ./secret.txt | while IFS=: read -r userName password; do \
 echo "$userName"
 echo "$password";

limit=10
counter=1
while [ $counter -le $limit ]
do
##upload pictures
python ./upload_photos.py -u $userName -p $password
##follows users from a file
python ./follow_users_from_file.py -u $userName -p $password ./usernames.txt
##likes last images from hashtags
python ./like_hashtags.py -u $userName -p $password  hkrestaurant,hkrestaurants,hkstartup,hkbusiness,hkcafe
##comments Hashtags
python ./comment/comment_hashtags.py -u $userName -p $password ./comments.txt hkrestaurant,hkrestaurants,hkstartup,hkbusiness,hkcafe
##messages all Followers
python ./message.py -u awesomebarbara22 -p Don735zari@@ -users ./notified_users.txt -message "Hi there, did you see my comment?  🙂 Just wanted to check if you wanted to hear more about the digital growth program we offer. Have a couple of seats left, so let me know if you’re interested (or not) haha."
done

echo DONE

done
