import telebot
import time
from GIF import GIF

bot = telebot.TeleBot('2125057771:AAHzoKqLjbtho2kQuxy8evJV07q4dvkB3Eg')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    gif = GIF()
    if message.text[:4] == "http" and len(message.text) > 10:
        try:
            split_space = str(message.text).split(' ')
            filename, cut_frames, color = gif.downloadVideo(split_space)
            gif.createGIF(split_space, filename, cut_frames, color)

            with open(gif.path + filename + '.gif', 'rb') as f1:
                bot.send_animation(message.from_user.id, f1)

            time.sleep(2)
            gif.remove(filename)
        except UnicodeError:
            bot.send_message(message.from_user.id, "Invalid input")
            try:
                gif.remove(filename)
            except Exception:
                pass
    else:
        bot.send_message(message.from_user.id, 
                         I can only create GIFs, so give me a link and 2 timestamps in the format 
                         ‘link mm:ss mm:ss.’ You can also add 2 additional values:
                         frame division and color.

Frame division: 1 (default) means full frames, 2 takes half of the frames from the stream, 
3 takes a third, and so on.
Color: 1 (default) or 2 (gray). 
The higher the frame division, the worse the visual perception of the image,
as it will appear jerky. It’s recommended to use this on longer time intervals so that
Telegram can handle larger GIF sizes. 
For example, a 1-second GIF with full frames weighs 2.5 MB, 
so Telegram won’t accept GIFs longer than approximately 20 seconds,
and processing will take longer.)

bot.polling(none_stop=True, interval=0)
