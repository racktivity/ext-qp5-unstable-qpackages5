# -*- coding: utf-8 -*-
__author__ = 'amplidata'
__tags__   = 'install',

def main(q, i, params, tags):
    qpackage = params['qpackage']
    qpackage.copyFiles()
    
