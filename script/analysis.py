# coding: utf-8


__author__ = 'tuomao'

import torndb
from model import dbsetting
from model import db_tool
import os

# dbtool = db_tool.DbTool(torndb.Connection(**dbsetting.DATABASE['mysql']))

RESOURCE_PATH = "C:\\Users\\tuomao\\workspace\\AndroidCloneDection\\resource"
ANALYSIS_JAR_PATH="C:\\Users\\tuomao\Desktop\\test\\analysis.jar"

def get_un_analysis_application(dir):
    files = []
    for fpathe, dirs, fs in os.walk(dir):
        for f in fs:
            mfile = os.path.join(fpathe, f)
            if mfile.endswith(".apk"):
                files.append(mfile)
    print (files)
    return files

def run_command(command):
    result = os.popen(command)
    print(result.read())
# get_un_analysis_application("C:\\Users\\tuomao\\Desktop\\node")

apk_path="K:\\workspace\\android\CloneAnalysis\\app\\app-release.apk"
comand ="java -jar -Xmx5G %s %s %s" %(ANALYSIS_JAR_PATH,apk_path,RESOURCE_PATH)
run_command(comand)