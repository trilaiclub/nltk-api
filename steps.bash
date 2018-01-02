sudo pip install -U nltk
NLTK_DATA=~/
sudo python -m nltk.downloader maxent_treebank_pos_tagger -d ~/nltk_data
sudo python -m nltk.downloader punkt -d ~/nltk_data
sudo python -m nltk.downloader averaged_perceptron_tagger -d ~/nltk_data
sudo python -m nltk.downloader stopwords -d ~/nltk_data
sudo python -m nltk.downloader wordnet -d ~/nltk_data
sudo python -m nltk.downloader tagsets -d ~/nltk_data

sudo yum install git
git clone https://github.com/trilaiclub/nltk-api.git
curl --silent --location https://rpm.nodesource.com/setup_8.x | sudo bash -
sudo yum -y install nodejs
npm install loopback
sudo npm install -g forever
forever start --verbose --append --uid \"nltk\" --watch --watchDirectory ./server server/server.js --spinSleepTime 1000ms

