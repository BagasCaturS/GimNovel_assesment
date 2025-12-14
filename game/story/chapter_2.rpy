label chapter_2:
    play music Nexus_Ambient fadein 1.0
    scene bg bg_chapter_2 with fade 
    'Lucien merasakan dinginnya udara The Nexus, ruang hampa yang dingin di bawah langit keperakan yang suram.'

    scene bg ruangHampa with fade
    'Kabut perak itu berputar pelan, menggantung seperti embusan napas raksasa yang tidak terlihat. Lucien menelan ludah saat matanya tertuju pada tiga pintu yang melayang tinggi.'
    'Semuanya bersinar.'
    'Semuanya terlihat memanggil namanya.' 
    'Namun semuanya… menyembunyikan sesuatu.'
    
    'Serena Aisley berdiri di belakangnya seperti bayangan yang terlalu setia untuk ditinggalkan.'
    show serena bicaraSerius at right with dissolve
    serena 'Ingat, Lucien. Setiap pintu hanya terlihat berbeda… tapi setiap jalan akhirnya harus melewati Pintu Logika.'
    show lucien determined at left with dissolve
    lucien '…Logika. Jadi meski aku memilih pintu lain… ujungnya tetap kembali ke sana?'

    'Serena tidak menjawab. Mata peraknya hanya bergetar sedikit — cukup untuk membuat dada Lucien mengencang.'
    hide lucien with dissolve
    hide serena with dissolve
    jump pilihan_gerbang
    return
# Buat akibat dari setiap keputusan yang diambil

label pilihan_gerbang:
    scene bg ruangHampa2 with fade
    show lucien monolog at center with dissolve
    lucien 'Ini bukan sekadar memilih rute. Ini memilih bagaimana aku akan dikenang oleh para Nexus — oleh dunia ini. Tapi pada akhirnya… apa pun yang kupilih, aku akan kembali ke Logika. Seolah dunia ini memaksaku menghadapi satu kebenaran.'
    hide lucien with dissolve
    
    'Ia mengangkat tangan.'

    call screen pilihan_gerbang_visual
    
    return 

label pilihan_gerbang_repeat:
    scene bg ruangHampa2 with fade
    show lucien focus at center with dissolve
    "Aku pikir gerbang logika merupakan jalan yang benar"
    hide lucien focus with dissolve
    call screen pilihan_gerbang_visual
    return


label gerbang_logika:
    
    show lucien determined at center with dissolve
    lucien 'Baiklah, pintu biru. Aku siap!'

    hide lucien with dissolve
    'Cahaya biru menyala seperti denyut nadi raksasa.'

    'Tubuh Lucien ditarik masuk, terdorong oleh angin digital yang tidak memiliki bentuk. Di sekelilingnya, garis-garis seperti kode membungkus tubuhnya.'
    show lucien realization at center with dissolve
    show lucien realization at left with dissolve
    lucien 'A-aku… terpecah?'

    'Suara Serena terdengar menggema.'

    show serena bicaraSerius at right with dissolve
    serena 'kau tidak terpecah... kau sedang disusun ulang'
    
    hide serena with dissolve
    'Semuanya memudar.'
    hide lucien with dissolve  

    jump inside_gerbang_logika

    return


label inside_gerbang_logika:
    scene bg TEMPLATE with fade
    'Ia muncul di dalam ruangan raksasa — seakan seluruh dunia dibangun oleh kaca steril dan logam dingin.'
    'Setiap langkahnya memantulkan suaranya sendiri.'

    show lucien tense at center with dissolve
    lucien 'Ruang ini… tidak punya jiwa.' 
    hide lucien with dissolve

    'Di tengah ruangan muncul hologram pewujud dari pejabat legislatif — jauh lebih muda, namun terlihat kelelahan.'
    show dewan cold at center with dissolve
    dewan 'Siapa kamu?'
    show dewan cold at right with move
    
    show lucien focus at center with dissolve
    show lucien focus at left with move
    lucien 'Aku hanya… seseorang yang ingin memahami apa yang kau sembunyikan.'

    'Sosok itu tidak menjawab, hanya memalingkan wajah ke arah dinding kosong — dinding yang menjadi Bingkai Trauma. Bingkai itu bergetar. Retakan kecil menyebar. Lucien maju satu langkah.'
    hide dewan with dissolve

    show lucien focus at center with move
    lucien 'Ini Level 1. Aku baru mulai… tapi dunia ini sudah ingin runtuh.'
    hide lucien with dissolve
    jump bingkai_titik_patah
return

label bingkai_titik_patah:
    $ pilihan = 0
    scene TEMPLATE with fade
    'Saat jarinya menyentuh bingkai, dunia pecah.'
    'Kegelapan melebur menjadi api dan kaca pecah. Jeritan mengambang seperti gema dari ribuan kenangan yang terdistorsi.'
    
    show dewan marah at center with dissolve
    dewan 'Ini… ini yang membuat semuanya hancur…'
    show dewan marah at right with move
    hide dewan with dissolve
    show lucien focus at center with dissolve
    'Lucien ingin menjangkau, tapi retakan lain muncul di langit mimpi.'

    menu:
        'Cahaya di lantai berubah, membentuk 3 jalur:'

        'Sentuh bingkai dengan lembut':
            $ pilihan = 1
        'Hancurkan bingkai secara paksa':
            $ pilihan = 2
        'Tinggalkan bingkai':
            $ pilihan = 3
    
    lucien 'Setiap keputusan membentuk akhir. Aku tidak boleh gegabah…'
    hide lucien with dissolve

    jump diluar_mimpi
    return 

label diluar_mimpi:
    scene bg blank with fade
    'Di luar mimpi, dunia nyata mulai kacau.'
    scene bg TEMPLATE with fade
    'Lampu berkedip. Monitor EEG naik turun liar.'
    show marcus urgent at center with dissolve
    marcus 'Lampu berkedip. Monitor EEG naik turun liar.'
    show marcus urgent at left with move

    show evelyn frantic at center with dissolve
    evelyn "Tidak! Nexus mendesak dia menyelesaikan pilihan!"
    show evelyn frantic at right with move
    hide marcus with dissolve
    hide evelyn with dissolve

    # pindah lokasi ke mimpi
    scene bg TEMPLATE with fade
    show lucien tense at center with dissolve
    '...'
    show lucien suprise at center with dissolve
    serena '(Suara dalam kepala) Hati-hati, Lucien… satu pilihan salah, realitas bisa pecah.'

    jump level_2_scene_6
    return

label level_2_scene_6:
    scene bg TEMPLATE with fade
    'Lucien menatap tiga jalur.'

    lucien 'Apakah rasa sakit masa lalu harus dihapus… atau dimengerti?'
    lucien 'Atau... tidak kusentuh sama sekali?'

    if pilihan == 1:
        'Dia membuat keputusan sentuh bingkai dengan lembut'
    elif pilihan == 2:
        'Dia membuat keputusan hancurkan bingkai secara paksa'
    elif pilihan == 3:
        'Dia membuat keputusan Tinggalkan bingkai'

    
    'Saat ia menyentuh jalurnya, dunia pecah oleh cahaya biru.'

    jump back_to_nexus_scene_7
    return

label back_to_nexus_scene_7:
    scene bg blank with fade
    'Lucien muncul kembali di The Nexus, tersungkur. Lantai retak-retak seperti kaca yang disiram suhu ekstrem.'

    scene bg ruangHampa2 with fade
    'Serena kini tampak lebih transparan, hampir tembus pandang.'
    show serena bicaraSerius at center with dissolve:
        alpha 0.5
    serena 'Kau membuat Konsensus bergetar. Realitas berubah.'
    show serena bicaraSerius at right with move:
        alpha 0.5
    show lucien exhausted at center with dissolve
    show lucien exhausted at left with move
    lucien 'Aku… cuma memilih satu pintu.'
    show lucien exhausted at left with dissolve
    lucien 'Bagaimana bisa ini terjadi?'

    serena 'Tidak.'
    serena 'Kau memilih jalur nasib.'

    hide lucien with dissolve
    # show serena bicaraSerius at center with dissolve
    scene bg ruangHampa with fade
    show serena bicaraSerius at center with dissolve:
        alpha 0.5
    hide serena
    'Di belakang Serena, tiga pintu kembali muncul — namun kali ini lebih redup, lebih liar.'
    '3 Pintu.'
    '2 level.'
    '1 kebenaran.'
    'Ending-mu mulai terbentuk.'

    jump scene_8_closing_chapter
    return

label scene_8_closing_chapter:
    
    return