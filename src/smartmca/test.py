from smartmca import SmartMCA
from smartmca import Config 
mca = SmartMCA()

mca.connect("http://192.168.102.120", "user", "password")
mca.get_server_status()
config = mca.get_processing_configuration()

print(config)

config.baseline_hold=2000
config.trigger_mode = Config.TriggerMode.EXTERNAL
mca.set_processing_configuration(config)

config = mca.get_processing_configuration()

print(config    )