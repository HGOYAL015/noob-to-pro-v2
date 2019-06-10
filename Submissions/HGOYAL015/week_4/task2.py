import psutil
print("Total CPU percent usage : \n" +str(psutil.cpu_percent(interval=1))+"\n")
print("Total no: of Cores in CPU: "+str(psutil.cpu_count())+"\n")
ram=dict(psutil.virtual_memory()._asdict())
battery = psutil.sensors_battery()
print(str(battery)+" \n")
for x in ram:
    print (x,":",ram[x])
print("\n Disk Information:")
disk=psutil.disk_partitions()
for i in disk:
    print (i)


   
