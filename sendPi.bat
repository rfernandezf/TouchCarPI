pscp -r -pw raspberry touchcarpi pi@192.168.1.200:Shared
plink -ssh -P 22 -pw raspberry pi@192.168.1.200: chmod 777 Shared/touchcarpi/main/__init__.py