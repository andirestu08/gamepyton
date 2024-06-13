class senjata:
    def __init__(self, nama: str, tipe_senjata:str,kerusakan: int,kekuatan: int, nilai:int ) -> None:
        self.nama = nama
        self.tipe_senjata = tipe_senjata
        self.kerusakan=kerusakan
        self.kekuatan=kekuatan
        self.nilai=nilai
        
        
pedang =senjata(nama="pedang",
               tipe_senjata="tajam",
               kekuatan=5,
               kerusakan=5,
               nilai=10)

busur =senjata(nama="busur",
               tipe_senjata="terbang",
               kekuatan=4,
               kerusakan=7,
               nilai=8)

pukulan =senjata(nama="pukulan",
               tipe_senjata="tumpul",
               kekuatan=2,
               kerusakan=6,
               nilai=20)
