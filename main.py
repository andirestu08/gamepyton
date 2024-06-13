from game1 import Pahlawan,musuh
from senjata import busur, pedang

pahlawan = Pahlawan (nama ="pahlawan", kesehatan=100, kerusakan=0) 
pahlawan.perlengkapan(pedang)
musuh = musuh(nama="musuh", kesehatan=100, senjata=busur )

while True:
   pahlawan.serangan (musuh)
   musuh.serangan(pahlawan)
   
   pahlawan.bar_kesehatan.draw()
   musuh.bar_kesehatan.draw()
   
   print(f"kesehatan dari {pahlawan.nama}: {pahlawan.kesehatan}")
   print(f"kesehatan dari {musuh.nama}: {musuh.kesehatan}")



   input()
   

