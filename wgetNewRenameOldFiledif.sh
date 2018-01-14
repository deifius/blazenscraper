#!/bin/bash


wget -T 4 -O urls/newfile https://blaze-n-gems.myshopify.com/collections/rough-montana-sapphires?page=2&sort_by=created-descending
sleep 5
diff -s urls/newfile oldfile > difflog
python3 mailor.py
