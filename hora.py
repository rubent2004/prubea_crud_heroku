import pytz
from datetime import datetime


# Fecha y hora actuales en UTC
utc_time = datetime.now(pytz.utc)

# Convertir la fecha y hora a la zona horaria de El Salvador
local_time = utc_time.astimezone()
#commit de prueba
print("Fecha y hora UTC:", utc_time)
print("Fecha y hora local (El Salvador):", local_time)
