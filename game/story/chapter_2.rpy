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
    scene bg ruang_logika with fade
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
return