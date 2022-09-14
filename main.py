import time
from utils import menugen
from requests_html import HTMLSession
from bs4 import BeautifulSoup as bs
from loguru import logger
import pyppeteer

def fetch_html(playlist_url):
    logger.debug("Creating HTML Session")
    session = HTMLSession()
    # get the html content
    logger.debug("Fetching Content")
    while True:
        try:
            response = session.get(playlist_url)
            # execute Java-script
            response.html.render(sleep=1)
            logger.debug("Executing js")
        except pyppeteer.errors.TimeoutError:
            continue
        else:
            break

    # create bs object to parse HTML
    return bs(response.html.html, "html.parser")


def scrape_html(soup):
    logger.debug("Scraping Data")
    video_tags = soup.find_all("ytd-playlist-video-renderer")
    
    for tag in video_tags:
        with open("hell.txt","a") as f:

            f.write(str(tag)+"\n\n")
    


def main():
    play_list = []
    title = "playlist"
    # selected_playlist, play_list = menugen(play_list, title=title)
    soup = fetch_html("https://www.youtube.com/playlist?list=PLF_7kfnwLFCF8sjVSdxn3yWAghIgVnw26")
    scrape_html(soup)



if __name__ == "__main__":
    main()