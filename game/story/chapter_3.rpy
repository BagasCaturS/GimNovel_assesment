label chapter_3:
    scene bg bg_chapter_3 with fade
    
    ' '

    # BGM: ambient low hum (replace with actual file if available)
    # play music "audio/ambient_low_hum.ogg" loop
    scene bg ruangHampa with fade
    show serena bicaraSerius at right
    show lucien focus at left with dissolve

    serena "Kesadaranmu lebih stabil hari ini."
    serena "Evelyn pasti memaksamu menekan semua emosi."

    show lucien exhausted at left with dissolve
    lucien "Dia selalu begitu."

    serena "Dan kau selalu membencinya."
    hide serena with dissolve
    hide lucien with dissolve
    show lucien cemas at center with dissolve
    "Lucien memandang lantai Nexus yang berfungsi seperti cermin retak."

    show lucien cemas at left with move
    show serena bicaraSerius with dissolve
    serena "Titik Patah pertama."
    hide serena with dissolve
    "Retakan merah muncul."

    show lucien tense at center with move
    lucien "Ada... sesuatu yang masuk?"

    show serena bicaraSerius at right with dissolve
    serena "Bukan sesuatu. Seseorang."
    show lucien focus at center with dissolve
    lucien "...Marcus?"
    hide lucien with dissolve
    show serena bicaraSerius at center with dissolve
    "Serena membuka retakan sepenuhnya."

    # BGM fades and is replaced by a different ambience for the campus (replace with file)
    # stop music fadeout 1.0
    # play music "audio/empty_city_ambience.ogg" loop

    scene bg jalananKampus with fade
    hide serena
    show serena bicaraSerius at right with dissolve
    show lucien focus at center with dissolve

    "Tiba-tiba Lucien berada di jalan kampus yang sepi."
    show lucien realization at center with dissolve
    lucien "Ini kampus... Studio desain harusnya ada di sana..."
    show lucien focus at center with dissolve
    serena "Tempat ini sedang ditimpa memori lain."
    show serena bicara at right with dissolve
    "Dari kejauhan terdengar langkah berat dan gema."
    show serena bicaraSerius at right with dissolve

    show lucien tense at center with dissolve
    lucien "Apa itu?"

    serena "Serpihan ingatan Anchor-mu. Dia mencoba mendapatakan pijakan."
    hide serena with dissolve
    show lucien suprise at center with dissolve
    lucien "Marcus?! Kalau dia masuk tanpa pelindung—"
    
    show serena bicaraSerius at right with dissolve
    serena "—dia akan kehilangan lebih banyak ingatannya."

    hide serena with dissolve
    show lucien focus at center with dissolve
    show lucien focus at center with hpunch
    lucien "Sialan!"
    
    serena "Fokus, Lucien."
    show serena bicaraSerius at right with dissolve
    serena "Ada jalur di bawah struktur ini. Memori masa kecil Anchor-mu."

    show lucien focus at center with dissolve
    lucien "Aku harus menjemputnya."

    show serena SadSmile at right with dissolve
    serena "Rencana Evelyn akan rusak. Rencana Profesor juga."
    show lucien monolog at center with dissolve
    lucien "Marcus adalah alasan aku masih bisa kembali. Tanpa dia… aku tenggelam."
    hide lucien with dissolve

    show serena softSmile at center with move
    " "
    hide serena

    "Retakan baru berbentuk lingkaran muncul. Dengan warna yang hitam pekat."


    "Dan terdengan suara samar"

    "…Luc… lo jangan hilang…"
    show lucien suprise at center with dissolve
    lucien "Aku datang."

    "Ia melangkah masuk."

    "Gelap menutup ruang Nexus dan menariknya ke dalam memori kelam yang bukan miliknya sendiri."

    scene bg kamarAsrama with fade

    "sementara itu di dunia nyata…"


    show evelyn screaming at center with dissolve
    evelyn "Sinyalnya berubah!"

    "Prof. Rowan berdiri perlahan."
    show prof normal at right with dissolve
    prof "Kita biarkan."

    show evelyn frantic at center with dissolve
    evelyn "Biarkan?! Pola gelombang seperti ini—"
    show prof bicara at right with dissolve
    prof "—seperti ada yang menulis ulang protokol mimpi kita."

    evelyn "Siapa yang bisa melakukan itu?"
    show prof severe at right with dissolve
    prof "Bukan siapa, Evelyn... tetapi apa."

    hide evelyn with dissolve
    hide prof with dissolve 

    jump chapter_4
    return