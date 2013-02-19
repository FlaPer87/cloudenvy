import logging
import os

ENVIFILE = """
project_config:
  name: %(name)s
  image: %(image)s

  # Remote VM User
  #remote_user: ubuntu

  # Nova Flavor to use
  #flavor_name: m1.small

  # Enable / Disable Auto Provision
  #auto_provision: False

  # Provision Scripts to execute
  #provision_scripts:
    #- provision_script.sh
"""


class EnvyInit(object):

    def __init__(self, argparser):
        self._build_subparser(argparser)

    def _build_subparser(self, subparsers):
        help_str = 'Create and optionally provision an ENVy.'
        subparser = subparsers.add_parser('init', help=help_str,
                                          description=help_str)
        subparser.set_defaults(func=self.run)

        subparser.add_argument('-n', '--name', default='envy',
                               help='Specify custom name for an ENVy.')
        subparser.add_argument('-i', '--image', required=True,
                               help='Image name')
        return subparser

    def run(self, config, args):
        if os.path.isfile("Envyfile") or os.path.isfile("Envyfile.yml"):
            raise SystemExit("An Envifile already exists. "
                             "Please, remove it and run init again.")
        with open("Envyfile.yml", "w") as envy:
            envy.write(ENVIFILE % {"name": args.name, "image": args.image})
        logging.info('New Envyfile created')
