from collections import OrderedDict

od = OrderedDict([('b', 2), ('c', 3)])

od.update({'e': 1})           
od.move_to_end('e', last=False)  

print(od)
