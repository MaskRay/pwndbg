#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import subprocess

import pwndbg.commands
import pwndbg.which


@pwndbg.commands.Command
@pwndbg.commands.OnlyWithFile
def checksec(file=None):
    '''
    Prints out the binary security settings. Attempts to call the binjitsu
    checksec first, and then falls back to checksec.sh.
    '''
    local_path = file or pwndbg.file.get_file(pwndbg.proc.exe)

    for program in ['checksec', 'checksec.sh']:
        program = pwndbg.which.which(program)

        if program:
            return subprocess.call([program, '--file', local_path])
    else:
        print('Could not find checksec or checksec.sh in $PATH.')
