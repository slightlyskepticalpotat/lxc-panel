import lxc_functions
import sys

print(lxc_functions.create_instance(name=sys.argv[1], os=['ubuntu','focal','amd64']))
print(lxc_functions.setup_instance(name=sys.argv[1], commands=[['apt', 'install', '-y', 'openssh-server'], ['adduser', 'root'], ['usermod', '-aG', 'sudo', 'root'], ['echo', '-e', f'rootpass\nrootpass', '|', 'passwd', 'root']])) # VERY INSECURE, should change
                                                                                                            
