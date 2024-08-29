# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

define wjs = Character("593")
define cz = Character("见")
define ks = Character("K.")

image wjs_idle = "images/sprites/593.png"
image wjs_ques = "images/sprites/593_ques.png"
image cz_idle = "images/sprites/cz.png"

image bg zszx_dawn_sky = "images/bgs/zszx_dawn_sky.jpg"

# 游戏在此开始。

label start:

    # 显示一个背景。此处默认显示占位图，但您也可以在图片目录添加一个文件
    # （命名为 bg room.png 或 bg room.jpg）来显示。

    scene bg zszx_dawn_sky

    show wjs_idle

    wjs "我是火日女神593"

    show wjs_idle:
        choice:
            easein 1 xalign 0.0

    show cz_idle:
        xalign 1.0

    wjs "这是小见"
    cz "..."

    hide wjs_idle
    show wjs_ques:
        xalign 0.0
        yalign 0.64

    wjs "? 不想说话么"
    cz "...只是想吐槽为什么我们是线稿"
    ks "啊拉也是没办法的事啦，谁让我这个写程序的不会画画（"
    ks "光是扣人物和对齐高度就花了我好久了"
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