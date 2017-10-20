    
with open('running-config.cfg', 'r+') as f:
     x = f.readlines()
     for strings in x:
         strings = strings.split()
         print (strings)
     new_list = []
     y = []
     for items in x:
         if "172" not in items:
            new_list.append(items)
         else:
            items = items.replace("172","192")
            new_list.append(items)
     
     my_dict = {}
     s = len(strings)
     for strings in x:
        if "access" in strings:
           my_dict.append(strings[1] , strings[(s-1)]
           
                
         

    


