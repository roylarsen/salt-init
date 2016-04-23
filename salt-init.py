import sys, getopt, os

def create_formula(name):
  if not os.path.exists(name):
    #Yes, this is dumb. I'm also a bad programmer, so, #dealwithit.
    print "Creating {name}-formula/...".format(name=name)
    os.makedirs("{name}-formula".format(name=name))
    print "Creating {name}-formula/{name}/...".format(name=name)
    os.makedirs("{name}-formula/{name}".format(name=name))
    print "Creating {name}-formula/{name}/files/...".format(name=name)
    os.makedirs("{name}-formula/{name}/files".format(name=name))
    print "Creating {name}-formula/{name}/templates/...".format(name=name)
    os.makedirs("{name}-formula/{name}/templates".format(name=name))
    print "Creating {name}-formula/{name}/init.sls...".format(name=name)
    with open("{name}-formula/{name}/init.sls".format(name=name), "a+") as f:
      f.write('{{% from "{name}/map.jinja" import {name} with context %}}'.format(name=name))
      f.close()
    print "Creating {name}-formula/{name}/map.jinja...".format(name=name)
    with open("{name}-formula/{name}/map.jinja".format(name=name), "a+") as f:
      map_content = "{% set " + """{NAME} = salt['grains.filter_by']({{
    'default': {{}}
}},
merge=salt['pillar.get']('{NAME}:lookup'))
""".format(NAME = name) + "%}"
      f.write(map_content)
      f.close()
      print "Creating {name}-formula/pillar.example...".format(name=name)
      with open("{name}-formula/pillar.example".format(name=name), "a+") as f:
        f.write("""{name}:
    lookup:""".format(name=name))
        f.close()

def main(argv):
  try:
    opts, args = getopt.getopt(argv, "hf:")
  except getopt.GetoptError:
    print 'salt-init.py -f <Formula Name>'
    sys.exit(2)

  for opt, arg in opts:
    if opt == '-h':
      print 'salt-init.py -f <Formula Name>'
      sys.exit()
    elif opt in ("-f"):
      create_formula(arg)

if __name__ == "__main__":
  main(sys.argv[1:])
