# coding: utf-8
import os

ANDROGUARD_PATH = "/home/tuomao/workspace/androguard-2.0"
WHILTE_LIST_PATH = "/home/tuomao/Desktop/android_clone_dection/resource/whitelist"

exclude_list=""

def compute_apk_similarity(apk1, apk2):
    os.chdir(ANDROGUARD_PATH)
    result = os.popen("./androsim.py -i %s %s -n -e %s -t 0.8 -s 10" % (apk1, apk2,exclude_list))
    print(result.read())


# compute_apk_similarity("/home/tuomao/Desktop/malware/com.meilishuo_95.apk","/home/tuomao/Desktop/malware/绝色视频_041805.apk")


def gen_exclude_list():
    whitelist = open(WHILTE_LIST_PATH)
    str = ""
    for line in whitelist.readlines():
        line = line.replace(".", "/").strip("\n")
        str = str + "(L" + line + ")|"
    if len(str) > 0:
        str = str[0:(len(str) - 1)]
    print(str)
    exclude_list=str


def __main():
    gen_exclude_list()
    compute_apk_similarity("/data/confuse_apk/orgin/com.douban.daily_181.apk","/data/confuse_apk/nontrivialjunk/com.douban.daily_181.apk")
    # compute_apk_similarity('/data/confuse_apk/orgin/com.douban.daily_181.apk','/data/confuse_apk/orgin/com.douban.daily_181.apk')
__main()
