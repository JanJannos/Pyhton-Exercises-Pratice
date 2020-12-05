import webbrowser as wb


def webauto():
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    URLS = (
        'https://stackoverflow.com/',
        'gmail.com',
        'google.com',
        'youtube.com'
    )

    for url in URLS:
        print('Opening URL ' + url)
        wb.get(chrome_path).open(url)


webauto()