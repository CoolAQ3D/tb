#Install Toolbox v3
if [[ ! -d Toolbox ]];then
  echo 'Downloading Library!!!'
  git clone https://github.com/CoolAQ3D/tb Toolbox
else
  #Check if toolbox exist
  python Toolbox/Toolbox/replit/install_toolbox.py
  #Check for update
  sh Toolbox/Toolbox/replit/update.sh
fi


#python main.py

