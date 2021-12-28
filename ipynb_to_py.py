# coding=utf-8
import json
import os

ipynb_file_path = os.path.join('40狗的品种识别/')
ipynb_file_names = [
    '狗的品种识别',
]

for name in ipynb_file_names:
    with open(ipynb_file_path + name + '.ipynb', 'r', encoding='utf-8') as file:
        txt = ''
        for line in file.readlines():
            txt += line
        txt_json = json.loads(txt)
        output_txt = ''
        for cell_txt_json in txt_json['cells']:
            if cell_txt_json['cell_type'] == 'code':
                for source_txt in cell_txt_json['source']:
                    output_txt += source_txt
            output_txt += '\n'
        print(output_txt)
        with open(ipynb_file_path + name + '.py', 'w', encoding='utf-8') as output_file:
            output_file.write(output_txt)
