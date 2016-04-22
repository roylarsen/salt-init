import sys, getopt, os

def create_formula(name):
  if not os.path.exists(name):
    print "Creating {name}/...".format(name = name)
    os.makedirs(name)
    print "Creating {name}/files/...".format(name = name)
    os.makedirs(name + "/files")
    print "Creating {name}/templates/...".format(name=name)
    os.makedirs(name + "/templates")
    print "Creating {name}/init.sls...".format(name=name)
    with open(name + "/init.sls", "a+") as f:
      f.write('{% from "' + name + '/map.jinja" import ' + name + ' with context %}')
      f.close()
    print "Creating {name}/map.jinja...".format(name=name)
    with open(name + "/map.jinja", "a+") as f:
      map_content = "{% set " + """{NAME} = salt['grains.filter_by']({{
    'default': {{}}
}},
merge=salt['pillar.get']('{NAME}:lookup'))
""".format(NAME = name) + "%}"
      f.write(map_content)
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
