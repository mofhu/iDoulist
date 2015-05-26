# -*- coding: utf-8 -*-
# Author Frank Hu
# iDoulist Function 0 - output

'''
std test
output_list = ['http://book.douban.com/subject/1139336/', 
               'http://book.douban.com/subject/25724948/']
'''

def output_CLI(output_doulist):
	print 'iDoulist: 导出的豆列包含以下书籍'
	for i in output_doulist:
		print i

def output_file(output_doulist):
	file_target = file('iDoulist.md', 'w')
	file_target.write('# iDoulist: 导出的豆列包含以下书籍 \n\n')
	for i in output_doulist:
		file_target.write(i + '\n\n')
	print 'iDoulist: 书籍列表已被导出为 iDoulist.md'
	file_target.close()

'''
def output_file(output_doulist):
	title = "iDoulist"

	from jinja2 import Environment, FileSystemLoader
	jinja_env = Environment(loader=FileSystemLoader('./'))
	template = jinja_env.get_template('iDoulist.mdtemplate')

	s = template.render(messages=output_doulist, title=title)

	with open('{0}.md'.format(title), 'w') as f:
		f.write(s.encode('utf-8'))

	print 'iDoulist: your input Doulist is exported as {0}.md'.format(title)'''