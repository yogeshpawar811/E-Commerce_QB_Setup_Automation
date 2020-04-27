#
#
# data="(Docid: 1090966204 )Status: New(7), Default(0) | JAN-10-2020 00:09:04Evision Docid: 16304324118 | Message: Warehouse/Store # 9CTC TPID: 043EDIBACCUS000"
#
# import re
#
# # s = 'asdf=5;iwantthis123jasd'
# # result = re.search('Evision Docid: (.*) | Message', data)
# # print(result.group(1))
#
#
# s = 'asdf=5;iwantthis123jasd'
# start = 'Evision Docid: '
# end = ' | Message:'
#
# result = re.search('%s(.*)%s' % (start, end), data).group(1).split(("|"))[0]
# print(result)

str="5000g00002EFpx2_CASES_CASE_NUMBER"

print(str.split("_")[0])