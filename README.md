# YouTube Video Auto-Liker/Disliker

This script automates interactions on YouTube using Playwright. It allows users to automatically log in, browse videos on a specified channel, like or dislike videos based on user preferences, and record these actions in local text files.

## Features

- **Auto Login**: Automatically logs into YouTube using provided user credentials.
- **Video Browsing**: Automatically browses through all videos on a specified channel and processes them according to predefined rules.
- **Auto Like/Dislike**: If a video is liked or disliked by the user but not recorded in the local file, the script will add it to the respective file.
- **Skip Disliked Videos**: Skips videos if the title is listed in the `youtube_dislikes.txt` file.
- **Ad Skipping**: Automatically skips ads during video playback.

## Requirements

- Python 3.x
- Playwright

## Installation

1. Install Playwright:

   ```bash
   pip install playwright
   ```

2. Initialize Playwright:

   ```bash
   playwright install
   ```

## Usage

1. Modify the `userID` and `password` variables in the script with your YouTube login credentials.

2. Run the script using the following command:

   ```bash
   python script.py
   ```

3. The script will perform the following tasks:
   - Navigate to the specified YouTube channel page.
   - Browse and process each video.
   - Record any liked or disliked videos in the `youtube_likes.txt` or `youtube_dislikes.txt` files.
   - Return to the channel page after finishing each video and proceed to the next one.

## Files

- `script.py`: The main script file containing all the automation logic.
- `youtube_likes.txt`: Records the titles of videos that the user has liked.
- `youtube_dislikes.txt`: Records the titles of videos that the user has disliked.

## Important Notes

- Before running the script for the first time, ensure that the `youtube_likes.txt` and `youtube_dislikes.txt` files are present in the same directory as the script. If not, create these files manually.
- Do not share your YouTube credentials with others to maintain account security.

## License

This script is intended for learning and personal use only. Please do not use it for commercial purposes or in ways that violate YouTube's terms of service.
