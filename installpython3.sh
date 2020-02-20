apt-get -y update
apt-get -y install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget
cd /root
curl -O https://www.python.org/ftp/python/3.6.10/Python-3.6.10.tgz
tar -xvf Python-3.6.10.tgz
cd Python-3.6.10
./configure --enable-optimizations
make -j 8
make altinstall
ln -s /usr/local/bin/python3.6 /usr/bin/python3
pip3.6 install --index-url=https://pypi.python.org/simple/ bs4 lxml requests python-magic
