import flask_hook # for what? only god knows
import lxc-nat-py # https://github.com/daniel5gh/lxc-nat-py

class CreationError(Exception):    
  pass

def create_instance(name: str, port: list, internal_ip: list, os: list):
  c = lxc.Container(name)
  if c.defined:
    print("Container already exists", file=sys.stderr)
    raise CreationError

  for x in range(len(internal_ip)):
    container.network[x].ipv4 = internal_ip[x]
    container.network[x].ipv4_gateway = "?" # I don't know enough about lxc networking to have any idea what to put here

  if not c.create("download", lxc.LXC_CREATE_QUIET, {"dist": os[0],
                                                   "release": os[1],
                                                   "arch": "i386"}): # don't know what the x64 equiv is here either
    print("Failed to create the container rootfs", file=sys.stderr)

  if not c.start():
    print("Failed to start the container", file=sys.stderr)
    raise CreationError

  f = open('conf', 'r+') # def should wrap this in a try except
  ...
  f.write(new_conf)
  lxc-nat-py.rerun(conf='conf') # may be a good idea to move to front, so additional reboot is not necessary

  return (c, True) # object containing queriable info (possible security risk) and True because why not

def setup_instance(name: str, commands: list): # commands must be double list! if only one command, wrap in this format: [[{command}]]
  c = lxc.Container(name) # TODO: use smaller functions like start_function instead of implementing all of this seperately

  if c.running:
    if not c.stop():
      print("Failed to kill the container", file=sys.stderr)
      raise CreationError # wrong error but who cares
  if not c.start():
    print("Failed to start the container", file=sys.stderr)
    raise CreationError
  if not c.get_ips(timeout=30):
    print("Failed to get IPs", file=sys.stderr)
    raise CreationError

  for x in commands:
      c.attach_wait(lxc.attach_run_command,
                          x)

  return True

def start_instance(name: str):
  c = lxc.Container(name)
  
  if not c.start():
    print("Failed to start the container", file=sys.stderr)
    raise CreationError
  if not c.get_ips(timeout=30):
    print("Failed to get IPs", file=sys.stderr)
    raise CreationError
    
def stop_instance(name: str):
  c = lxc.Container(name)
  
  if not c.shutdown(30):
    print("Failed to cleanly shutdown the container, forcing.")
    if not c.stop():
      print("Failed to stop the container", file=sys.stderr)
      raise CreationError
    
def console_instance(name: str, commands: list): # definitely should rename this sometime
  c = lxc.Container(name)
  
  for x in commands:
      c.attach_wait(lxc.attach_run_command,
                          x)
