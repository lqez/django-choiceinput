from django.forms import widgets
from django.utils.safestring import mark_safe

__all__ = ('ChoiceInput', )


class ChoiceInput(widgets.TextInput):
    __PREFIX = 'helper_'
    __ONCHANGE = mark_safe('document.getElementById(\'id_\'+this.name.substr(%d)).value = this.options[this.selectedIndex].value;' % len(__PREFIX))

    def __init__(self, attrs=None, choices=()):
        self._helper = widgets.Select(attrs=attrs, choices=choices)
        super(ChoiceInput, self).__init__(attrs)

    def render(self, name, value, attrs=None):
        output = [
            super(ChoiceInput, self).render(name, value, attrs),
            self._helper.render(self.__PREFIX + name, value, {'onchange': self.__ONCHANGE}),
        ]
        return mark_safe('\n'.join(output))
