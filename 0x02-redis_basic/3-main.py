#!/usr/bin/env python3

from web import get_page
import time

def test_get_page_caching():
    # Test the caching behavior with a slow URL
    url = "http://slowwly.robertomurray.co.uk/delay/1000/url/https://www.example.com"

    # Fetch the page for the first time (should take around 1 second)
    start_time = time.time()
    page_content = get_page(url)
    end_time = time.time()
    print(f"First fetch took {end_time - start_time:.2f} seconds")
    print(f"Page content:\n{page_content}\n")

    # Fetch the page again immediately (should be cached, so it should be much faster)
    start_time = time.time()
    page_content_cached = get_page(url)
    end_time = time.time()
    print(f"Second fetch took {end_time - start_time:.2f} seconds")
    print(f"Page content (cached):\n{page_content_cached}\n")

    # Wait for 10 seconds to test cache expiration
    print("Waiting for cache expiration...")
    time.sleep(10)

    # Fetch the page after 10 seconds (should take around 1 second again)
    start_time = time.time()
    page_content_expired = get_page(url)
    end_time = time.time()
    print(f"Third fetch took {end_time - start_time:.2f} seconds")
    print(f"Page content (after cache expiration):\n{page_content_expired}\n")

if __name__ == "__main__":
    test_get_page_caching()