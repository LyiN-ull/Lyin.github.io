# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

define y = Character("core and m2 teacher")
define c= Character("Phy teacher")
define z=Character("作者本人")
define J=Character("Chem teacher")
define oth=Character("other students in class")
define player = Character("[player_name]")
define M=Character("Chem teacher")
init python:
    import datetime
    
    def get_current_time():
        
        now = datetime.datetime.now()
        return now.strftime("%H:%M:%S")  
    
    def get_current_date():
        
        now = datetime.datetime.now()
        return now.strftime("%Y/%m/%d")  
transform shake:
    # block:  # 如果出现报错可以尝试去掉这行的注释
    linear 0.025 xoffset -6 yoffset -6
    linear 0.05 xoffset 12 yoffset 12
    linear 0.025 xoffset 0 yoffset 0
    linear 0.025 xoffset -6 yoffset -6
    linear 0.05 xoffset 12 yoffset 12
    linear 0.025 xoffset 0 yoffset 0
    
transform bounce:
    linear 0.08 yoffset -55
    linear 0.06 yoffset 0
    linear 0.04 yoffset -15  # 轻微回弹
    linear 0.04 yoffset 0    # 最终归位
    


# 游戏在此开始。

label start:
    play music "bgm1.mp3" loop fadein 10.0
    # 显示一个背景。此处默认显示占位图，但您也可以在图片目录添加一个文件
    

    scene bg white
    menu:
        "ver1.0":
            jump ver10
        
        "ver1.1":
            jump ver11

        "ver1.2":
            jump ver12
    
    label ver10:
        "来自作者本人的一句话：这只是一个半成品，有一些立绘和bgm我都还没弄好。{w}如果在不同的线路看到了相似的文字，先别急着读档或者快进。{w}说不定会有些不同呢？"
        "还有，{w}记得存档,{w}记得存档，{w}记得存档。"
        "以上。"
        "......script.ryp loading......"
        "这只是不久前的事。"
        "我是指，{w}我进入十年级...{w}或者说，进入10H8班吧。"
        "真是仓促啊..."
        "不过，{w}我并不想在这里提起一些学习压力什么的。"

    
        "就让我们用最无虑的最幽默的方式来叙事罢。"
        $ player_name = renpy.input("在进入正题前，先告诉我你的名字吧。", length=20)
    
    
        if player_name == "":
            $ player_name = "anonymous"
        "好的，[player_name] "
        "让我们将目光放回本班的老师们。"
        "你会想要了解谁呢？"
        hide lyin grin with dissolve

        menu:
            "phy":
                $ choice = "A"
            "chem":
                $ choice = "B" 
            "m2(same teacher as core math)":
                $ choice = "C"
            "what the hell are these subjects...?":
                $ choice = "D"
            "non of them...":
                $ choice = "D"
    
        if choice == "A":
            jump route_a
        elif choice == "B":
            jump route_b
        elif choice == "C":
            jump route_c
        elif choice == "D" :
            jump route_d

    label ver11:
        scene bg white
        "......script.ryp loading......"
        "嗨。{w}好久不见（）"
        "我是指，{w}自上次编辑这个脚本文件...{w}或者说，编辑这个视觉小说罢...?"
        "不知不觉，下学期期中考已经考完了。（现在是26年4月25日 :)）{w}真是仓促啊..."
        "不过，{w}我也还是并不想在这里提起一些学习压力什么的。这种东西，留给在学校的自己吧...（(汗 QwQ)"
        "......"
        "那就像上次那样，就让我们用最无虑的最幽默的方式来叙事罢。"
        $ player_name = renpy.input("在进入正题前，先告诉我你的名字吧。", length=20)
    
    
        if player_name == "":
            $ player_name = "anonymous"
        "好的，[player_name] "
        "让我们将目光放回本班的老师们。"
        "你会想要了解谁呢？"
        hide lyin grin with dissolve

        menu:
            "phy":
                $ choice = "A"
            "chem":
                $ choice = "B" 
            "m2(same teacher as core math)":
                $ choice = "C"
            "what the hell are these subjects...?":
                $ choice = "D"
            "non of them...":
                $ choice = "D"
    
        if choice == "A":
            jump route_a
        elif choice == "B":
            jump route_b
        elif choice == "C":
            jump route_c_ver11
        elif choice == "D" :
            jump route_d



    label ver12:
        scene bg white
        "......script.ryp loading......"
        "你好啊。{w}又是好久不见（）"
        "要不是因为一些事情，我都快忘记这个烂尾的摊子了（）"
        "不知不觉，下学期期末考已经考完了。（现在是26年7月6日 :)）{w}6767676767(被打)"
        "这大概是我为这个神秘作品脚本的最后一次更新了。居然有点舍不得呢。"
        "你也许已经意识到了，封面上多了一位老师。请别见怪就是了。"
        "......"
        "那么，就像上次那样，准备好罢。。"
        $ player_name = renpy.input("在进入正题前，先告诉我你的名字吧。", length=20)
    
    
        if player_name == "":
            $ player_name = "anonymous"
        "好的，[player_name] "
        "让我们将目光放回本班的老师们。"
        "你会想要了解谁呢？"
        

        menu:
            "phy":
                $ choice = "A"
            "chem":
                $ choice = "B" 
            "m2(same teacher as core math)":
                $ choice = "C"
            "what the hell are these subjects...?":
                $ choice = "D"
            "non of them...":
                $ choice = "D"
    
        if choice == "A":
            jump route_a
        elif choice == "B":
            jump route_b
        elif choice == "C":
            jump route_c_ver11
        elif choice == "D" :
            jump route_d

label route_c_ver11:
    scene bg white
    "看不出来啊，你居然这么喜欢数学（或者数学延伸单元二？）哈哈。"
    "还是说。{w}你只是喜欢这个老师呢"
    "我当然不会拦着你再看一遍这条线啦（）"
    "那一道remainder thm.的题目，即使再写一遍还是会有点卡壳罢（）"
    "祝你好运）"
    jump route_c

label route_a:
    scene bg white

    stop music          # 停止当前BGM
    play music "bgm3.mp3"   # 播放新BGM
    "嗯哼。是个首选物理的人嘛"
    "又或者是看完其他支线回来的？"
    "总之，{w}欢迎"
    "这个老师其实我九年级就是他教了。当时我对他的印象就是..."
    "这也...{w}太催眠...了吧...（你知道的，九年级我们物理教的真的很简单，进度又很慢）"
    "不过时间到了现在。"
    $ time_now = datetime.datetime.now().strftime("%H:%M")
    scene bg classroomm2 with dissolve
    "哦哦，[time_now]。上课铃响了一段时间了。{w}那些还没进教室的..."
    "*几个同班同学从前门进了教室*"
    
    show c_chau at Position(xalign=0.5) with dissolve  # 从左边0.2处开始
    c "why are you late...?{w}well..."
    show c_chau at Position(xalign=0.8) with MoveTransition(0.5)



    c "（从透明文件夹里拿出一张纸）come here and write down you name, ok?{w}I will give you a penalty next time.: )"
    "(哦...他管的好严啊）"
    "其实并非，还是挺佛系的。只是记录下名字，他倒是没真的记过违规。"
    hide c_chau
    show c_normal at Position(xalign=0.8) 
    c "no one can answer this...?Come on just have a try.(*这种情况也不是没人会做，只是我们班都懒得举手了）"
    hide c_normal
    show c_chaifen1 at Position(xalign=0.8) 
    c "[player_name],answer the question?"

    c "书上说的是，频率越高的电磁波(electromagnetic waves)，通常来说会有更大的能量。{w}你知道这对应的公式吗？"
    "（啊...）"
    menu:
            "v=f * lambda":
                $ choice = "1"
            "S=v * t (你当然不会选这个，对吧）":
                $ choice = "1" 
            "E=h * f":
                $ choice = "2"
            "T^2MG=4pi^2r^3":
                $ choice = "1"
            "....what?":
                $ choice = "1"

    if choice == "1":
        jump route_a01
    elif choice == "2":
        jump route_a02       
label route_a01:
    show c_chaifen1 at right with dissolve
    c "没关系，我们会在十一...十二年级学到这些公式。所以不用着急。" 
    c "（继续讲课）"
    hide c_chaifen1  with dissolve
    "（啊...太好了。感觉没有那位教m2的恐怖啊）"
    "嗯哼，毕竟他年纪也挺大的，说实话，我没怎么见他发过火。"
    "虽然你选错了，但还是让我的故事继续下去吧。"
    
    jump route_a03

label route_a02:   
    show c_chaifen1 at right with dissolve
    c "不错呢。这是我们会在十一...十二年级学到的公式。所以不用着急。"
    c "（继续讲课）"
    hide c_chaifen1  with dissolve
    "也许你提前学过了？真不赖。"
    "考虑今年11月来考BPhO吗？^_^..."
    "咳咳，我开玩笑的，当我没说（（（"
    "既然你答对了，那故事就要继续了。"

    jump route_a03

label route_a03:
    scene bg classroomm2
    show c_chaifen1 at right with dissolve
    "(......)"
    c "（继续慢慢悠悠地讲PPT，以及抽取人回答问题）"
    "（......其实我想问，他一直都讲这么慢吗....????)"
    "你现在知道为什么我之前说他真的很催眠了吧。"
    "不过你要是单独去找他问问题，他会详细讲给你听的。{w}他确实有这个实力）"
    "我在考SPC前两天就问过他一道电阻题目，他也立马给我讲解怎么做了XD"
    scene bg qres
    "sudden QUIZZZZ!:[player_name] 你会分析这个导线两端电阻阻值吗？"
    menu:
            "会":
                $ choice = "A"
            "不会":
                $ choice = "A" 
            "我想到了绝妙的过程，可你没有给输入框，我写不下。":
                $ choice = "B"

    if choice == "B":
        jump route_a_0x00
    elif choice =="A":
        jump route_a_cont

label route_a_0x00:
    "AUV费马大人（）扣一找我领免费大张草稿纸，量大管饱！"
    $ renpy.input("这能忍住不扣11111111？")   
    "笑死，我甚至没有保存这个输入，反正不会影响走向就是了（）"
    "不过你要是真的缺纸我是真的可以给你草稿本（）只要你是和我现在同校的说。"
    "啊，扯远了，回归正题。" 
    jump route_a_cont

label route_a_cont:         
    scene bg sit with dissolve
    "呵呵...这道题就留给玩家做练习好了。要是不会的话你还可以去找他问哦？（当然我觉得你应该会的，对吗）"
    "啊啊，果然只要不听课，时间就会过得很快呢。{w}已经下课了哦。"
    "你现在想干些什么呢？......"
    menu:
            "好累啊...课间就休息吧。":
                $ choice = "A"
            "（口艾 口牙 我手滑点到这个选项惹XPP！）":
                $ choice = "B" 
            "真的什么题都能问他吗...？":
                $ choice = "C"

    if choice == "A":
            jump route_a_end1
    elif choice == "B":
            jump route_a_end2
    elif choice == "C":
            jump route_a_end3       

label route_a_end1:
    scene bg sit with dissolve
    
    "也是，我码字码到这里也挺累的。现在甚至是26号凌晨了。"
    "关于他的事情就讲到这里吧？"
    "如果你想知道更多，为什么不读档回去看看其他老师的支线呢？（笑）"
    scene bg white with dissolve
    "希望你不是忘记存档了。"
    "虽然我还没写完完整的脚本呢。"
    "另外，如果你直接选了这个选项，那你大概你漏掉了一张CG ：）{w}如果你作弊去翻了图片文件夹，那我也没什么好说的了。"
    "这条线就写到这里吧...说实话，比起上次的部分，真的加了一倍有多的选项...真挺累的。"
    "休息一下好了。"
    "(达成：轻松的结局...吗？)"
    
    jump route_d1
    # A路线剧情
    return

label route_a_end2:
    scene bg white
    "......"
    "OK.TRUST YOU.(--- by that math teacher)"
    "(达成：手滑的人...？)"

    return

label route_a_end3:
    scene bg sit with dissolve
    "<（^_^）>对。"
    "我前阵子（现在也）在为一些转动惯量的计算烦恼来着。你知道的...我的数学能力有限。"
    
    z "老师，你现在有空吗...能不能帮我看看...系数...2/5.....1/2.....（说了一堆问题）"
    show c_sp at center with dissolve
    c "......"
    c "wah...你确实问到我了。我需要回去准备一下这个呢。"
    hide c_sp at center with dissolve
    "......"
    "......"
    c "......"
    "（啊，他回来了！）"
    scene cg_route_a01 with dissolve
    c "嘛，（递过来）这里就是一些过程了。"
    scene cg_route_a02 with dissolve
    c "就是要用*一点点*积分，你们学过吧：）"
    "（他人还真的怪好....)"
    with vpunch
    "(这tm啥啊？！！)"
    "所以说，他很有能力，他的方法也太高明了。"
    "也就是说，我没法理解这个方法。"
    with vpunch
    "毕竟我不会球坐标系啊....!!!!!!QAQ)"
    "不过我还是很感谢他的，至少他让我不得不好好学积分。{w}也许之后还会有机会和他jogging？"
    "......"
    scene bg white with dissolve
    c "PHYSIC IS SIMPLE ,BUT NOT EASY :) --- by the Phy teacher"
    "（达成：博学的结局...大概。）"
    "感谢你愿意玩...或者看到这里，真的。"
    "我这一整个script下来，全都是些无厘头的东西..."
    "如果能给你带来一点乐子，那也不坏。"
    "总之，非常感谢。（鞠躬）{w}下一次再动工可能又是一段时间之后了。"
    "总之，这是一个好结局（至少在我的设定上）"
    "现在，要跳转去固定的结尾流程咯。"
    "......"

    jump route_d1
    # A路线剧情
    return




label route_b:
    stop music
    scene bg white
   
    "对了，我们班是有两位化学老师的。"
    "你还记得自己的学号吗？"
    menu:
       "奇数":
            jump route_b01
       "偶数":
            jump route_b02

label route_b02:
    play music "bgm4.mp3" loop
    $ renpy.music.set_volume(0.2, channel="music")
    scene bg classroomm2 with dissolve
    "我一直在想一件事，{w}很多时候，学生们都会模仿老师的语气语调甚至音色和口音..."
    "但是这个老师的发音没人模仿的来吧...."
    #立绘 中间
    show j_normal at center
    J "..."
    J "students, from now on you should call me Mr.James and NO MORE Mr.To, OK?"
    J "我作为老师肯定是想和同学们走近一点..."
    "（啊——这么有亲和力的老师。）"
    "比起亲和我觉得电波系更能描述他。"
    "那是在分班之后，我们这个班去了实验室上课..."
    J"额 你们也看到了 我的嗓子呢不是很好的，所以这节课..."
    #立绘左移
    show j_smile at center 
    hide j_normal
    show j_smile at Position(xalign=0.0) with MoveTransition(0.5)
    J "你们先写题，{w}之后我来讲噢。"
    "（只是正常的上课啊）"
    "你在失望什么啊（）"
    "在他（老师）还在待机时，来看下这道题吧。"
    "对。他出在这次期末的题目："
    hide j_simle with dissolve
    scene chem_1 with dissolve
    #chem1
    "..."
    "（我记得这根本不在范围内吧？？？）" with hpunch
    "（再说了，{w}卤素盐的反应，之前作业里不是说{color=#ff0000}绝对不会考{/color}吗？！）"
    "唉。"
    menu:
        "好吧，我写！":
            jump route_b01_a
        "这算什么化学课啊？都没有实验的？":
            jump route_b_con



label route_b01_a:
    "那请先输入这道题的答案吧："
    $ answer = renpy.input("（格式：反应物+反应物=产物+产物）")
    
    if answer == "H2SO4+NaCl=NaHSO4+HCl":
        "对，看来你有好好看题啊（）"
        "下一道"
        scene chem_2
    else:
        "哈，怎么和我一样，是没看题的人啊。"
        "不过没事（）"
    #chem2
    "要怎么modify呢？"
    menu:
        "dilute H2SO4":
            $ choice = "a"
        "HCl(aq)":
            $ choice = "b"
        "HI(aq)":
            $ choice = "c"
        "use H2 and Br2":
            $ choice = "d"
        "H3PO4":
            $ choice = "e"
        "CH3COOH":
            $ choice = "f"
        "(COOH)2":
            $ choice = "g"
    
    if choice == "e":
        "讲完试卷之后，谁都知道了吧（叹）"
        "谁能想到是用磷酸呢。"
    else:
        "...好好听试卷解析吧，下次。"
    
    scene bg classroomm2 with dissolve
    show j_smile at Position(xalign=0.0) with dissolve  # 从左边0.2处开始
   
    show j_smile at Position(xalign=0.5) with MoveTransition(0.5)
    J "OK---STUDENTS！If you still not finish, 我多给你一分钟。"
    "（好有磁性的声音（））"
    show j_oo at center
    hide j_smile
    J "另外，你们都知道我喉咙不太行的啦，{w}所以今天..."
    show j_normal at center
    hide j_oo
    J "我就打字给你们讲了！"
    "（？？？？？）" with hpunch
    J "（以下内容皆为打字输入）"
    show j_clear at center with vpunch
    J "{cps=15}@#￥%%……&*（*&……%%￥#，这个非常重要，大家听懂了吗？QWQ{/cps}"
    show j_clear at center with vpunch
    J "{cps=10}总之，先*&……%%￥#再#￥%%……&*&，这就是答题格式了哟！*0v0*{/cps}"
    show j_clear at center with vpunch
    J "大家一定要记住哦>.<" 
    "............." 
    "!? >.< ?!" 
    hide j_clear
    scene cg_route_b02 with dissolve
    "（这。）"
    "（全班人尖叫）"
    "他在卖萌吧...大概"
    oth "一定要记住哦~~~~~~--->.<"
    "（简直疯了）"
    "日常而已。"
    "所以我说了他简直就是电波系啊。"
    $ preferences.text_cps = 100
    window auto 
    "（话说，你为什么给他画了一个* E5&B7%%A8#E@4B?9B3（捂嘴） {nw}"
    window auto hide
    "啊哈。只是想画。"
    "...."
    #cg淡出
    
    scene bg white with dissolve
    "嘛，到这里，这条线就差不多结束了。你也获得这张CG了"
    "如果愿意的话，可以去看看其他支线：）"
    "感谢你的游玩。（鞠躬）{w}我知道这条线很水，但我的产能确实有限（）"
    "..."
    jump route_d1



label route_b_con:
    "uhoh."
    "你知道我要说什么"
    "很抱歉我忘记做这个支线了..."
    "下次一定()"
    "进入另一条路线。"
    "对不起，我还没写好脚本。"
    "restricted access"
    jump route_d1


label route_b01:

    play music "Storyteller.mp3" loop    
# 全屏文本显示模式（使用 narrator 或自定义 screen）
    show text "{color=#ff0000}如果您在看的话\n我在这里仅对事实稍作改编\n真的无意冒犯\n另外，按照你说的，BGM我用的stroyteller()不用谢\n就这样\n---LYN_{/color}" with dissolve
    pause 5.0  # 停留5秒后继续
    hide text with dissolve

    "我并不是这位老师的学生，毕竟我学号是偶数。"

    "但最开始，他似乎是从某节课开始来观课的。"

    "然后，再分成两批学生之前教过我们几堂课(?)我记得那是教酸碱和pH的时候。"



    "到这里为止都还挺正常的，直到不知道谁说*新老师玩明ΔΔ舟*来着...."
    scene bg classroomm2 with dissolve
    player "我说把通行证摆在这里，真的能吸引到人吗"

    oth "事已至此先画画吧。"

    show m_standard with dissolve
    show m_standard at shake

    M "（非常突然的拿起了桌上的通行证）"
    M "......"
    
    show m_notice with dissolve
    hide m_standard
    M "你们玩Φ啊"

    player "哦哦....呃，对()"

    "(沉默。)"
    
    
    show m_spk with dissolve
    hide m_notice
    M "（开始分析通行证上的角色的卡池还是强度什么的）"

    M "......"
    show m_spk at shake
    
    M "（掏手机）"
    show m_account with dissolve
    hide m_spk with dissolve
    M "....我的账号。"

    "（我还没来得及说话，半个班的Φ批已经闻着味来了(）"

    "(我说，班上这个成分，一班人是打危机合约认识的吗(x))"
    scene bg white with dissolve

    "....笑死("

    "总之，我想说的是，这条线与其说是关于这位老师和化学倒不如说是关于游戏的。"

    "(所以比较水，我滑跪，我肝不动了。)"


    "在那之后，毕竟不是负责我的教学的老师，自然不太会交流的("

    
    scene bg classroomm2 with dissolve
    "(某天课间)"
    show m_standard
    show m_standard at bounce
    M "（拿出折叠手机）这是今年音律:)"
    M "我抢了票然后去听。"
    show m_standard at bounce
    M "我前几年也去了（诸如此类的话说了一堆）"
    hide m_standard
    oth "我趣，老资历。"
    oth "！？强强？！"

    "啊.....现场听吗。今年还有mili,这也吃太好了wwww"

    menu:
        "啊--所以只是玩游戏，和老师很难混熟吧":
            jump route_b_con
        "虽然班上不缺玩Φ的人，但是同好多多益善罢":
            jump route_b02_a

label route_b02_a:
    scene bg classroomm2 
    player "对了老师，今年暑假前校园节有Φ的摊位。记得来支持"
    scene bg classroomm2 with vpunch
    oth "对对对来支持)"
    scene bg white with dissolve
    "(于是到了七月初)"
    "啊啊 画完宣传板子了"

    "把我们摊位东西搬出去吧！"

    player "话说老师会不会过来"

    oth"会吧()他不是说还会买点东西周边什么的吗"

    "......"

    "摊位没摆上多久。"
    show m_notice at right with dissolve 
    "然后他拎着一堆东西就走过来了()"
    show m_bgds at right with dissolve
    hide m_notice
    M "你们怎么选了这么角落的一个位置..算了，这里有些卡片和盲抽徽章，你们要展示，知道吗。"
    M "这个24年音律的票根主要是向圈外人介绍我们有音律这种活动，好吧。"
    show m_vol6 at right with dissolve
    hide m_bgds 
    M "这个是纪念画册....."
    M "总之，要展示出来，我就一个要求——"
    show m_vol6 at right,bounce
    M "别 输 给 旁 边 的 摊 位"
    hide m_vol6 with dissolve
    scene bg white with vpunch
    "(不是，隔壁可是米Φ游的Φ批摊位啊？)"
    "(........)"
    show m_sp with dissolve
    "(也没什么人在听他讲吧())"
    show m_sp with vpunch
    oth "(拿着画集)我靠，我靠！！！！所有人，品鉴！！！！"
    show m_sp with vpunch
    oth "我靠，画的太tmΦΦ了，这个海报———"
    show m_sp with vpunch
    oth "(拿着平板开始打危机合约)"

    "(最后呢？)"
    hide m_sp with dissolve
    "还可以吧，摊位还是一直有人的，不过我们摊位游戏的受众应该是牌佬((("

    "于是被老师吐槽有点复杂了(我没意见)当然那几个打危机合约的也挺红温()"

    "到最后结束的时候"
    scene m_cg01 with dissolve
    M "那最后，我自留一部分周边手办，剩下的你们自己分吧。"

    "(咦咦，分的内容甚至有山山兔和画集...???)"
    M "对。"

    "于是大家挑选起来。"
    scene m_cg_sp with dissolve
    "身后的白板上已集结了许多在场与不在场的Doctor的签名。"
    ##这里展示一下##
    M "...."
    scene m_cg01 with dissolve
    "(听起来很开心的样子)"
    M "我拿了蓝牙音箱下来，现在摊位上可以放歌了。"
    scene m_cg02 with dissolve
    M "我跟你们说，你们之后一定要想办法今日学校广播室让每个人的设备都播放众生行记OST(乱讲一通玩笑)让电子设备赛博飞升巴拉巴拉"

    ":)"
    scene bg white with dissolve

    show text "最后，拿到了amy山山兔很多周边)){w}\n 真是不错)"
    pause 3.0
    hide text with dissolve

    show text"{color=#ff0000}顺便，在此感谢为我们小摊位购入这么多东西{/color}\n 收获颇丰.{w}\n 好耶。{w}\n 明年也许会继续罢。"
    pause 3.0
    hide text with dissolve
    "......"

    
    show text "好了，这条线的完成，代表着这个v.n.主线全部的完成。{w}还有一条彩蛋，打算之后有精力再画。{w}\n毕竟每次都是心血来潮，熬个大夜或者通宵，草草画完图写完script再丢进renpy里然后修一堆报错{w}\n在制作这个整活向的时候，试着尝试运用很多新奇的效果，甚至自己设置transform什么的，尝试了更多renpy的功能{w}\n(这很困难....才不是因为版本太低？)\n总之 零零碎碎的拼起来 终于有点成型的样子了。{w}\n感谢你的耐心观看。\n非常感谢(鞠躬)\n那么...."
    pause 10.0
    hide text
    jump route_d1








    return






label route_c:
    "哈哈，这位老师吗..."
    "你知道的，他在全年级里都很出名，{w}即使你不是他的学生，你也应该认识他。"
    "他负责了上学期M2 chapter3的出卷，和期末核心数学的出卷。哦对了，与时俱进一点，他出了十年级期末M2卷，对。"
    "那一份神秘猎奇coordinate geometry的作业纸也是他出给全年级的。这次的神秘M2我也没什么想说的了。"
    "不过，{w}你上了他的课才会知道...{w}他这个人...()"
    scene bg classroom with blinds
    show ymy normal at center with blinds
    y "..."
    hide ymy normal
    show ymy teach
    y "你这写的什么来的？"
    y "怎么能直接从f(x)=2(5x-1)(x+2)开始解？？哈啊？！"
    y "原函数都不抄下来的？"
    hide ymy teach
    show ymy angry with vpunch
    y "数学上正确，{w}考试上错误！"
    show ymy angry with vpunch
    y "公开文凭试的游戏规则就是这样。"
    hide ymy angry
    show ymy teach
    y "你们必须先成为*我想让你们成为的样子*，然后再去成为你们想成为的样子。OK？"
    "(啊啊...真是教学风格独特呢。)"
    "(...)"
    "(...等下？)"
    hide ymy teach
    show ymy normal
     
    y "..."
    $ time_now = datetime.datetime.now().strftime("%H:%M")
    y "it is ...[time_now]"
    y "（一段精密的口算四则运算）"
    y "student number xx ——"
    y "that is,you,{w}[player_name],{w}asnwer the question."
    show ymy normal:
        xalign 0.5  ###
        linear 0.3 xalign 0.95
    scene bg q23 with blinds 
    y "what is your answer...?"
    "*来自作者的再三提醒：{w}记 得 存 档 。*"
    $ player_ans_maco = renpy.input("A/B/C/D ?", length=10)
    if player_ans_maco == "B":
        jump route_aa
    elif player_ans_maco == "A" or "C" or "D" :
        jump route_ab
    else :
        jump route_ac

label route_ab:
    scene bg classroom
    show ymy teach at center with dissolve
    y "...ok,没事。这道题比较难。"
    y "坐下来听讲。"
    "(哈...{w}吓死我了。)"
    scene bg white 
    "他大概就是这么一个人"
    "不过，既然答错了，不读档回去再来一次吗？"
    "..."
    "看来你到现在都没有读档呢。{w}我是指，听我讲了这么多废话。"
    "那就由我来送你出去罢。"
    jump route_d1

    return
    

label route_aa:
    scene bg q23
    show ymy normal at center 
    y "OK,good."
    "(啊啊...看来是答对了)"
    hide ymy normal with dissolve
    "*这一轮回答通过了呢。{w}你是自己做出来的，对吗？（笑）{w}哈哈，不用紧张，这只是一个视觉小说。...但如果是考试的话，可就没有读档的机会了？*"
    "*回归正题。还有一门不得不品的课...就是M2了。*"
    scene bg classroomm2 with  pixellate
    show ymy angry at center with dissolve
    stop music 
    y "喂。"
    show ymy angry with vpunch
    y "在我的M2课上写core作业？"
    y "你很急吗？你家人不让你寒假写作业啊？{w}你是不是今晚七点就要去赶飞机再也不回来啊？{w}你这么想写，{w}不如晚上三四点拿个小夜灯在宿舍里写啊？！{w}你现在就是既要又要——"
    show ymy angry with vpunch
    y "一己私欲喔！！！？"
    "(啊啊，还好他不是在说我吧...)"
    "(...啊？)"
    scene bg classroomm2 with vpunch
    "（怎么在朝着我这边走啊！！！）"
    scene bg ymycg with dissolve
    y "..."
    y "翘什么腿！{w}没礼貌的坏毛病。"
    y "听不见我说话吗？？？"
    "(呃啊，是我后排那位同学吗...)"
    "*哈，保留节目来了。*"
    y "放下来，张开腿，塞进去。"
    y "听不懂人话？？？"
    y "放 下 来，{w}  张 开 腿，{w}  塞 进 去。{w}"
    "(这是什么虎狼之词啊喂...)"
    "*...that is.*"
    "*我们班常态了。{w}还没算上被扔粉笔头的说。"
    "*我上周五清理座位的时候，还在我桌子底下找到好几个粉笔头...你知道的，我并没有被扔过（"
    scene bg white 
    "你已经获得这张CG了，现在你可以离开这条线了"
    "我是说，虽然我很想再分享他的更多事迹，但我真的产能有限（）"
    "感谢你能耐心看完这条线。actually，这是我写的第一条线（虽然其下有若干个分支就是了）"
    "..."
    "看来你到现在都没有读档呢。{w}我是指，听我讲了这么多废话。"
    "那就由我来送你出去罢。"
    "我也刚好编不出script了。哈（）"
    jump route_d1



















    # C路线剧情
    return

label route_d:
    "(我是想说,{w}谁会对你们这些elective感兴趣啊...)"
    
    "这样吗..."
    "常有人这么说。{w}\n 既然这样，那你也没必要再看下去了，不是吗？"
    
    "如果你只是好奇点进了这个选项，那就尽快读档回去吧。{w}\n 嘛，你要是没有存档的话就是你活该了。XD"
    "好吧，我不会这么说我的玩家的。"
    "如果你还想再去试试另一个作死选项也没必要了，我在第4、5个选项后设置的路线是一样的。"
    
    "看来你到现在都没有读档呢。{w}我是指，听我讲了这么多废话。"
    "那就由我来送你出去罢。"
    "我也刚好少写一段script了。哈（）"
    
    
    "再会。"
    menu:
        "再见。":
            $ choice = "BE"
        "ヾ(￣▽￣)":
            $ choice = "BE"
        "神人rpg，乐。":
            $ choice = "BEBE"
    
    if choice =="BE":
        return
    if choice =="BEBE":
        "..."
        "[player_name],我说啊..."
        "你需要知道一个热知识，我使用renpy引擎做出来的东西叫做\n {w}视-{w}觉-{w}小-{w}说。"
        return

label route_d1 :
    "再会。"
    menu:
        "再见。":
            $ choice = "BE"
        "ヾ(￣▽￣)":
            $ choice = "BE"
        "神人rpg，乐。":
            $ choice = "BEBEBE"
    
    if choice =="BE":
        return
    if choice =="BEBEBE":
        "..."
        "[player_name],我说啊..."
        "你的爱好就是点击这些无意义的选项吗...?"
        "哈。"
        return



    


    # 显示角色立绘。此处使用了占位图，但您也可以在图片目录添加命名为
    # “eileen happy.png”的文件来将其替换掉。

    

    # 此处显示各行对话。

    y "您已创建一个新的 Ren'Py 游戏。"

    y "当您完善了故事、图片和音乐之后，您就可以向全世界发布了！"

    return