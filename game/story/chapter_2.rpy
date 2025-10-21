label chapter_2:
    play music Nexus_Ambient fadein 1.0
    scene bg ruangHampa with fade
    'Lucien merasakan dinginnya udara The Nexus, ruang hampa yang dingin di bawah langit keperakan yang suram.'
    'Di depannya, Serena Aisley, The Arsitek, menatap tiga gerbang bercahaya yang berputar pelan di kejauhan.'
    show serena bicaraSerius at center with dissolve

    serena 'Kau tidak punya banyak waktu, Lucien.'
    serena 'Setiap detik yang kau habiskan di Nexus adalah ketidakstabilan di dunia nyata. Pilih.'
    serena 'Tiga gerbang, tiga pejabat. Kepala Dewan Legislatif, Menteri Informasi, atau Juru Bicara Presiden.'

    hide serena with dissolve

    'Gerbang pertama bersinar dengan warna biru muda Gerbang Logika.'
    'Gerbang kedua berwarna kuning keemasan sebuah Gerbang Ambisi.'
    'Gerbang ketiga berwarna merah gelap merupakan Gerbang Ketakutan.'

    'Evelyn, telah merencanakan untuk memulai dengan Kepala Dewan Legislatif, karena ia diyakini paling didorong oleh logika kaku yang rapuh.'
    # Lucien fokus pada Gerbang Logika.
    menu gerbang:
            "gerbang mana yang akan kamu pilih?"
            "Gerbang Logika":
                return
            "Gerbang Ambisi":
                return
            "Gerbang Ketakutan":
                return
    return

# Buat akibat dari setiap keputusan yang diambil