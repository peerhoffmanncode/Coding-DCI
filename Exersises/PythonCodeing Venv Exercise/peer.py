import npyscreen

class ClassMateForm(npyscreen.Form):
    def create(self):
        self.myName        = self.add(npyscreen.TitleText, name='Classmate')
        self.myRoll        = self.add(npyscreen.TitleSelectOne, scroll_exit=True, max_height=3, name='Options', values = ['Nice', 'Neutral', 'Boring'])
        self.myDate        = self.add(npyscreen.TitleDateCombo, name='Date since in class')


def get_new_class_mate(*args):
    F = ClassMateForm(name = "Classmate")
    F.edit()
    return "Created record for " + F.myName.value

if __name__ == '__main__':
    print(npyscreen.wrapper_basic(get_new_class_mate))