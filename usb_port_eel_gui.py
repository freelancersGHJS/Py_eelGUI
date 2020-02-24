import eel
import serial.tools.list_ports
eel.init('web')

@eel.expose
def main():
    class usb_ports_gui:
        def window_usb_ports(self):
            global usb_ports
            usb_ports = []
            for port in serial.tools.list_ports.comports():
                port_ = str(port)
                list_ = port_.split(" ")
                concat = ""
                for i in range(2, len(list_) - 1):
                    concat = concat + list_[i] + " "
                usb_ports.append([list_[0], concat])
            usb_list = []
            for i in usb_ports:
                usb_list.append([i[0] + "  " + i[1], i[1].split(" ")[0]])

            usb_port_name = usb_ports_gui.usb_port_count(self,usb_list)
            return [usb_port_name,len(usb_list)]

        def linux_usb_ports(self):
            global usb_ports
            usb_ports = []
            for port in serial.tools.list_ports.comports():
                port_ = str(port)
                #print(port)
                list_= port_.split(" ")
                concat = ""
                for i in range(2,len(list_)):
                    concat = concat+list_[i]+" "
                string = list_[0][slice(5, len(list_[0]))] + "  " + concat
                usb_ports.append([string,string.split(" ")[2]])
            #print(usb_ports)
            usb_port_name = usb_ports_gui.usb_port_count(self,usb_ports)
            return [usb_port_name,len(usb_ports)]

        def usb_port_count(self,usb_ports):
            ignore = []
            count = 0
            list_ = []
            for i in range(0, len(usb_ports)):
                com1 = usb_ports[i][1]
                for j in range(i,len(usb_ports)):
                    com2 = usb_ports[j][1]
                    if j not in ignore:
                        if com1 == com2:
                            ignore.append(j)
                            count +=1
                if count != 0:
                    list_.append([usb_ports[i][0],count])
                count = 0
            global eel_list
            eel_list = []
            #usb_ports_gui.gui(self,list_)
            for i in list_:
                temp_list = []
                concat = ""
                i = i[0].split(" ")
                for j in range(1,len(i)-1):
                    concat +=i[j]+" "
                temp_list.append(concat)
                for k in usb_ports:
                    if concat in k[0]:
                        id = k[0].split(" ")[0]
                        temp_list.append(id)
                eel_list.append(temp_list)
            return eel_list

    obj1 = usb_ports_gui()
    f_usb_list = obj1.linux_usb_ports()
    usb_list = f_usb_list[0]
    port_length = f_usb_list[1]
    print(usb_list,port_length)
    eel.js_function(usb_list,port_length)

eel.start('index.html',size=(200,200))
