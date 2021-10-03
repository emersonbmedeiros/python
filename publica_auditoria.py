import psutil
import paho.mqtt.publish as publish
import platform
import shutil
import psutil

so = (platform.system())
versao = (platform.release())
hostname = (platform.node())
sensor_cpu = psutil.cpu_percent(interval=1)
sensor_disco = psutil.disk_partitions()
sensor_memoria = psutil.virtual_memory().percent
total, used, free = shutil.disk_usage("/")
#print("Total: % dGB" % (total / (2**30)))
#print("Used: %d GB" % (used / (2**30)))
espaco_livre = ("%dGB" % (free / (2**30)))

comando = "so:"+str(so+versao)+ ', ' "origem:"+str(hostname)+ ', ' "espaco_livre:"+str(espaco_livre) + ', ' "sensor_cpu:"+str(sensor_cpu) + ', ' "sensor_ram:"+str(sensor_memoria)
print(comando)
publish.single("pi/auditoria", comando, hostname="broker.emqx.io")
