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

    scene bg blank with fade
    'Lucien memejamkan mata.'
    scene bg ruangHampa with fade
    show lucien tired at center with dissolve
    
    lucien 'Jika baru satu pintu saja bisa mengubah fondasi dunia…'
    lucien 'Bagaimana jika aku membuka dua pintu lainnya?'
    lucien 'Apakah dunia ini masih bisa bertahan?'
    hide lucien with dissolve

    'Kabut perak mengalir cepat, menelan Nexus sedikit demi sedikit.'

    'Pintu-pintu berderak seperti menunggu untuk dipilih kembali.'

    'Perang baru dimulai.'
    'Dan kamu baru melewati pintu pertama.'

    scene bg TEMPLATE with fade
    # LAB BAWAH TANAH

    'Laboratorium bawah tanah itu sunyi seperti ruangan yang sengaja dilupakan. Cahaya lampu neon memantul pada permukaan logam, menciptakan pantulan kabur seolah semuanya hanyalah ilusi.'

    'Lucien Vale menarik napas panjang saat ia duduk di kursi Infiltrasi struktur logam melingkar dengan kumpulan kabel yang menghubungkan pelipis, dada, dan tulang belakangnya.'
    'Kursi itu tampak seperti mesin untuk menyeberang ke mimpi… atau ke sesuatu yang lebih berbahaya dari mimpi.'

    show lucien determined at center with dissolve
    lucien 'Jadi, kita mulai sekarang?'
    show lucien determined at left with move
    show evelyn bicara at center with dissolve
    evelyn 'Jangan bertanya ‘mulai sekarang’, Lucien. Kita sudah mulai sejak kau duduk di kursi itu.'
    show evelyn bicara at right with move

    evelyn 'Sinyal stabil. Jangan biarkan emosimu mengganggu.'
    hide evelyn with dissolve
    show lucien tired at center with move
    'Lucien menghela nafas.'

    show lucien monolog at center with dissolve
    lucien 'Emosi yang bikin aku tetap manusia, Evelyn.'

    show evelyn fokus at right with dissolve
    evelyn 'Tidak. Emosi yang membuatmu tersesat.'
    evelyn 'Kau harus mengingat skrip Narasi yang sudah kita latih. Tidak ada improvisasi.'
    hide evelyn with dissolve

    'Marcus Hale muncul membawa headset monitoring, wajah cerianya langsung mencairkan ketegangan ruangan.'
    show marcus normal at left with dissolve
    marcus 'Bro, kalau kau mulai pusing atau ngerasa mau muntah, ingat: tarik napas, fokus, dan panggil gue.'

    marcus 'Aku tetep jadi anchor kamu, oke? Lo jangan hilang.'

    'Lucien tersenyum tipis.'
    show lucien senyumPalsu at center with dissolve

    lucien 'Tenang, aku nggak akan hilang'

    show marcus serius at left with dissolve
    marcus 'Lo sering ngomong gitu, tapi gue tahu kadang lo nggak balik sepenuhnya'

    'Ketika semua persiapan selesai, Profesor Alden Rowan masuk. Sosok tua itu membawa aroma buku-buku filsafat dan ambisi lama yang belum mati.'
    show marcus serius at left with dissolve:
        alpha 0.5
    show prof normal at right with dissolve
    prof 'Lucien, ingat apa yang kuceritakan.'

    show lucien calm at center with dissolve
    lucien 'Mengenai konsensus?'

    prof 'Konsensus yang represif harus dihancurkan. Dunia tidur terikat pada narasi palsu. Kau harus menemukan Titik Patah. Di sanalah, debu waktu disembunyikan.'
    lucien 'Aku tahu. Aku hanya… belum siap melihat semuanya.'
    show prof severe at right with dissolve
    prof 'Tidak ada yang pernah siap. Yang penting kau melangkah.'
    'Tangan Professor menyentuh bahu Lucien. Kehangatannya terasa aneh di ruangan yang dingin secara klinis.'

    show prof bijaksana at right with dissolve
    prof 'Serena akan menunggu di Nexus. Tapi hati-hatilah… dia bukan sekutu yang utuh.'

    'Nama itu membuat dada Lucien terasa tertarik ke dalam.'

    hide prof with dissolve
    hide marcus with dissolve

    'Serena Aisley.' 
    'Pemandu mimpi.' 
    'Penghalang. Dan sesuatu yang tidak bisa ia definisikan.'

    show evelyn fokus at right with dissolve
    evelyn 'Sesi dimulai dalam hitungan tiga. Fokus pada pola napas. Jangan memikirkan hal lain.'
    show marcus tawaRingan at left with dissolve
    marcus 'Bro, gue ada di sini. Jangan lupa cara berhenti kalau lo ngerasa dunia berubah bentuk.'
    show lucien determined at center with dissolve
    lucien '...Baik.'
    evelyn 'Dua…'
    evelyn 'Satu…'
    'Arus listrik turun melalui kabel, mengalir masuk ke syarafnya.'
    'Suara Evelyn semakin menjauh.'
    'Suara Marcus teredam seperti dari bawah air.'
    hide lucien with dissolve
    hide marcus with dissolve
    hide evelyn with dissolve
    scene bg blank with fade
    'Gelap berubah menjadi ruang tak bertepi, lalu perlahan membentuk struktur: jembatan cahaya, kabut biru, dan bayangan seorang perempuan yang berdiri di ujung horizon.'
    'Serena Aisley.'
        
    scene bg ruangHampa with dissolve
    show serena bicara at center with dissolve 
    serena 'Selamat datang kembali, Lucien. Nexus menunggu langkahmu.'
    show serena bicara at right with move
    show lucien determined at center with dissolve
    lucien 'Aku hanya datang untuk mencari Titik Patah. Tidak lebih.'
    show serena bicara at right with dissolve 
    serena 'Tidak lebih?'
    show serena bicaraSerius at right with dissolve 
    serena 'meskipun begitu. Tapi kau selalu kembali ke sini.'
    show lucien tense at center with dissolve
    lucien '...'

    serena 'The Nexus adalah jembatan.'
    serena 'Di sinilah kau memilih siapa yang akan kau sabotase.'
    show lucien focus at center with dissolve
    hide serena with dissolve
    lucien 'Jika ini benar-benar jembatan…'
    lucien 'maka aku tidak yakin dunia mana yang sedang kutinggalkan.'
    hide lucien with dissolve
    scene bg blank with fade
    'Cahaya redup itu merambat ke seluruh ruangan mimpi seperti kabut lembut. Lucien berdiri diam, matanya terbuka separuh, seolah ia masih memproses perpindahan tak wajar tersebut.'

    'Serena muncul di hadapannya, langkahnya ringan namun presisi. Bayangannya memanjang, seolah gravitasi tidak berlaku di tempat ini.'
    show serena bicaraSerius at center with dissolve
    serena 'Selamat datang… atau selamat kembali, Lucien.'
    show serena bicaraSerius at right with move

    show lucien exhausted at center with dissolve
    lucien 'Kenapa rasanya dunia ini… lebih padat dari mimpiku biasanya?'
    serena 'Karena ini bukan mimpi biasa. Ini Nexus—lapisan bawah dari mimpi manusia. Strukturnya… lebih nyata daripada dunia nyata jika kau terlalu lama di sini.'

    show lucien tired at center with dissolve
    lucien 'Nexus… dunia yang terasa seperti teka-teki. Tapi kenapa aku bisa masuk ke sini begitu mudah… dan kenapa dia menyapaku seperti sudah mengenal?'

    show serena SadSmile at right with dissolve
    serena 'Kau punya retakan dalam kesadaranmu, Lucien. Retakan itu membuka pintu yang seharusnya tertutup'

    show lucien tense at center with dissolve
    lucien 'Retakan…? Apa maksudmu aku rusak?'
    show lucien tense at left with move 
    show serena bicaraSerius at center with dissolve
    serena 'Bukan rusak. Berbeda.'

    '*Lantai nexus bergetar.'
    show serena bicara at right with dissolve
    show lucien suprise at center with move
    lucien 'Apa itu...?'

    serena 'Kita harus bergerak. Ada sesuatu yang tidak stabil di sisi timur Nexus.'
    show lucien tense at center with dissolve
    lucien 'Kau bilang Nexus stabil… ini kelihatan tidak stabil sama sekali!'

    show serena bicaraSerius at right with dissolve
    serena 'Aku bilang Nexus *seharusnya* stabil. Tapi ada infiltrasi energi asing beberapa hari terakhir.'
    
    show lucien focus at center with dissolve
    lucien 'Dan kau pikir aku ada hubungannya?'
    hide lucien with dissolve

    show serena bicara at center with dissolve
    'Serena tidak menjawab. Ia hanya menatapnya—tatapan penuh makna ambigu'
    show serena bicara at right with move

    show lucien focus at center with dissolve
    lucien 'Ada apa lagi sekarang?'
    hide serena with dissolve
    hide lucien with dissolve

    show serena bicaraSerius at center with dissolve
    serena 'Dunia ini mulai mengingatmu.'
    show serena bicaraSerius at right with move

    show lucien suprise at center with dissolve
    lucien 'Mengingatku…? Apa yang pernah kulakukan di sini?'

    'sebelum bisa bertanya lebih jauh, Serena menarik lengannya'

    serena 'Kita harus pergi. Sekarang juga.'
    hide lucien with dissolve
    hide serena with dissolve

    show serena bicaraSerius at center with dissolve
    serena 'Kau bukan satu-satunya yang bangun di Nexus hari ini.'
    show serena bicaraSerius at right with move
    
    show lucien focus at center with dissolve
    lucien 'Maksudmu... ada orang lain?'
    show serena bicaraSerius at right with dissolve
    serena 'Bukan orang.'
    serena 'Dan dia sedang mencarimu.'
    return