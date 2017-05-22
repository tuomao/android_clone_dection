# coding: utf-8
import sys
import torndb

__author__ = 'tuomao'

NONE_LIST_RETURN = []
NONE_DICT_RETURN = {}


class DbTool(object):
    def __init__(self, con):
        self.db = con

    def track_file(self, files):
        sql = "insert into files(path) VALUES('%s')"
        records = []
        for file in files:
            record = [file]
            records.append(record)
        self.db.insertmany(sql, records)

