from senjata import pedang
from bar_kesehatan import bar_nyawa

class Character:
    
    def __init__(self,nama:str,kesehatan: int,kerusakan :int) ->None:
        self.nama = nama
        self.kesehatan = kesehatan
        self.kesehatan_max = kesehatan
        
        self.senjata = pedang
    
    def serangan(self, target) ->  None:
        target.kesehatan -= self.senjata.kerusakan
        target.kesehatan =  max(target.kesehatan, 0 )
        target.bar_kesehatan.update()
        print(f"{self.nama} terkena {self.senjata.kerusakan} kerusakan {target.nama} dengan {self.senjata.nama}")
        
        
class Pahlawan(Character):
    def __init__(self, nama, kesehatan, kerusakan):
        super().__init__(nama = nama, kesehatan = kesehatan, kerusakan = kerusakan)
        self.bar_kesehatan = bar_nyawa(self, panjang=100, perwarnaan="default", warna="hijau")
        
        self.tanpa_senjata = self.senjata
        self.bar_kesehatan = bar_nyawa(self, warna="hijau", panjang=0, perwarnaan = 0)
        self.bar_kerusakan = self.kerusakan
    
    def perlengkapan(self,senjata)-> None:
        self.senjata = senjata
        print(f"{self.nama} perlenkapan a(n){self.senjata.nama}!")
        
        
    def copot(self)-> None :
        print(f"{self.nama} copot {self.senjata.nama}!")
        self.senjata=self.tanpa_senjata
        
        
class musuh (Character):
    def __init__(self, nama: str,
                 kesehatan: int, 
                 senjata,
                 kerusakan: int) -> None:
        super().__init__(nama=nama, kesehatan=kesehatan, kerusakan=kerusakan)
        self.senjata = senjata
        self.bar_kesehatan = bar_nyawa(self, warna="merah")
        
