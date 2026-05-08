#!/data/data/com.termux/files/usr/bin/bash

clear
echo "==============================="
echo "   LivvMux v2.2 Installer"
echo "==============================="
echo ""

pkg update -y
pkg upgrade -y
pkg install git python -y

pip install --upgrade pip
pip install -r requirements.txt

chmod +x run.sh

echo ""
echo "Install selesai!"
echo "Jalankan dengan: ./run.sh"
