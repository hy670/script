# -*- coding:utf8 -*-
import sys


class Table:
    def __init__(self, username, tablename, rows):
        self.username = username
        self.tablename = tablename
        self.rows = rows


def parse_source_log(pwd="netbank_zl.log"):
    try:
        f = open(pwd, 'r')
    except Exception as exc:
        print("文件打开失败：" + str(exc))
        exit()
    log = []
    for line in f.readlines():
        if line.startswith(". ."):
            linesplite = line.strip().split(" ")
            while "" in linesplite:
                linesplite.remove("")
            while "." in linesplite:
                linesplite.remove(".")
            username = linesplite[1].split("\"")[1]
            tablename = linesplite[1].split("\"")[3]
            rows = linesplite[4]
            log.append(Table(username=username, tablename=tablename, rows=rows))
    return log


def compare_log(export_logs, import_logs):
    print('{:^10}{:^30}{:^20}{:^20}{:^20}'.format("用户名", "表名", "导出条数", "导入条数", "是否一致"))
    tempexportlogs = export_logs[:]
    match_num = 0
    unmath_num = 0
    for exportlog in export_logs:
        for importlog in import_logs:
            if exportlog.username == exportlog.username and exportlog.tablename == importlog.tablename:
                if exportlog.rows == importlog.rows:
                    print(
                        '{:^10}{:^30}{:^20}{:^20}{:^20}'.format(exportlog.username, exportlog.tablename, exportlog.rows,
                                                                importlog.rows, "Y"))
                    match_num = match_num + 1
                elif exportlog.rows != importlog.rows:
                    print(
                        '{:^10}{:^30}{:^20}{:^20}{:^20}'.format(exportlog.username, exportlog.tablename, exportlog.rows,
                                                                importlog.rows, "N"))
                    unmath_num = unmath_num + 1
                tempexportlogs.remove(exportlog)

    print("导出表：" + str(len(exportlogs)) + " 导入表：" + str(len(importlogs)) + " 匹配：" + str(match_num) + " 不匹配：" + str(
        unmath_num))

    if len(tempexportlogs) != 0:
        print("导出日志中表在导入日志中未找到：")
        for exportlog in tempexportlogs:
            print(exportlog.username + "  " + exportlog.tablename + "  " + exportlog.rows)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("使用方法: python3 db_log_compare.py exportlogfile importlogfile")
        exit()
    exportlogfile = sys.argv[1]
    importlogfile = sys.argv[2]
    exportlogs = parse_source_log(exportlogfile)
    importlogs = parse_source_log(importlogfile)
    print(len(exportlogs))
    if len(exportlogs) != len(importlogs):
        print("导出导入数据表数量不一致" + " 导出表:" + str(len(exportlogs)) + " 导入表：" + str(len(importlogs)))
        exit()
    compare_log(exportlogs, importlogs)
