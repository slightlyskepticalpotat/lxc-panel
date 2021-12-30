import lxc
import sys
# import flask_hook # for what? only god knows
# import lxc-nat-py # https://github.com/daniel5gh/lxc-nat-py

class CreationError(Exception):    
  pass

def create_instance(name: str, os: list, keyserver: str='keyserver.ubuntu.com'): # internal_ip: list, port: list
  c = lxc.Container(name)
  if c.defined:
    print("Container already exists", file=sys.stderr)
    raise CreationError

  # for x in range(len(internal_ip)):
  #  container.network[x].ipv4 = internal_ip[x]
  #  container.network[x].ipv4_gateway = "?" # I don't know enough about lxc networking to have any idea what to put here

  if not c.create("download", lxc.LXC_CREATE_QUIET, {"dist": os[0],
                                                   "release": os[1],
                                                   "arch": os[2], # amd64 or i386
                                                   "keyserver": keyserver}): 
    print("Failed to create the container rootfs", file=sys.stderr)

  if not c.start():
    print("Failed to start the container", file=sys.stderr)
    raise CreationError

  # f = open('conf', 'r+') # def should wrap this in a try except
  # ...
  # f.write(new_conf)
  # lxc-nat-py.rerun(conf='conf') # may be a good idea to move to front, so additional reboot is not necessary

  return (c, True) # object containing queriable info (possible security risk) and True because why not

def setup_instance(name: str, commands: list): # commands must be double list! if only one command, wrap in this format: [[{command}]]
  c = lxc.Container(name)

  if c.running:
    stop_instance(name=name, force=True)
  start_instance(name=name)
  console_instance(name=name, commands=commands)

  return True

def start_instance(name: str):
  c = lxc.Container(name)
  
  if not c.start():
    print("Failed to start the container", file=sys.stderr)
    raise CreationError
  if not c.get_ips(timeout=30):
    print("Failed to get IPs", file=sys.stderr)
    raise CreationError
    
  return True
  
def stop_instance(name: str, force: bool=False):
  c = lxc.Container(name)
  
  if force is True:
    if not c.stop():
      print("Failed to stop the container", file=sys.stderr)
      raise CreationError
    
  if not c.shutdown(30):
    print("Failed to cleanly shutdown the container, forcing.")
    if not c.stop():
      print("Failed to stop the container", file=sys.stderr)
      raise CreationError
  
  return True

def console_instance(name: str, commands: list): # definitely should rename this sometime
  c = lxc.Container(name)
  
  for x in commands:
      c.attach_wait(lxc.attach_run_command,
                          x)
      
  # TODO: figure out what to return to get SIGOUT/STDERR/TTY
