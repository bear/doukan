# -*- coding: utf-8 -*-
"""
:copyright: (c) 2015-2016 by Mike Taylor
:license: MIT, see LICENSE for more details.
"""
import os
import sys
import click


_cfg_name    = 'doukan.cfg'
_cfg_path    = click.get_app_dir('doukan')
_cfg_default = """{ 'active': False }"""


class Options(object):
  def __init__(self):
    self.verbose    = False
    self.configName = None
    self.configPath = None
    self.configFile = None

cfg_items = click.make_pass_decorator(Options, ensure=True)

@click.group()
@click.option('--verbose',  is_flag=True)
@click.option('--cfg_path', default=_cfg_path, type=click.Path(),
              help='Path where the configuration file can be found. Default value is %s' % _cfg_path)
@click.option('--cfg_name', default=_cfg_name,
              help='Configuration file name. Default value is %s' % _cfg_name)
@cfg_items
def cli(config, verbose, cfg_path, cfg_name):
  config.verbose    = verbose
  config.configPath = cfg_path
  config.configName = cfg_name
  config.configFile = os.path.join(cfg_path, cfg_name)
  
@cli.command()
@click.option('--create', is_flag=True, default=False,
              help='Create an empty configuration file if not found at the given path.')
@cfg_items
def check(config, create):
  """Checks that the configuration is functional."""
  errors = []
  events = []

  if not os.path.exists(config.configPath) and create:
    os.mkdir(config.configPath)
    events.append('The configuration directory %s was created.' % config.configPath)
  if not os.path.exists(config.configFile) and create:
    with open(config.configFile, 'w') as h:
      h.write(_cfg_default)
    events.append('An empty configuration file was created.')

  if not os.path.exists(config.configFile):
    errors.append('The configuration file %s could not be found at %s' % (config.configName, config.configPath))
    if not create:
      errors.append('  Add to the check command the "--create" option to create an empty configuration file.')

  if config.verbose and len(events) > 0:
    click.echo('We performed the following events during this check')
    for s in events:
      click.echo('  %s' % s)

  if len(errors) > 0:
    click.echo('The configuration check failed with the following errors', err=True)
    for s in errors:
      click.echo('  %s' % s, err=True)
    sys.exit(2)
