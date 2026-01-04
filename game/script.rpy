
label start:
    scene bg blank
    scene bg splashScreen with fade
    menu intro:
        "Mau dimulai dari mana ceritanya?"
        "Chapter one":
            jump chapter_1
        "Chapter two":
            jump chapter_2
        "Chapter three":
            jump chapter_3
        "Chapter four":
            jump chapter_4
        "Chapter five":
            jump chapter_5
    return


label startHere: 
    scene bg bg_chapter_1 with fade

    'Sebuah pemerintahan yang kuat di kota Elyndra baru saja mengesahkan "Undang-Undang Konsensus (UUK)" yang sangat represif, membatasi kebebasan berekspresi. Lucien Vale memiliki kemampuan unik untuk memasuki hingga memanipulasi alam bawah sadar “Dream Infiltration”.' 
    
    'Bersama tim kecilnya, ia berencana menjatuhkan UUK dengan mengubah ingatan krusial di dalam mimpi para pejabat tinggi. Keberhasilan atau kegagalan misi ini akan menentukan salah satu dari lima takdir berbeda yang akan mengubah realitas Elyndra.'

    jump chapter_1
    
    return