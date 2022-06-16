#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
import re
from cgi import escape  # urllib.quote
blocks = {}


def load_template(template=None, block=False, variable=False, fix=False, form=False, overwrite=False):
    if template:
        blocks[''] = template
        if overwrite:
            fix = True
        if fix:
            parse_fix()
        if block:
            parse_block()
        if variable:
            parse_variable(default=overwrite)
        if form:
            parse_form()
    return get_block('')


def get_block(name):
    if name in blocks:
        return blocks[name]
    return ''


def set_block(name, value=None):
    if value:
        blocks[name] = value
    else:
        del blocks[name]


def parse_fix(template=None):
    if template == None:
        template = get_block('')
    pattern = '<!--\s*START\s*([\w\d_]+)\s-->((?:.|\s)*?)<!--\s*END\s*(\\1)\s-->'
    while True:
        tmp = re.sub(pattern, '<!-- \\1 \\2 \\1 -->', template)
        if tmp == template:
            break
        template = tmp
    pattern = '(<[^>]+)(value\s*=\s*(?:\w*|\'[^\']*\'|"[^"]*"))([^>]+)(name\s*=\s*(?:\w*|\'[^\']*\'|"[^"]*"))([^>]*>)'
    template = re.sub(pattern, '\\1\\4\\3\\2\\5', template)
    blocks[''] = template
    return template


def parse_block(template=None):
    if template == None:
        template = get_block('')

    def block(mm):
        pattern = '<!--\s*([\w\d_]+)\s*((?:.|\s)*?)(\s+\\1)?\s*-->'
        m = re.match(pattern, mm.group(0))
        if m:
            blocks[m.group(1)] = m.group(2)
            if m.group(3):
                return '{%s}' % m.group(1)
        return ''
    pattern = '<!\s*(?:--(?:[^\-]|[\r\n]|-[^\-])*--\s*)>'
    p = re.compile(pattern)

    while True:
        new = p.sub(block, template)
        if template == new:
            break
        template = new
    blocks[''] = template
    return template


def parse_form(template=None, default=False):
    if template == None:
        template = get_block('')

    def form(m):
        if m.group(1):
            name, variable = m.group(1).split('=')
            variable = variable.strip()
        else:
            variable = 'form'
        blocks[variable] = m.group(0)
        return '{%s}' % variable

    pattern = '<form\s*(name\s*=\s*(?:\w*|\'[^\']*\'|"[^"]*"))?[^>]*>((?:.|\s)*?)</form>'
    template = re.sub(pattern, form, template)
    blocks[''] = template
    return template


def parse_variable(template=None, default=False):
    if template == None:
        template = get_block('')

    def attrs(m):
        if m.group(2):
            if default:
                s = m.group(0)
                name, variable = m.group(1).split('=')
                variable = "{%s}" % variable.strip()
                if s.startswith(('textarea', 'select', 'iframe', 'div'), 1):
                    i = m.end(0)-m.start(0)
                else:
                    variable = 'value=\'%s\'' % variable
                return s[:m.start(2)-m.start(0)]+variable+s[m.end(2)-m.start(0):]
            else:
                return m.group(0)
        else:
            s = m.group(0)
            name, variable = m.group(1).split('=')
            variable = "{%s}" % variable.strip()
            if s.startswith(('textarea', 'select', 'iframe', 'div'), 1):
                i = m.end(0)-m.start(0)
            else:
                variable = ' value=\'%s\'' % variable
                i = m.end(1)-m.start(0)
            return s[:i]+variable+s[i:]

    pattern = '<[^>]+(name\s*=\s*(?:[^ >]*|\'[^\']*\'|"[^"]*"))(?:[^>]+(value\s*=\s*(?:[^ >]*|\'[^\']*\'|"[^"]*")))?[^>]*>'
    template = re.sub(pattern, attrs, template)
    blocks[''] = template
    return template


def assign_block(name, vars, debug=False):
    return assign(get_block(name), vars, debug)


def assign(template, vars, debug=False):
    def dodos(template, vars):
        offset = 0
        pattern = '\{([^\s\{\}]+)\}'
        p = re.compile(pattern)
        m = p.search(template)
        while m:
            if m.group(1) in vars:
                s = vars[m.group(1)]
                if not m.group(1) in blocks:
                    s = escape(s)
                template = template[:m.start(0)]+s+template[m.end(0):]
                offset = m.start(0)+len(s)
            elif m.group(1) in blocks:
                s = dodos(blocks[m.group(1)], vars)
                template = template[:m.start(0)]+s+template[m.end(0):]
                offset = m.start(0)+len(s)
            else:
                if debug:
                    offset = m.end(0)
                else:
                    template = template[:m.start(0)]+template[m.end(0):]
                    offset = m.start(0)
            m = p.search(template, offset)
        return template

    if type(vars) == dict:
        return dodos(template, vars)
    return '\n'.join([dodos(template, var) for var in vars])
