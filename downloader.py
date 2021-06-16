import os
import requests
import time

def human_readable_size(size, decimal_places=2):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB', 'PB']:
        if size < 1024.0 or unit == 'PB':
            break
        size /= 1024.0
    return f"{size:.{decimal_places}f} {unit}"



async def DownLoadFile(url, chunk_size, reply, file_name="file.mkv"):
    if os.path.exists(file_name):
        os.remove(file_name)
    if not url:
        return file_name

    r = requests.get(url, allow_redirects=True, stream=True)
    total_size = int(r.headers.get("content-length", 0))
    downloaded_size = 0
    current = ""
    count = 0
    with open(file_name, 'wb') as fd:
        for chunk in r.iter_content(chunk_size=chunk_size):
            if chunk:
                fd.write(chunk)
                downloaded_size += chunk_size
                count = count+1
                if count % 100 == 0:
                    string = f"{human_readable_size(downloaded_size)}/{human_readable_size(total_size)}"
                    time.sleep(0.3)
                    if current != string:
                        await reply.edit(string)
                        current = string

    await reply.edit("Uploading holdup")
    return file_name

# DownLoadFile("https://s-delivery11.mxdcontent.net/d/wneqkj7vujlgqx/dxbbk2p8njgl2mda2l5wsfkod7vhz62?ab=0&r=https%3A%2F%2Fmixdrop.co%2Ff%2Fwneqkj7vujlgqx", "hi.mkv", 1024*10)