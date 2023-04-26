import nmap

scanner = nmap.PortScanner()


def get_port(target,port):
    res = scanner.scan(target,str(port))
    # ip = list(res['scan'].keys())
    # target = ip[0]
    # status_up_down = res['scan'][target]['status']['state']
    # status_open_close = res['scan'][target]['tcp'][port]['state']
    # name = res['scan'][target]['tcp'][port]['name']
    # product = res['scan'][target]['tcp'][port]['product']
    # if product == '':
    #     product = "None"
    # res = {'Target':target,'Port':port,'Up/Down':status_up_down,'Port Status':status_open_close,'Name':name, 'Product':product}
    
    res = scanner.csv().split('\r')[1].removeprefix('\n')
    res = res.split(";")
    return res

def get_ports(target,ports=1024):
    reslst = []
    flag = False
    if ports == 1024:
        flag = True
    if isinstance(ports, list):  
        for port in ports:
            res = get_port(target,port)
            reslst.append(res)
    elif isinstance(ports, int) and flag == False:  
        res = get_port(target,ports)
        reslst.append(res)
    else:
        for port in range(1,ports):
            res = get_port(target,port)
            reslst.append(res)
    tittle = ['IP Addr','Host','','Protocol','Port','Service Name','State','Product','Extra Info','Reason','Version','Conf']
    reslst.insert(0,tittle)
    return reslst


# res = get_ports('scanme.nmap.org',[80])
# print(res)

# for i in res:
#     print(i)