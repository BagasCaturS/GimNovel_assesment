label chapter_2:
    play music Nexus_Ambient fadein 1.0
    scene bg bg_chapter_2 with fade 
    'Lucien merasakan dinginnya udara The Nexus, ruang hampa yang dingin di bawah langit keperakan yang suram.'
    
    jump pilihan_gerbang
    return
# Buat akibat dari setiap keputusan yang diambil

label pilihan_gerbang:
    scene bg ruangHampa with fade
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
                jump gerbang_logika
                return
            "Gerbang Ambisi":
                jump gerbang_ambisi
                return
            "Gerbang Ketakutan":
                jump gerbang_ketakutan
                return
    return