import subprocess, os, sys
import pkg_resources

reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
installed_packages = [r.decode().split('==')[0] for r in reqs.split()]
#print(installed_packages[113]) 

def install_toolbox(
  dev_mode = True
):
  reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
  installed_packages = [r.decode().split('==')[0] for r in reqs.split()]

  for package in ['toolbox']:
    try:
        dist = pkg_resources.get_distribution(package)
        print('{} ({}) is installed!'.format(dist.key, dist.version))
    except pkg_resources.DistributionNotFound:
        #print('{} is NOT installed'.format(package))
        print('Installing Toolbox Features!')

        if dev_mode:
          os.system("pip install -e ./Toolbox")
        else:
          os.system("pip install ./Toolbox")



install_toolbox(dev_mode=False)
