if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/vloggerdeven/File-share-bot
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /File-share-bot
fi
cd /File-share-bot
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
