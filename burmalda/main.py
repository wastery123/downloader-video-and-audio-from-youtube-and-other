import os
import yt_dlp
import imageio_ffmpeg

def download_media(url, mode):
    base_folder = "downloads"
    ffmpeg_path = imageio_ffmpeg.get_ffmpeg_exe()

    # Настройки стабильности и сети
    ydl_opts = {
        'ffmpeg_location': ffmpeg_path,
        'outtmpl': os.path.join(base_folder, '%(playlist_title)s', '%(playlist_index)s - %(title)s.%(ext)s'),
        
        'ignoreerrors': True,
        'socket_timeout': 60,
        'retries': 10,
        'fragment_retries': 10,
    }

    if mode == "1":
        print("\n[Режим: Только Аудио (MP3)]")
        ydl_opts.update({
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        })
    elif mode == "2":
        print("\n[Режим: Видео со звуком (MP4)]")
        ydl_opts.update({
            'format': 'bestvideo+bestaudio/best',
            'merge_output_format': 'mp4',
        })
    else:
        print("Неверный режим работы!")
        return

    print(f"\nНачинается загрузка. Сейчас сеть защищена от сбоев...")
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("\nПроцесс завершен! Проверьте папку downloads.")
    except Exception as e:
        print(f"\nКритическая ошибка: {e}")

if __name__ == "__main__":
    print("=== УНИВЕРСАЛЬНЫЙ СКАЧИВАТЕЛЬ (ОДИНОЧНЫЕ И ПЛЕЙЛИСТЫ) ===")
    video_url = input("Введите URL (видео, аудио или плейлист): ").strip()
    
    if video_url:
        print("\nЧто вы хотите скачать?")
        print("1 — Только звук (MP3)")
        print("2 — Полное видео (MP4)")
        user_choice = input("Выберите вариант (1 или 2): ").strip()
        
        download_media(video_url, user_choice)
    else:
        print("Вы не ввели URL. Пожалуйста, попробуйте снова.")
