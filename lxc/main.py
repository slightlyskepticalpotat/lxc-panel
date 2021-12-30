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
