import sys
import time
import urllib.request
import urllib.error

def main(url):
    request = urllib.request.Request(url, method="HEAD")
    while True:
        print(f"ping {url}...", end="")
        try:
            response = urllib.request.urlopen(request, timeout=30)
        except urllib.error.HTTPError as e:
            print(f" HTTP error '{e.code}'")
        except urllib.error.URLError:
            print(" URL error")
        else:
            response.close()
            print(f" {response.status}")
            if response.status == 200:
                break
        time.sleep(2)

if __name__ == "__main__":
    main(sys.argv[1])