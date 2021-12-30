import lxc_main_functions
import sys

print(lxc_main_functions.create_instance(name=sys.argv[1], os=['ubuntu','focal','amd64']))
print(lxc_main_functions.setup_instance(name=sys.argv[1], commands=[['apt', 'install', '-y', 'openssh-server'], ['adduser', 'newuser'], ['usermod', '-aG', 'sudo', 'newuser']])) 

# ['echo', '-e', f'rootpass\nrootpass', '|', 'passwd', 'newuser'] for non-interactive use
