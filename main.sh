#Install Toolbox v3
if [[ ! -d Toolbox ]];then
  echo 'Downloading Library!!!'
else
  #Check if toolbox exist
  python Toolbox/replit/install_toolbox.py
  #Check for update
  sh Toolbox/replit/update.sh
fi













