# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  author: zhangmiao
  date:  2025/4/28 18:32
  file:  show
  Description :
-------------------------------------------------
"""


def show(graph, output_path='output.png'):
    try:
        print("=====show======")
        image_data = graph.get_graph().draw_mermaid_png()
        # 将图像保存到文件
        with open(output_path, 'wb') as file:
            file.write(image_data)
    except Exception:
        pass
