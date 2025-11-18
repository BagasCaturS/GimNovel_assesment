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
    serena 'Ingat Lucien, Kau harus yakin agar ketiga gerbang itu menunjukkan Aura Sesungguhnya.'
    serena 'Gerbang pertama bersinar dengan warna biru muda Gerbang Logika.'
    serena 'Gerbang kedua berwarna kuning keemasan sebuah Gerbang Ambisi.'
    serena 'Gerbang ketiga berwarna merah gelap merupakan Gerbang Ketakutan.'

    hide serena with dissolve

    show lucien lookAround at center with dissolve
    'Evelyn, telah merencanakan untuk memulai dengan Kepala Dewan Legislatif, karena ia diyakini paling didorong oleh logika kaku yang rapuh.'
    
    'Tapi setiap keputusan ada ditangan mu.'
    hide lucien lookAround with dissolve

    scene bg ruangHampa2 with fade
    # Lucien fokus pada Gerbang Logika.
    show serena bicaraSerius at center with dissolve
    'Pikirkan pilihan mu dengan baik, Lucien. Karena setelah memilih, tidak ada jalan kembali. Selain menyeleasikannya misi ini.'
    hide serena with dissolve
    call screen pilihan_gerbang_visual


label gerbang_logika:
    
    serena 'logika.'

    return

label gerbang_ambisi:

    serena 'ambisi'

    return

label gerbang_ketakutan:
    
    serena 'ketakutan.'

    return
