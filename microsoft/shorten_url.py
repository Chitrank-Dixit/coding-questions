"""
Implement a URL shortener with the following methods:

shorten(url), which shortens the url into a six-character alphanumeric string, such as zLg6wl.
restore(short), which expands the shortened string into the original url. If no such shortened string exists, return null.
Hint: What if we enter the same URL twice?


"""
import random
import string

lookup = {}
processed = {}


def shorten_url(url):
    if url not in processed:
        short_url = "".join(
            random.choices(
                string.ascii_uppercase
                + string.ascii_lowercase
                + string.digits,
                k=6,
            )
        )
        processed[url] = short_url
        lookup[short_url] = url
        return short_url
    return processed[url]


def original_url(shorten_url):
    if shorten_url in lookup:
        return lookup[shorten_url]
    return None


if __name__ == "__main__":
    url = "google.com"
    short_url = shorten_url(url=url)
    print(short_url)
    print(original_url(shorten_url=short_url))

    url = "microsoft.com"
    short_url = shorten_url(url=url)
    print(short_url)
    print(original_url(shorten_url=short_url))
