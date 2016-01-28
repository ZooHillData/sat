#!/usr/bin/env python
#-*- coding:utf-8 -*-

import common

# Define all possible option for config command :  sat config <options>
parser = common.options.Options()
parser.add_option('u', 'unique', 'boolean', 'unique', "TEST d'option.")
parser.add_option('v', 'value', 'string', 'value', "Appelle la commande config avec l'option value.")

def description():
    return _("Test d'une commande supplémentaire.")
    

def run(args, runner):
    (options, args) = parser.parse_args(args)
    if options.unique:
        print('unique')
    elif options.value:
        runner.cfg.VARS.user = 'TEST'
        runner.config('-v ' + options.value)
