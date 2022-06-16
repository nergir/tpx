#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
from template import *
from cgi import escape

form = """
<form name=User action=?f=user method=post enctype=multipart/form-data onSubmit=return(check(this)) lang='Ar išsiųsti skelbimą?' onReset="return(confirm('Ar išvalyti anketos laukus?'))">
<p class=ln>Privilegija</p><select lang='0`Parinkite privilegija' name=Privilegija><option value=0><option value=1>Admin</option></select>
<fieldset><legend onclick=toggle(this.nextSibling) style=cursor:pointer>Informacija</legend><div>
<p class=ln>Vardas</p><input type=text name=Name style=text-transform:capitalize>
<br><p class=ln>Pavardė</p><input type=text name=Surname style=text-transform:capitalize>
<br><p class=ln>Gimtadienis</p><input type=text name=Gimtadienis> <input type=button title='Kalendorius' id=date class=sq onclick=showXY(event,'cldr') value=...>
<br><p class=ln>Slapyvardis</p><input type=text name=Slapyvardis>
<br><p class=ln>Slaptažodis</p><input type=password name=Login maxLength=20>
<!--human-->
</div>
</fieldset>
<fieldset><legend onclick=toggle(this.nextSibling) style=cursor:pointer>Kontaktai</legend><div>
<p class=ln>Telefonas</p><input type=text name=Telefonas maxLength=8>
<br><p class=ln>Paštas</p><input type=text name=Paštas maxLength=20>
</div>
</fieldset>
<fieldset><legend onclick=toggle(this.nextSibling) style=cursor:pointer>Adresas</legend><div>
<p class=ln>Miestas</p><input type=text name=Miestas style=text-transform:capitalize>
<br><p class=ln>Gatvė</p><input type=text name=Gatvė>
<br><p class=ln>Namas</p><input type=text name=Namas>
<br><p class=ln>Butas</p><input type=text name=Butas>
</div>
</fieldset>
<fieldset><legend onclick=toggle(this.nextSibling) style=cursor:pointer>Extra</legend><div style=display:none>
<p class=ln>Kaina</p><input type=text name=Kaina maxLength=20> <input type=button title='Kalkuliatorius' id=number class=sq onclick=showXY(event,'calc') value=...>
<br><p class=ln>Spalva</p><input type=text name=Spalva maxLength=6 style=text-transform:uppercase onkeydown=keydown(event,'clrs') onkeyup=if((s=clrget(Title(this.value)))==this.value)return;this.value=s;color.style.backgroundColor=s> <input type=button title='Spalvų paletė' id=color class=sq onclick=showXY(event,'clrs') value=...>
<br><p class=ln>Logo</p><input name=Logo lang='/^\d+(,\d+)*$/'> <input type=button class=sq value=... onclick=showXY(event,'upload',uploading,'Byla') title='Parinkti bylą'>
<br><p class=ln>Foto</p><input name=Foto lang='/^\d+(,\d+)*$/'> <input type=button class=sq value=... onclick=showXY(event,'upload',uploading,'Byla') title='Parinkti bylą'>
<br><p class=ln>CV</p><input name=CV lang='/^\d+(,\d+)*$/'>
</div>
</fieldset>
<img src=img/1.ico title=Tinka onclick=dosubmit(this)>
<img src=img/reset.ico title=Valyti onclick=doreset(this)>
<img src=img/help.ico title=Pagalba onclick=doPagalba()>
<img src=img/save.ico title=Atsiminti onclick=doForma(this,1)>
<img src=img/open.ico title=Atverti onclick=doForma(this)>
<img src=null.ico class='icon id' title=ID onclick=doID(this)>
<input type=submit value=' ' Pateikti style=width:16;height:16;border:0>
<input type=hidden name=ID>
</form>
<input value=321 name=demo>
<input name=test value=123>
"""
line = """
<html>
<head>
	<title>ngs | ng solution. For everyone</title>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<!--ona at-si-ti-ko -->
<!--tbl
	this is the
	total
	<!--tr
		<!--this 
		is another {sources}
		this--><!--secondas 
		
		
		secondas--> 
	tr-->
	first
-->
<!--content
	hello
	<!--subcontent
		inside of hello1
	subcontent-->
	<!--subcontent
		inside of hello2
	subcontent-->
	there
-->
<!-- 
one toksdalykas 



dar karteli
padaryta

-->
</head>
<body>
This place for static block assign programically self
<hr>
{hello_world}
<hr>
<table>
    <!-- START row -->
        <tr>
            <!-- START cell --><td>{td_value}</td><!-- END cell -->
        </tr>
    <!-- END row -->
</table>
<hr>
<div>
    BARS IN BERLIN:
    <!-- START bar -->
    <ul>
        <li><strong>{name}</strong></li>
        <li>{desc}</li>
    </ul>
    <!-- END bar -->
</div>
<hr>
Coding PHP is <!-- START opt1 -->fun<!-- END opt1 --><!-- START opt2 -->boring<!-- END opt2 -->
<hr>
<!-- list {variable1} {variable2} list -->
<hr>
<div name=div></div>
<hr>
My invented code advantage:<xmp>For description changed {} to [], name to nane
< !-- START blockname -- >...< !-- END blockname -- > => < !-- blockname ... blockname -- > Visible block.(optional if fix=True)
< !-- blockname ...-- > => Not visible block, can output only self or if is [blockname] inside visible block.
[source] => [source] if is debug=True and undefined block
<form nane=form1>...</form> => [form1]
<form>...</from> => [form] (only if form is one)
<tag nane=name0>...</tag> => <tag nane=name0>[name0]</tag>
<input type=text name=value1> => <input type name=value value=[value1]>
<input type=text nane=value2 value='dont overwrite default'> => <input type nane=value2 value='dont overwrite default'>
<textarea nane=text></textarea> => <textarea nane=text>[text]</textarea>
For future
< !-- url -- > or < !-- INCLUDE ...-- > - include file like template,css,js or other
<select nane=select1></select> => <select nane=select1><option value=value1><option value=value2>...<option value=valuen></select>
Your comments,feedbacks and bugs send me by email girner@gmail.com
</xmp>

<hr>
%s
</body>
</html>
""" % form

debug = False
if debug:
    load_template(line)
    parse_fix()
    parse_block()
    parse_variable()
    parse_form()
    print(load_template())
    line = load_template()
else:
    line = load_template(line, fix=True, block=True,
                         variable=True, form=True, overwrite=True)
#raise SystemExit

debug = False

set_block('opt2' if True else 'otp1')
rows = []
for tr in range(3):
    vars = []
    for td in range(3):
        vars.append({'td_value': '%s:%s' % (tr, td)})
    cell = assign_block('cell', vars)
    rows.append({'cell': cell})
row = assign_block('row', rows)

vars = (
    {'variable1': 'variable1', 'variable2': 'variable2'},
    {'variable1': 'variable1', 'variable2': 'variable2'},
)
list = assign_block('list', vars, debug=debug)
vars = (
    {'name': 'Sonderbar', 'desc': 'best red vine in town'},
    {'name': 'Wunderbar', 'desc': 'happy hour ends at 9 pm'},
)
bar = assign_block('bar', vars, debug=debug)
vars = {'list': list, 'bar': bar, 'row': row,
        'hello_world': 'hello world!',
        'Miestas': 'Klaipėda',
        'Paštas': 'girner@gmail.com',
        'Telefonas': '+370-611-38490',
        'Name': 'Nerijus',
        'Surname': 'Girskis',
        'Slapyvardis': 'girner',
        'Gimtadienis': '0000-03-18',
        'test': 'overwrited',
        'demo': '<fix><overwrite>',
        'div': 'work where inside name attribute(optional by allowed tags: textarea, select, iframe, div), can skip with value attribute',
        }
globals().update(vars)


def main(str=False):
    text = assign(line, debug=debug, vars=vars)
    if str:
        return text
    print(text)
    print('<pre>')
    print('vars=', vars.keys())
    print('blocks=', blocks.keys())
    print('#'*80)
    print(escape(open(__file__, 'r').read()))
    print('#'*80)
    print('locals', locals().keys())
    print('globals', globals().keys())
    print('</pre>')


if __name__ == "__main__":
    main()
else:
    dummy = 1
