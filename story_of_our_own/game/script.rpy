# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

define wjs = Character("593")
define cz = Character("见")

image wjs_idle = "images/sprites/593.png"
image cz_idle = "images/sprites/cz.png"

# 游戏在此开始。

label start:

    # 显示一个背景。此处默认显示占位图，但您也可以在图片目录添加一个文件
    # （命名为 bg room.png 或 bg room.jpg）来显示。

    scene bg room

    show wjs_idle

    wjs "我是火日女神593"

    show wjs_idle:
        choice:
            easein 1 xalign 0.0

    show cz_idle:
        xalign 1.0

    wjs "这是小见"

    return


'''
# 显示角色立绘。此处使用了占位图，但您也可以在图片目录添加命名为
    # eileen happy.png 的文件来将其替换掉。

    show eileen happy

    # 此处显示各行对话。

    e "您已创建一个新的 Ren'Py 游戏。"

    e "当您完善了故事、图片和音乐之后，您就可以向全世界发布了！"

    # 此处为游戏结尾。
'''