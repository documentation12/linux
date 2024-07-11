nano file.html
sude systemctl start apache2
sude systemctl enable apache2
sude systemctl status apache2
mv ~/file.html /var/www/html

====================================================================================================

#!/bin/bash

network_prefix="192.168.100."
start_range=10
end_range=25
output_file="IPs.txt"

> "$output_file"

for i in $(seq $start_range $end_range); do
    ip="${network_prefix}${i}"
    if ping -c 2 -W 1 "$ip" > /dev/null 2>&1; then
        echo "$ip is active"
        echo "$ip" >> "$output_file"
    else
        echo "$ip is not active"
    fi
done

echo "Active IPs have been recorded in $output_file."

====================================================================================================

nano hello.sh
chmod +x hello.sh
./hello.sh

====================================================================================================

#!/bin/bash

echo "Hello, World!"
mkdir hello
cd hello
touch hello.txt
echo "Hello, World!" > hello.txt

====================================================================================================

mkdir safe
cd safe
sudo chmod u=rwx,o= safe
ls -ld safe

====================================================================================================

sude systemctl enable ssh
sude systemctl start ssh
cd nano /etc/ssh/sshd_config
sude systemctl restart ssh

====================================================================================================

Check the status of ufw
sudo ufw status

Enable ufw if inactive
sudo ufw enable

Set default policies
sudo ufw default deny incoming
sudo ufw default allow outgoing

Allow SSH connections on port 2222
sudo ufw allow 2222/tcp

Allow HTTP connections on port 80
sudo ufw allow 80/tcp

Check the firewall rules
sudo ufw status verbose

====================================================================================================

sudo ip addr add 192.168.100.10/24 dev eth0
sudo ip link set eth0 up
sudo ip route add default via 192.168.100.1
ip addr show
ip route

====================================================================================================

sudo adduser user
password reqiusite minlen=8
sudo user -a -G sudo user
sudo groupadd group
sudo usermod -a -G group user
sudo chsh -s /bin/bash user
finger user
touch report.txt
sudo chown user:group report.txt