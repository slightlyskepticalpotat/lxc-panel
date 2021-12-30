def setup_instance(name: str, commands: list): # commands must be double list! if only one command, wrap in this format: [[{command}]]
  c = lxc.Container(name)

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
