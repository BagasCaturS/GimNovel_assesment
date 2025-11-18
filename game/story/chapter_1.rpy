label chapter_1:
    play music blue_edge fadein 1.0
    scene bg bg_chapter_1 with fade 

    'Lucien Vale berjalan di atas trotoar. Ia membiarkan earphone-nya mati. Ia membutuhkan keheningan mutlak untuk memastikan setiap langkahnya adalah miliknya sendiri.'
    'Ia memiliki keyakinan dingin: ia mampu menulis ulang realitas dengan memengaruhi mimpi orang lain (Dream Infiltration).'
    scene bg jalananKampus with fade 

    show lucien monolog at center
    with dissolve
    lucien 'Hanya meyakinkan diri sendiri bahwa hari ini adalah hari yang benar-benar baru. Hari yang belum pernah ada sebelumnya.'
    hide lucien with dissolve

    'Ia memandangi sekeliling. Toko-toko, lampu lalu lintas yang semuanya tampak terlalu pas, sebuah tata panggung yang sempurna, yang hanya membuatnya semakin curiga.'

    jump strategist_design
    return

label strategist_design: 
    'Lucien berbelok, dan Studio Desain Fakultas, pusat ambisinya, menjulang. Inilah Base Camp rahasianya.'


    scene bg studioDesain with fade

    'Di mejanya, ia menemukan Sketsa Pusaran. Itu adalah pola pusaran air rumit dengan titik biru kobalt di tengahnya, sebuah Master Plan dari misi mereka.'

    'Evelyn Crestfield adalah The Strategist. Ia menghampiri Lucien.'

    show evelyn bicara at right 
    with dissolve

    evelyn 'Pagi, Lucien. Persiapan semalam sudah final.'

    menu:
        'Pagi, Lucien. Persiapan semalam sudah final.'

        'Pagi juga, Evelyn':
            # Tambahin optional dialog
            show lucien calm at left with dissolve
            lucien 'pagi juga, Evelyn'

    evelyn 'Formula tidurnya sudah siap, berbasis stimulus gelombang theta yang kita dapat dari Alden. Kita harus mulai malam ini.'


    show lucien cemas at left with dissolve
    lucien 'Seberapa besar risikonya, Evelyn?'


    evelyn 'Risikonya nol, jika kau mengikuti logikanya. Kita akan memasuki mimpi para pejabat yang bertanggung jawab atas Undang-Undang Konsensus (UUK). Misi kita adalah mengubah Titik Patah ingatan krusial yang menopang keyakinan mereka terhadap UU represif itu.'

    hide evelyn with dissolve
    hide lucien with dissolve

    play music blue_edge fadeout 1.5
    jump shadow_anchor

    return

label shadow_anchor: 
    play music Mission_Blueprint fadein 1.0
    'Marcus Hale, The Anchor, Datang menghampiri.'
    
    show marcus normal at right with dissolve
    marcus 'Bro! Lo kenapa lihat sketsa itu kayak lihat hantu? Lo jangan aneh-aneh, ya. Kit ada tugas studio yang harusnya lo kerjain.'
    # hide marcus normal with fade out
    show lucien senyumPalsu at left with dissolve
    lucien 'Semuanya aman, Marcus. Aku cuma tidur larut.'
    hide marcus with dissolve
    show marcus serius with dissolve
    marcus 'Gua cuma nggak mau lihat lo kayak kesambet lagi.'
    hide marcus with dissolve
    hide lucien with dissolve
    
    jump mentor_code

    return

label mentor_code:

    scene bg ruangFilsafat with fade

    show lucien senyumPalsu at center with dissolve
    'Lucien menemukan Profesor Alden Rowan, The Mentor, di tengah tumpukan buku-buku lama.'
    hide lucien with dissolve
    
    show prof bijaksana at center with dissolve
    prof 'Lucien Vale. Aku sudah menunggumu. Ambil peralatan ini.'
    hide prof with dissolve
    show prof bijaksana at right with dissolve
    prof 'Aku tahu, ini bertentangan dengan semua yang kuajarkan tentang Konsensus. Tapi Konsensus yang represif harus dihancurkan.'
    prof 'Tempat terbaik untuk menanamkan ingatan adalah di Gedung Arsip Lama (Basement 3). Kelembapan di sana akan melindungi sinyalmu. Temui Evelyn di Kamar Asrama-mu, itu Base Camp utamamu.'
    hide prof with dissolve

    play music Mission_Blueprint fadeout 1.5
    jump titik_infiltration
    return

label titik_infiltration:
    play music Point_of_No_Return fadein 1.0
    scene bg kamarAsrama with fade

    'Malam tiba. Kamar Asrama Lucien kini menjadi Ruang Kendali utama. Lucien berbaring di kasur, sensor dipasang. Marcus duduk di samping, memegang monitor.'


    show evelyn fokus at right with dissolve
    evelyn 'Target pertama sudah ditentukan: Kepala Dewan Legislatif. Dia yang paling mudah dipengaruhi emosinya.'
    evelyn 'Misi kita adalah mengubah Titik Patah yang membuatnya percaya bahwa UUK adalah ide terbaik.'
    hide evelyn with dissolve

    show lucien monolog at center with dissolve
    lucien 'Berat misi terasa di dadaku.'
    
    hide lucien with dissolve

    # Bunyi kapsul tertelan
    show marcus serius at right with dissolve

    marcus 'Lo jangan hilang, Lucien. Gue butuhin lo di sini.'

    hide marcus with dissolve

    'Begitu kapsul itu bekerja, kesadaran Lucien segera jatuh.' 
    play music Point_of_No_Return fadeout 1.5
    jump nexus
    return


label nexus: 
    play music Nexus_Ambient fadein 1.0
    scene bg ruangHampa with fade 

    show serena bicaraSerius at center with dissolve
    'Lucien tiba di lapisan kesadaran yang lain. Serena Aisley, The Arsitek, menunggunya.'
    hide serena with dissolve

    show serena bicara at right with dissolve
    serena 'Kau datang, Lucien. Nexus adalah jembatan. Di sinilah kau memilih mimpi mana yang akan kau sabotase.'

    serena 'Gerbang itu adalah mimpi para pejabat. Kau hanya bisa memilih satu malam ini. Di dalamnya, ada lima Titik Patah yang akan menentukan lima takdir berbeda untuk realitas Elyndra.'
    hide serena with dissolve
    show serena bicaraSerius at right with dissolve
    serena 'Berhati-hatilah, Konsensus yang kau pecahkan mungkin akan menghancurkanmu.'
    hide serena with dissolve

    show lucien normal at center with dissolve
    'Lucien menatap tiga gerbang, bersiap untuk misi pertamanya.'
    hide lucien with dissolve

    stop music 
    jump chapter_2
    return