import lxc_main_functions

def nat_setup_instance(name: str, port: list):
  internal_ip = lxc_main_functions.get_ip_instance(name=name)[0]
  todo: actual stuff
