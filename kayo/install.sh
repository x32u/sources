sudo apt update

curl -fsSL https://pkg.cloudflareclient.com/pubkey.gpg | sudo gpg --yes --dearmor --output /usr/share/keyrings/cloudflare-warp-archive-keyring.gpg
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/cloudflare-warp-archive-keyring.gpg] https://pkg.cloudflareclient.com/ $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/cloudflare-client.list
sudo apt-get update && sudo apt-get install cloudflare-warp -y # done

warp-cli register
warp-cli set-mode proxy
warp-cli set-proxy-port 7483
warp-cli connect

sudo apt install redis-server postgresql postgresql-contrib -y
sudo systemctl start postgresql.service
sudo -i -u postgres
psql
ALTER USER postgres with encrypted password 'aiemcfZMxcvbhfcs';
CREATE DATABASE swag;
\q
exit

sudo apt install software-properties-common -y
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.10 python3.10-dev python3.10-venv -y

python3.10 -m venv .venv
screen -dmS main
source .venv/bin/activate

sudo apt install libcairo2 libmagickwand-dev
python3.10 -m pip install -r requirements.txt
playwright install
playwright install-deps

python3.10 main.py