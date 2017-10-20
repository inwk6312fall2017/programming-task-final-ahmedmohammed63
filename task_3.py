with open('running-config.cfg', 'r+') as f:
     x = f.readlines()
     s = len(x)
     new_list = []
     y = []                
     for items in x:
         if "172" not in items:
            new_list.append(items)
         else:
            items = items.replace("172","192")
            new_list.append(items)
                            
     print(new_list)     
