# Persist-venture-Assignment
CI
main - Build Status
develop - Build Status

YouTube Gif Bot is a bot that sends a gif to the Telegram chat, following a link from YouTube and two timestamps in the 'link mm:ss mm:ss' format.

Usage:
Find YoutubeGifBot in Telegram;

Run the script using Docker or just some IDE;

Some optional parameters:
Decrease FPS - 4 input parameter. By default, YouTube has 30 FPS, and with this function you can reduce their number many times (reducing frames by 2 times doesn't really catch the eye, so it can be used).

Docker:
docker build -t ygb .
docker run ygb
The bot is running - you can write to it.


Problems and Recommendations
It would be great not to download the full video from YouTube, and FFMPEG can somehow help with this, but I didn't go into details;
Since in my implementation the video is downloaded completely, therefore, I think you understand that you shouldn't give the bot some 10-hour video input;
You shouldn't give timestamps with a difference of more than 15 seconds, since Telegram may not accept such a GIF.





