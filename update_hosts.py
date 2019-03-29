#coding=utf-8
"""
Create on 19-3-26

@author: hzx

@requirements: PyCharm 2017.2.4, Python 3.5
"""
import sys
import os
import shutil

FILE_PATH = '/etc/hosts'
BAK_PATH = '/etc/bak/hosts_bak'

"""
使用说明：
    备份hosts文件：python update_hosts.py bak        # 备份路径为'/etc/bak/hosts_bak'
    还原hosts文件：python update_hosts.py reduction  # 从备份文件还原
    清除备份hosts文件：python update_hosts.py clear   # 将备份hosts文件删除
                                方法   IP        网址
    添加：python update_hosts.py add 0.0.0.0 www.google.com
    删除：python update_hosts.py del 0.0.0.0   删除整行
    修改：python update_hosts.py change www.baidu.com www.google.com
"""


def bak_reduction_hosts(flag):
    """
    包含三个功能：
    1.hosts文件备份,备份后的路径为'/etc/bak/hosts_bak'
    2.hosts文件还原,存在备份文件'/etc/bak/hosts_bak'时使用该文件还原hosts并删除备份文件
    3.清除备份hosts文件
    :param flag: 对hosts文件的备份/还原/备份文件删除的操作选择
    :return:
    """
    if flag in ['bak', 'reduction', 'clear']:
        if flag == 'bak':
            if os.path.exists(BAK_PATH):
                print('备份文件已存在！')
                pass  # 存在备份hosts文件时不做修改
            else:
                try:
                    shutil.copyfile(FILE_PATH, BAK_PATH)
                    print('已完成Centos7下的hosts备份')
                except PermissionError as e:
                    print(e)
                    print('You must use \'sudo\' command')
        elif flag == 'reduction':
            if os.path.exists(BAK_PATH):
                try:
                    shutil.copyfile(BAK_PATH, FILE_PATH)
                    os.remove(BAK_PATH)
                    print('Reduction \'hosts\' Complete!')
                except Exception as e:
                    print(e)
                    print('You must use \'sudo\' command')
            else:
                print('No hosts_bak file!')
        elif flag == 'clear':
            if os.path.exists(BAK_PATH):
                try:
                    os.remove(BAK_PATH)
                    print('Remove hosts_bak complete!')
                except PermissionError as e:
                    print(e)
                    print('You must use \'sudo\' command')
            else:
                print('不存在备份hosts文件,清除操作已完成!')


def alter_hosts():
    try:
        if sys.argv[1] == 1:
            pass
        elif sys.argv[1] == 2:
            pass
        elif sys.argv[1] == 3:
            pass
    except Exception as e:
        print(e)


if __name__ == '__main__':
    arg_len = len(sys.argv)
    if arg_len in [0, 1]:
        print('Please input params！')
    elif arg_len == 2:  # 对hosts文件进行备份/还原/备份文件清除
        flag2 = sys.argv[1]
        if flag2 in ['clear', 'reduction', 'bak']:
            bak_reduction_hosts(flag2)
        else:
            print('You must use second param like \'bak\' or \'reduction\' or \'clear\' but \'%s\'' % str(sys.argv[1]))
    elif arg_len >= 3:  # 选择对hosts文件内容进行添加/删除/修改等操作
        try:
            alter_hosts()
        except Exception as e:
            print(e)

