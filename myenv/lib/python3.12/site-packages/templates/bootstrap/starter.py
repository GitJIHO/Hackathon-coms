from .base import Bootstrap


class Starter(Bootstrap):

    def title(self):
        self.add('Starter Template for Bootstrap')

    def head_extra(self):
        with self.tag('style'):
            self.add('''
body {
    padding-top: 5rem;
}
.starter-template {
    padding: 3rem 1.5rem;
    text-align: center;
}
            ''')

    def main(self):
        with self.tag('div', attrs={'class': 'starter-template'}):
            self.h1_element()
            with self.tag('p', attrs={'class': 'lead'}):
                self.add('''
Use this document as a way to quickly start any new project.<br>All you get is
this text and a mostly barebones HTML document.
                ''')

    def h1(self):
        self.add('Bootstrap starter template')
