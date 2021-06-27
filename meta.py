class MetaAleph(type):

    print('<[100]> MetaAleph body')
 
    def __init__(cls, name, bases, dic):
        super().__init__(name, bases, dic)
        print('<[500]> MetaAleph.__init__')
        print('<[501]> MetaAleph. —— name:', name)
        print('<[502]> MetaAleph. —— bases:', bases)
        print('<[503]> MetaAleph. —— dic：', dic)     # dic 中包含ClassFive的class_name、__init__、__new__、__call__
 
    def __new__(cls, name, bases, dic):
        print('<[600]> MetaAleph.__new__')
        return super().__new__(cls, name, bases, dic)
 
    def __call__(self, *args, **kwargs):
        print('<[700]> MetaAleph.__call__')
        print(args)
        print(kwargs)
        return super().__call__(*args, **kwargs)
 
class ClassFive(metaclass=MetaAleph):
    print('<[6]> ClassFive body start')
    class_name = 'ClassFive'
    def __init__(self,*args,**kwargs):
        print("{}{} in ClassFive.__init__".format(str(args),str(kwargs)))
        print('<[7]> ClassFive.__init__')
 
    def __new__(cls, *args, **kwargs):
        print("{}{} in ClassFive.__new__".format(str(args),str(kwargs)))
        print('<[8]> ClassFive.__new__')
        return super().__new__(cls)
 
    def __call__(self, *args, **kwargs):
        print("{}{} in ClassFive.__call__".format(str(args),str(kwargs)))
        print('<[9]> ClassFive.__call__')
        return '<[10]> ClassFive.__call__ return'

five = ClassFive(x=1)
five(x=3)
