# coding: utf-8
# python 3.12.3
# @Author: siyue_huifeng
# @Time: 2024/12/8

import logop

log = logop.Logging(stdout=False)
log.add_stream(logop.StandardOutputStreamPlus())
log.add_stream(logop.FileOutputStream())
log.set_format("[{date} {time}] [{level_name}] > {message}")