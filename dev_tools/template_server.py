#! /bin/env python3
import argparse
import json
import math
import os
from typing import Union

from flask import Flask, redirect, url_for
from jinja2 import Template
import jinja2


def _parse_args():
    parser = argparse.ArgumentParser(prog='passer_template_server',
                                     description='模板开发工具')
    parser.add_argument(
        'template', help='模板文件路径, eg: test-data/src/template.html')
    parser.add_argument(
        'parameter', help='参数文件路径, eg: test-data/parameter.json')
    return parser.parse_args()


def format_number(value: [int, float, math.nan, str],  # type: ignore
                    digits:int = 0, 
                    placeholder:any = '--'
                    ) -> any:
    """
    格式化数字，传入字符串时尝试转为浮点数。当value为 None或math.NaN时返回default，传入其他无法转为数字的值
    时则给出提示字符串。
    Args:
        value: 传入值
        digits: 保留位数
        placeholder: 用于替换 None 或 math.NaN 的值
    """
    if value is None or math.isnan(value):
        return placeholder
    try:
        value = float(value)
        return f'{value:.{digits}f}'  
    except ValueError:
        return 'Invalid number:' + str(value)


def _main():
    args = _parse_args()
    template_path = args.template
    parameter_path = args.parameter

    static_folder = os.path.abspath(os.path.dirname(template_path))
    print('The static folder: ', static_folder)
    app = Flask(__name__, static_folder=static_folder, static_url_path='')

    @app.route('/template.html')
    def serve_template():
        parameter = json.load(open(parameter_path, 'rb'))
        env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_path))
        env.filters['format_number'] = format_number
        with open(template_path, 'r', encoding='utf-8') as f:
            template = env.from_string(f.read())
        print("Rendering parameters got: ", parameter)
        return template.render(data=parameter)
    
    @app.route('/')
    def root():
        return redirect('template.html', code=302)

    app.run(host='0.0.0.0', debug=True)


if __name__ == '__main__':
    _main()
