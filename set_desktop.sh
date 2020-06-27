python3 FILE_PATH/scrape_comic.py

convert FILE_PATH/latest_comic.png -resize 1920x1080 FILE_PATH/latest_comic.png

gsettings set org.gnome.desktop.background picture-options 'stretched'

gsettings set org.gnome.desktop.background picture-uri file://FILE_PATH/latest_comic.png

gsettings set org.gnome.desktop.background show-desktop-icons false
gsettings set org.gnome.shell.extensions.dash-to-dock intellihide true
bash FILE_PATH/set_mouseover.sh
