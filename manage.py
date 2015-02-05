#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask.ext.failsafe import failsafe
from flask.ext.script import Manager, Server


@failsafe
def create_app():
    from diilikone import Application
    return Application()


manager = Manager(create_app)
manager.add_command('runserver', Server(host='localhost'))

if __name__ == '__main__':
    manager.run()
