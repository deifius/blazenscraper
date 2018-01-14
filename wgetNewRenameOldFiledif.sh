#!/bin/bash


wget -o urls/newfile https://blaze-n-gems.myshopify.com/collections/rough-montana-sapphires?page=2&sort_by=created-descending
sleep 5
diff urls/newfile oldfile >> difflog
mv urls/newfile oldfile
##python3 mailor.py
