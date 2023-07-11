from playwright.sync_api import sync_playwright, Playwright
from playwright.sync_api import expect, Page

# fill your account information
userID = ''
password = ''

with sync_playwright() as p:
    browser = p.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.set_default_timeout(10000)

    ''' Log in '''
    while True:
        try:
            page.goto('https://www.youtube.com/@alpha_music/videos')
            page.wait_for_timeout(1500)
            page.locator('#buttons > ytd-button-renderer > yt-button-shape > a > yt-touch-feedback-shape > div > '
                         'div.yt-spec-touch-feedback-shape__fill').click()
            page.wait_for_timeout(1500)
            page.locator('#identifierId').fill(userID)
            page.wait_for_timeout(1500)
            page.locator('#identifierNext > div > button > span').click()
            page.wait_for_timeout(1500)
            page.locator('#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input').fill(password)
            page.wait_for_timeout(1500)
            page.locator('#passwordNext > div > button > span').click()
            page.wait_for_timeout(3000)
            break
        except:
            continue

    ''' Start listening '''
    index = 0
    index -= 1
    while True:
        index += 1
        print('index', index)
        current_sec = -1
        time_duration_sec = -1
        ''' Get title  '''
        while True:
            try:
                while not page.locator('#video-title').nth(index).is_visible():
                    page.keyboard.press("End")
                    page.wait_for_timeout(1500)
                current_title = page.locator('#video-title').nth(index).inner_text()
                break
            except Exception as e:
                print('error 1')
                continue

        ''' Make sure that the video is clickable '''
        while True:
            try:
                while not page.locator('#dismissible > ytd-thumbnail').nth(index).is_visible():
                    page.keyboard.press("End")
                    page.wait_for_timeout(1500)
                break
            except Exception as e:
                print('error 2')
                page.goto('https://www.youtube.com/@alpha_music/videos')
                continue

        ''' Skip videos if dislike '''
        skip = False
        with open('youtube_dislikes.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
        for line in lines:
            line = line.replace('\n', '')
            if current_title in line or line in current_title:
                skip = True
        if skip:
            print('txt, skip')
            print()
            continue

        ''' Enter video page '''
        while True:
            try:
                print('Playing', current_title)
                print()
                page.wait_for_timeout(1500)
                videos = page.query_selector_all('#dismissible > ytd-thumbnail')
                videos[index].click()
                break
            except Exception as e:
                print('Error 3')
                page.goto('https://www.youtube.com/@alpha_music/videos')
                page.wait_for_timeout(1500)
                while not page.locator('#dismissible > ytd-thumbnail').nth(index).is_visible():
                    page.keyboard.press("End")
                    page.wait_for_timeout(1500)
                continue

        ''' Check dislike button '''
        while not page.locator('#segmented-dislike-button > ytd-toggle-button-renderer > yt-button-shape > button').nth(
                0).is_visible():
            pass
        buttons = page.query_selector_all('#segmented-dislike-button > ytd-toggle-button-renderer > yt-button-shape > '
                                          'button')
        page.wait_for_timeout(1500)
        aria_pressed = buttons[0].get_attribute("aria-pressed")
        ''' Dislike, but not in txt file '''
        if aria_pressed == 'true':
            duplicate = False
            for line in lines:
                line = line.replace('\n', '')
                if page.locator('#title > h1 > yt-formatted-string').inner_text() in line or line in page.locator(
                        '#title > h1 > yt-formatted-string').inner_text():
                    duplicate = True
                    break

            if not duplicate:
                print("I don't like this song, but not in txt yet")
                print('writing', current_title)
                with open('youtube_dislikes.txt', 'a', encoding='utf-8') as f:
                    f.writelines(current_title + '\n')
                print('writing', page.locator('#title > h1 > yt-formatted-string').inner_text())
                with open('youtube_dislikes.txt', 'a', encoding='utf-8') as f:
                    f.writelines(page.locator('#title > h1 > yt-formatted-string').inner_text() + '\n')
                print()
            else:
                print('strange')

            page.goto('https://www.youtube.com/@alpha_music/videos')
            page.wait_for_timeout(1500)
            videos = page.query_selector_all('#dismissible > ytd-thumbnail')
            continue

        ''' if ads '''
        if page.locator('.ytp-ad-player-overlay-skip-or-preview').is_visible():
            print('ad')
            while not page.locator('.ytp-ad-skip-button-container').is_visible():
                pass
            page.locator('.ytp-ad-skip-button-container').click()

        ''' Get time length '''
        while not page.locator('#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > '
                               'div.ytp-left-controls > div.ytp-time-display.notranslate > span:nth-child('
                               '2) > span.ytp-time-duration').is_visible():
            print('waiting')
            pass
        time_duration = page.locator('#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > '
                                     'div.ytp-left-controls > div.ytp-time-display.notranslate > span:nth-child('
                                     '2) >'
                                     'span.ytp-time-duration').inner_text()
        time_duration_sec = int(time_duration.split(':')[0]) * 60 + int(time_duration.split(':')[1])

        ''' Stay, until press dislike button '''
        # Remember, current_time only update when showing
        # No process bar, current_time no update
        # When finish playing, process bar automatically pops out
        # subtract < 5, becomes true, pops out of the while loop
        while time_duration_sec - current_sec >= 5 and page.locator(
                '#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > '
                'div.ytp-left-controls > div.ytp-time-display.notranslate > span:nth-child(2) >'
                'span.ytp-time-current').is_visible():
            ''' 持續更新current time '''
            current_time = page.locator('#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > '
                                        'div.ytp-left-controls > div.ytp-time-display.notranslate > span:nth-child(2) >'
                                        'span.ytp-time-current').inner_text()
            current_sec = int(current_time.split(':')[0]) * 60 + int(current_time.split(':')[1])
            time_duration = page.locator('#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > '
                                         'div.ytp-left-controls > div.ytp-time-display.notranslate > span:nth-child('
                                         '2) >'
                                         'span.ytp-time-duration').inner_text()
            time_duration_sec = int(time_duration.split(':')[0]) * 60 + int(time_duration.split(':')[1])

            ''' Keep checking dislike button '''
            buttons = page.query_selector_all(
                '#segmented-dislike-button > ytd-toggle-button-renderer > yt-button-shape > '
                'button')
            page.wait_for_timeout(1500)
            aria_pressed = buttons[0].get_attribute("aria-pressed")
            if aria_pressed == 'true':
                print('pressed dislike button')
                print('writing', current_title)
                with open('youtube_dislikes.txt', 'a', encoding='utf-8') as f:
                    f.writelines(current_title + '\n')
                print('writing', page.locator('#title > h1 > yt-formatted-string').inner_text())
                with open('youtube_dislikes.txt', 'a', encoding='utf-8') as f:
                    f.writelines(page.locator('#title > h1 > yt-formatted-string').inner_text() + '\n')
                print()
                break

        ''' Finish the video, back to the main page '''
        page.goto('https://www.youtube.com/@alpha_music/videos')
        page.wait_for_timeout(1500)
