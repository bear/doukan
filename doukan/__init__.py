# -*- coding: utf-8 -*-
"""
:copyright: (c) 2015 by Mike Taylor
:license: MIT, see LICENSE for more details.
"""

__author__       = 'Mike Taylor'
__email__        = 'bear@bear.im'
__copyright__    = 'Copyright (c) 2015 by Mike Taylor'
__license__      = 'MIT'
__version__      = '0.1.0'
__url__          = 'https://github.com/bear/doukan'
__download_url__ = 'https://pypi.python.org/pypi/doukan'
__description__  = 'Palala'


cfgFilenames = ('doukan.fg', '.doukan.cfg')
cfgFilepaths = (os.getcwd(), '~/', '~/.doukan/')

possibleConfigFiles = []

for p in cfgFilepaths:
    for f in cfgFilenames:
        possibleConfigFiles.append(os.path.join(p, f))


def discoverConfig(cfgFilename=None):
    result = {}

    if cfgFilename is None:
        for possibleFile in possibleConfigFiles:
            possibleFile = os.path.expanduser(possibleFile)
            if os.path.exists(possibleFile):
                result = json.load(open(possibleFile, 'r'))
                break
    else:
        possibleFile = os.path.expanduser(cfgFilename)
        if os.path.exists(possibleFile):
            result = json.load(open(possibleFile, 'r'))

    return result

