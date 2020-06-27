# xkcd_scraper
Small project to scrape the latest xkcd comic from the website and set as desktop background, as well as display title, number and mouseover text in terminal.

## How it works

Run set_desktop.sh from the terminal, and scrape_comic.py saves the most recent xkcd comic as a png, and saves the mouseover text in a txt file both in the same folder.
set_desktop.sh resizes the png to fill the desktop, and sets it to be the desktop background. It then runs set_mouseover.sh which displays the mouseover text in 
the terminal.

## How to use

Update instances of FILE_PATH in scripts with the path to the directory you have cloned the repository into. Then simply run set_desktop.sh at any time from the terminal
(make sure you are in the right directory).
I alias the command 'FILE_PATH/set_desktop.sh' to 'xkcd' so I don't have to worry about being in the right directory.

## Requirements

Tested on Ubuntu 18.04. Requires Python3, Beautiful Soup 4, Selenium and Pandas.
