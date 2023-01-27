http_status = 900;
if http_status==200 or http_status== 201:
  print("success");
elif http_status==400:
    print("bad request");
elif http_status==404:
    print("Not found");
elif http_status==500 or http_status== 501:
    print("Server Error")
else:
    print("unknown")
    
#we will run same condition in match statement

match http_status:
    case 200 | 201:
        print("success")
    case 400:
        print("bad request");
    case 404:
        print("Not found");
    case 500|501:
        print("Server Error")
    case _:
        print("unknown")
        
        
    



    
