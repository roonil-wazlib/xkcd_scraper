python3 /home/user1/Desktop/xkcd_scrape/scrape_comic.py

convert /home/user1/Desktop/xkcd_scrape/latest_comic.png -resize 1920x1080 /home/user1/Desktop/xkcd_scrape/latest_comic.png

gsettings set org.gnome.desktop.background picture-options 'stretched'

gsettings set org.gnome.desktop.background picture-uri file:///home/user1/Desktop/xkcd_scrape/latest_comic.png

gsettings set org.gnome.desktop.background show-desktop-icons false
gsettings set org.gnome.shell.extensions.dash-to-dock intellihide true
bash /home/user1/Desktop/xkcd_scrape/set_mouseover.sh
