import requests
import os
import re


while True:
    music_id = input("请输入歌曲id或歌曲链接: ")
    if music_id.startswith("http"):
        music_id = re.search(r"id=(\d+)", music_id).group(1)
    get_lyric = requests.get(url="https://music.163.com/api/song/lyric", params={"id": music_id, "lv": 1, "kv": 1, "tv": -1}).json()
    if get_lyric.get("lrc").get("lyric") == "":
        print("该歌曲没有歌词")
    else:
        if not os.path.exists("./OutLyric"):
            os.makedirs("./OutLyric")
        with open(f"./OutLyric/{music_id}.lrc", "w", encoding="utf-8") as save_lyric:
            if get_lyric.get("tlyric").get("lyric") == "":
                save_lyric.write(get_lyric.get("lrc").get("lyric"))
            else:
                zh_cn_lyric = re.sub(r'\[[^0-9]*:[^0-9.]*]\n', '', get_lyric.get("tlyric").get("lyric"))
                save_lyric.write(f'{get_lyric.get("lrc").get("lyric")}\n{zh_cn_lyric}')
        print(f"下载成功,可将该文件重命名至与歌曲相同的名字使用,lrc文件保存至./OutLyric/{music_id}.lrc")