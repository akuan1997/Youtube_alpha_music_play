# YouTube Alpha Music Player

The **YouTube Alpha Music Player** is a tool designed to enhance your experience with the YouTube channel [알파 (@alpha_music)](https://www.youtube.com/@alpha_music), which regularly releases the latest Korean rap tracks. While YouTube’s “Play All” feature allows you to play music continuously, it often becomes repetitive, cycling through 10-15 songs, making it inconvenient for those who wish to discover new music. Additionally, users often have to manually skip songs they dislike, which can be cumbersome.

This repository aims to solve these issues by offering the following features:

Therefore, this repository mainly improves these problems, the following are the functions of this repository
* If your youtube account is not premium, it will automatically click to skip the advertisement at the end of the video countdown
* The program will play from the first song to the last song
* After entering the movie page, check whether the dislike button is pressed. If available, it will record this song in the local file and play the next song
* If you press the dislike button during video playback, it will record the song in the local file and play the next song
* The program will open local files and skip videos that have been recorded as you don't like
* Record the songs you liked in the txt file

- **Auto Ad Skipping**: If you don’t have a YouTube Premium account, the program will automatically skip ads once the countdown ends.
- **Sequential Playback**: It plays songs sequentially, from the first to the last in the playlist.
- **Dislike Detection**: Upon entering a video page, the program checks if the dislike button has been pressed. If so, it records the song in a local file and skips to the next song.
- **Real-Time Dislike Recording**: If you press the dislike button during playback, the program records the song in the local file and moves to the next song.
- **Skip Disliked Songs**: The program reads the local file of disliked songs and skips any that have been previously recorded as disliked.
- **Like Recording**: It keeps track of liked songs in a separate text file.

## Precautions

- **Account Login**: Before running the program, update the account credentials to your YouTube account's username and password. You will find the relevant instructions in the code comments.

## How to Use

1. Clone this repository to your local machine.
2. Modify the script to include your YouTube account credentials.
3. Run the program to start exploring new music on the **알파 (@alpha_music)** channel with improved playback control.

Feel free to contribute and suggest improvements!
