import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

TOKEN = '6571237246:AAHWPvjZO8lNEKG7jS-ZB-InQ8nMEtlJssE'

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

user_data = {}

MENU_MAIN = 0
MENU_SUBMENU_1 = 1
MENU_SUBMENU_2 = 2
MENU_SUBMENU_3 = 3
MENU_SUBMENU_4 = 4
MENU_SUBMENU_5 = 5
MENU_SUBMENU_6 = 6
MENU_SUBMENU_7 = 7
MENU_SUBMENU_8 = 8
MENU_SUBMENU_9 = 9
MENU_SUBMENU_10 = 10

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    menu_text = (
        f"Selamat datang di Portal Akademik CEP-CCIT FTUI.\nPilih salah satu menu (masukkan nomor saja):\n"
        "1. Jadwal Pembelajaran Tahap 1 Semester Gasal TA 2023/2024\n"
        "2. Kalender Akademik Semester Gasal TA 2023/2024\n"
        "3. Alokasi Kelas Semester Gasal TA 2023/2024 (Updated 26/09/2023)\n"
        "4. Informasi Kuliah Umum & WORKSHOP: Daftar Wajib Resume & Sertifikat Kuliah Umum\n"
        "5. Layanan Pengaduan Kritik/Saran/Keluhan\n"
        "6. Pengajuan Surat Keterangan Aktif/Lulus/Magang\n"
        "7. Program Magang CEP-CCIT FTUI\n"
        "8. Pengumuman Akademik Terbaru Website CCIT FTUI\n"
        "9. Peraturan Akademik dan Formulir Presentasi\n"
        "10. Panduan Akses CCIS Student dengan Anydesk\n"
        "11. Exit"
    )
    await update.message.reply_text(menu_text)

    context.user_data['menu_state'] = MENU_MAIN

async def submenu_1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    menu_text = (
        f"Jadwal Pembelajaran Tahap 1 Semester Gasal TA 2023/2024\n"
        "http://ccit.eng.ui.ac.id/wp-content/uploads/2023/09/Jadwal-Pembelajaran-Tahap-1-Semester-Gasal-TA-2023-2024-All-Program-15092023.pdf"
        "\n0. Kembali ke menu utama"
    )
    await update.message.reply_text(menu_text)

    context.user_data['menu_state'] = MENU_SUBMENU_1

async def submenu_2(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    menu_text = (
        f"Kalender Akademik Semester Gasal TA 2023/2024\n"
        "http://ccit.eng.ui.ac.id/wp-content/uploads/2023/09/Surat-Keputusan-Direktur-Tentang-Kalender-Smt-Gasal-TA-2023-2024.pdf"
        "\n0. Kembali ke menu utama"
    )
    await update.message.reply_text(menu_text)
    context.user_data['menu_state'] = MENU_SUBMENU_2

async def submenu_3(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    menu_text = (
        f"Alokasi Kelas Semester Gasal TA 2023/2024 (Updated 26/09/2023)\n"
        "http://ccit.eng.ui.ac.id/wp-content/uploads/2023/09/Kelas-Aktif-Semester-Gasal-TA-2023-2024-25092023.pdf"
        "\n0. Kembali ke menu utama"
    )
    await update.message.reply_text(menu_text)
    context.user_data['menu_state'] = MENU_SUBMENU_3

async def submenu_4(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    menu_text = (
        f"Informasi Kuliah Umum & WORKSHOP: Daftar Wajib Resume & Sertifikat Kuliah Umum\n"
        "https://bit.ly/CCIT_SertifikatKU"
        "\n0. Kembali ke menu utama"
    )
    await update.message.reply_text(menu_text)
    context.user_data['menu_state'] = MENU_SUBMENU_4

async def submenu_5(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    menu_text = (
        f"Layanan Pengaduan Kritik/Saran/Keluhan\n"
        "https://docs.google.com/forms/d/e/1FAIpQLScUZIJASHr76nZBxbNyKFh5bBwgqkyvJ5WbDgW-bEisS1Ea1A/viewform"
        "\n0. Kembali ke menu utama"
    )
    await update.message.reply_text(menu_text)
    context.user_data['menu_state'] = MENU_SUBMENU_5

async def submenu_6(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    menu_text = (
        f"Pengajuan Surat Keterangan Aktif/Lulus/Magang\n"
        "https://bit.ly/PengajuanSuratSiswaCCITFTUI"
        "\n0. Kembali ke menu utama"
    )
    await update.message.reply_text(menu_text)
    context.user_data['menu_state'] = MENU_SUBMENU_6

async def submenu_7(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    menu_text = (
        f"Program Magang CEP-CCIT FTUI\n"
        "https://bit.ly/CCIT_programmagang"
        "\n0. Kembali ke menu utama"
    )
    await update.message.reply_text(menu_text)
    context.user_data['menu_state'] = MENU_SUBMENU_7

async def submenu_8(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    menu_text = (
        f"Pengumuman Akademik Terbaru Website CCIT FTUI\n"
        "https://ccit.eng.ui.ac.id/category/pengumuman-untuk-siswa/"
        "\n0. Kembali ke menu utama"
    )
    await update.message.reply_text(menu_text)
    context.user_data['menu_state'] = MENU_SUBMENU_8

async def submenu_9(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    menu_text = (
        f"Peraturan Akademik dan Formulir Presentasi\n"
        "https://ccit.eng.ui.ac.id/resources/"
        "\n0. Kembali ke menu utama"
    )
    await update.message.reply_text(menu_text)
    context.user_data['menu_state'] = MENU_SUBMENU_9

async def submenu_10(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    menu_text = (
        f"Panduan Akses CCIS Student dengan Anydesk\n"
        "https://drive.google.com/file/d/1Plv4Rd4ytP6OSV28wwGMrHN6Dro-H-sQ/view?usp=sharing"
        "\n0. Kembali ke menu utama"
    )
    await update.message.reply_text(menu_text)
    context.user_data['menu_state'] = MENU_SUBMENU_10

async def handle_text_input(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    menu_state = context.user_data.get('menu_state', MENU_MAIN)

    if text == '0' and menu_state != MENU_MAIN:
        await start(update, context)
    elif text == '1' and menu_state == MENU_MAIN:
        await submenu_1(update, context)
    elif text == '2' and menu_state == MENU_MAIN:
        await submenu_2(update, context)
    elif text == '3' and menu_state == MENU_MAIN:
        await submenu_3(update, context)
    elif text == '4' and menu_state == MENU_MAIN:
        await submenu_4(update, context)
    elif text == '5' and menu_state == MENU_MAIN:
        await submenu_5(update, context)
    elif text == '6' and menu_state == MENU_MAIN:
        await submenu_6(update, context)
    elif text == '7' and menu_state == MENU_MAIN:
        await submenu_7(update, context)
    elif text == '8' and menu_state == MENU_MAIN:
        await submenu_8(update, context)
    elif text == '9' and menu_state == MENU_MAIN:
        await submenu_9(update, context)
    elif text == '10' and menu_state == MENU_MAIN:
        await submenu_10(update, context)
    elif text == '11' and menu_state == MENU_MAIN:
        await update.message.reply_text("Terima kasih")
    else:
        await update.message.reply_text("Silahkan masukkan nomor yang benar")

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    check_input_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text_input)
    application.add_handler(check_input_handler)

    application.run_polling()
