from abc import ABCMeta, abstractmethod
from textwrap import dedent


class Template(metaclass=ABCMeta):

    def __init__(self):
        self._parts = []

    def add(self, value):
        self._parts.append(value)

    def format(self, **kwargs):
        delete = object()
        originals = {}
        for key in kwargs:
            if hasattr(self, key):
                originals[key] = getattr(self, key)
            else:
                originals[key] = delete
        try:
            for key, value in kwargs.items():
                setattr(self, key, value)
            self._parts.clear()
            self.run()
            return ''.join(self._parts)
        finally:
            for key, value in originals.items():
                if value is delete:
                    delattr(self, key)
                else:
                    setattr(self, key, value)

    @abstractmethod
    def run(self):
        pass


class HTMLTemplate(Template):
    HTML_LANG = 'en'

    def add(self, value):
        value = value.strip()
        value = dedent(value)
        self._parts.append(value)

    def run(self):
        self.doctype()
        self.html_element()

    def doctype(self):
        self.add('<!doctype html>')

    def html_element(self):
        with self.tag('html', {'lang': self.HTML_LANG}):
            self.head_element()
            self.body_element()

    def tag(self, name, attrs=None, void=False):
        return Tag(self, name, attrs or {}, void)

    def head_element(self):
        with self.tag('head'):
            self.head()

    def head(self):
        pass

    def body_element(self):
        with self.tag('body'):
            self.body()

    def body(self):
        pass


class Tag:
    def __init__(self, template, name, attrs, void):
        self.template = template
        self.name = name
        self.attrs = attrs
        self.void = void
        if void:
            self.template.add(f'<{self.name}{self._extras()}>')

    def _extras(self):
        extras = ''
        attrs = self.attrs
        if attrs:
            items = attrs.items()
            pairs = ' '.join(f'{key}="{value}"' for key, value in items)
            extras = ' ' + pairs
        return extras

    def __enter__(self):
        assert not self.void
        self.template.add(f'<{self.name}{self._extras()}>')

    def __exit__(self, exc_type, exc_inst, exc_tb):
        self.template.add(f'</{self.name}>')
