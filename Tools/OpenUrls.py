#! /usr/bin/env python
import clipboard
import validators
import webbrowser

def read_urls_from_clipboard():
    urls = []
    for raw_url in clipboard.paste().split('\n'):
        raw_url = raw_url.replace(' ', '')
        raw_url = raw_url.replace('\r', '')

        if validators.url(raw_url):
            urls.append(raw_url)

    return urls
    
if __name__ == "__main__":
    for url in read_urls_from_clipboard():
        print('Opening:', url if len(url) < 80 else url[80] + '...')
        webbrowser.open(url)