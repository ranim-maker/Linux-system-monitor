import platform
import os
import psutil
print("==================================================")
print("            LINUX SYSTEM MONITOR               ")
print("==================================================")


print("\n--SYSTEME--")
print("Système :",platform.system())
print("Système :",platform.release())
print("Système :",platform.node())




print("\n--PROCESSEUR--")
print("nombre de coeurs logiques :",psutil.cpu_count())
print("Utilisation CPU :", psutil.cpu_percent(interval=1), "%")





print("\n--MEMOIRE RAM--")
ram=psutil.virtual_memory()
print("RAM total :",round(ram.total /(1024**3),2),"GO")
print("RAM utilisée :",round(ram.used /(1024**3),2),"GO")
print("RAM disponible :",round(ram.available /(1024**3),2),"GO")
print("RAM utilisée :",ram.percent,"%")




print("\n--ESPACE DISQUE--")
disk=os.statvfs("/")
total=disk.f_blocks * disk.f_frsize
free=disk.f_bavail * disk.f_frsize
used=total-free




print("Espace total :",round(total /(1024**3),2),"GO")
print("Espace used :",round(used /(1024**3),2),"GO")
print("Espace free :",round(free /(1024**3),2),"GO")





