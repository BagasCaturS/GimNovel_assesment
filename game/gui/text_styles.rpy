# game/gui/text_styles.rpy

# Style untuk tombol menu utama
style main_menu_button:
    # Mengatur latar belakang tombol agar transparan
    background None
    # Mengatur padding di sekitar teks tombol (opsional, bisa disesuaikan)
    xpadding 20
    ypadding 10

# Style untuk teks di dalam tombol menu utama
style main_menu_button_text:
    # Mengatur font (pastikan font ini ada di folder 'game/fonts/')
    # Jika tidak ada, Ren'Py akan menggunakan font default.
    # Contoh: font "fonts/OpenSans-Regular.ttf"
    font "gui/font.ttf" # Ren'Py default GUI font

    # Mengatur ukuran teks
    size 40
    
    # Warna teks normal (putih)
    color "#FFFFFF"         
    
    # Warna teks saat di-hover (merah seperti di screenshot Anda)
    hover_color "#FF0000"  

    # Mengatur efek shadow untuk teks agar lebih terbaca (opsional)
    # xoffset dan yoffset adalah posisi shadow
    # outline_color adalah warna shadow
    # outline_delta adalah ketebalan shadow (semakin besar semakin tebal)
    # outline_alpha adalah transparansi shadow (0 = transparan, 1 = solid)
    outlines [ (1, "#000000", 0, 0, 0.5) ]