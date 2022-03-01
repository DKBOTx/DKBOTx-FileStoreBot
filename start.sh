if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/vloggerdeven/File-Share-Bot
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /vloggerdeven
fi
cd /vloggerdeven
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
