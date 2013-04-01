django-choiceinput
==================

- Display preset strings as select tag right beside TextInput widget in Django.
- This can be useful when you want to provide some examples but you're using default TextInput widget.


Installation
------------
via pip:

    $ pip install django-choiceinput

Usage
-----
*django-choiceinput* provides `widgets.ChoiceInput`.

    from django import forms
    from choiceinput.widgets import ChoiceInput

    class WebLogFilterForm(forms.ModelForm):
        useragent = forms.CharField(max_length=100, widget=ChoiceInput(
            choices=(('(iPhone|iPod|iPad)', 'iOS'), ('Android', 'Android'))
        ))

        
Author
------
- Park, Hyunwoo \<ez.amiryo at gmail.com\>

Disclaimer
----------
Distributed under MIT license.
