from chord import Chord
#样例数据：
matrix = [
    [0, 5, 6, 4, 7, 4],
    [5, 0, 5, 4, 6, 5],
    [6, 5, 0, 4, 5, 5],
    [4, 4, 4, 0, 5, 5],
    [7, 6, 5, 5, 0, 4],
    [4, 5, 5, 5, 4, 0],
]

names = ["Action", "Adventure", "Comedy", "Drama", "Fantasy", "Thriller"]
# 可视化绘制
hex_colours = ["#222222", "#333333", "#4c4c4c", "#666666", "#848484", "#9a9a9a"]

Chord(matrix, names, colors=hex_colours).to_html()
# Chord(matrix, names).to_html()