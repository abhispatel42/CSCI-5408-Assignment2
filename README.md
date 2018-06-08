# CSCI-5408-Assignment2

**Let's install first:**
• sudo add-apt-repository -y ppa:webupd8team/java
• sudo apt-get update
• sudo apt-get -y install oracle-java8-installer

**Download & install the public signing key:**
• wget -qO - https://packages.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add

**Http transport should be enabled (important):**
• sudo apt-get install apt-transport-https

**Save the repository definition to /etc/apt/sources.list.d/elasticsearch-6.x.list:**
• echo "deb https://artifacts.elastic.co/packages/6.x/apt stable main" | sudo tee -a
/etc/apt/sources.list.d/elastic-6.x.list

**Run apt-get update and the repository is ready for use. You can install it with:**
• sudo apt-get update && sudo apt-get install elasticsearch
This information was taken from: https://www.elastic.co/guide/en/elasticsearch/reference/current/deb.html

**Install ElasticSearch**<br/>
• sudo apt-get -y install elasticsearch<br/>
**We have to do some configuration.**<br/>
file /etc/elasticsearch/elasticsearch.yml contains
important configuration details that have to be considered. Open it.<br/>
• sudo nano /etc/elasticsearch/elasticsearch.yml<br/>
• Locate and uncomment (remove # at the beggining of the line) node.name and cluster.name and give new names.<br/>
• Locate and uncomment (remove # at the beggining of the line) network.host and
change to 0.0.0.0. <br/>
Save file.<br/>
Restart the service so changes take the effect:<br/>
• sudo service elasticsearch restart<br/>
Run to start elasticsearch on boot up:<br/>
• sudo update-rc.d elasticsearch defaults 95 10<br/>
You might have a problem with starting ElasticSearch. Test if it’s running:<br/>
• sudo service elasticsearch status<br/>
The problem might be with jvm allocated memory. You can adjust this by lowering the
size of initial heap:<br/>
• sudo nano /etc/elasticsearch/jvm.options<br/>
• Change -Xms1g to -Xms512m and save.<br/>
Restart the service:<br/>
• Sudo service elasticsearch restart<br/>

**You can use any REST client you like. Some of the suggestions are curl for Linux distros,<br/>
or gui oriented ones. In the browser try:**<br/>
• http://<your_ec2_ip>:9200/
If everything is configured well, you should get 200 Response from ES.
Reference:<br/>
**A1: Elastic Search and traditional RDBMS. (n.d.). Retrieved from**<br/>
https://web.cs.dal.ca/~kosmajac/CSCI5408_tutorials/a1.html

## Install python3 and run files
pip3 install python3 <br/>
sudo apt-get install python3-pip<br/>
python3 A1Question1.py<br/>
python3 A1Question2.py<br/>
python3 q3.py

