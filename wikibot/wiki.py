import aiohttp
import html
import re


async def get_wikipedia_info(search_query):
    url = "https://uz.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "list": "search",
        "srsearch": search_query,
        "format": "json",
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as response:
            data = await response.json()
            return data


def clean_html(raw_html):
    clean_text = html.unescape(raw_html)  # HTML entitetslarini oddiy matnga aylantirish
    clean_text = re.sub(r"<.*?>", "", clean_text)  # HTML teglarini olib tashlash
    return clean_text


# Misol uchun:
# asyncio.run(get_wikipedia_info("Python programming language"))
