#房间字典
rooms={
    "Foyer":{
        'name':'门厅（Foyer）',
        'description':'你身处古堡的阴暗⻔厅。头顶⼀盏布满蜘蛛⽹的吊灯微微摇晃，投下忽明忽暗的光芒。空气中弥漫着潮湿的霉味，下是冰冷的⼤理⽯地⾯。北⾯是⼀扇沉重的橡⽊⻔，⻔上雕刻着狰狞的怪兽头像，东⾯则是⼀条通向⿊暗深处的⾛廊。',
        'items':[{'门厅地毯下的纸条':'（一张陈旧的字条，似乎是从某本书页上撕下来的，上边潦草着写着“光芒指引方向”）'}],
        'exits':{'北':'Grand Hall','东':'Hallway'}  # 修改为简化的键
    },
    "Grand Hall":{
        'name':'大厅（Grand Hall）',
        'description':'你推开橡⽊⻔，进⼊了古堡的宏伟的⼤厅。尽管岁⽉流逝，依稀可⻅昔⽇的辉煌。⼀个巨⼤的⽔晶吊灯（虽然已经缺了⼏盏灯泡）仍然悬挂在⾼耸的天花板上。彩⾊玻璃窗阻挡了外界的光线，使得⼤厅内光线昏暗。南⾯是你进来的⻔厅，⻄⾯是⼀扇装饰华丽的⽊⻔，通往图书馆，东⾯则是⼀道拱形⽯⻔，通向餐厅。',
        'items':[{'壁炉拨⽕棍':'⼀根沉重的铁制拨⽕棍，顶端装饰着狮⼦头。'}],
        'exits':{'南':'Foyer','西':'Library','东':'Dining Room'}  # 修改为简化的键
    },
    "Hallway":{
        'name':'⾛廊 (Hallway)',
        'description':'你沿着昏暗的⾛廊前⾏，脚踩在吱吱作响的⽊地板上。墙壁上挂着褪⾊的家族画像，画像中的⼈物表情模糊不清，仿佛在注视着你。⾛廊尽头似乎传来微弱的滴⽔声。⻄⾯是⻔厅。',
        'items':[{'生锈的铁钥匙':'⼀把锈迹斑斑的铁钥匙，看起来年代久远，也许能打开古堡的某扇⻔。'}],
        'exits':{'西':'Foyer'}  # 修改为简化的键
    },
    "Library":{
        'name':'图书馆 (Library)',
        'description':'你推开装饰华丽的⽊⻔，⾛进了布满灰尘的图书馆。⾼耸的书架⼀直延伸到天花板，上⾯堆满了布满灰尘的书籍。空⽓中弥漫着浓重的旧书和⽪⾰的味道，令⼈昏昏欲睡。阳光透过⾼窗洒进来，照亮了书架上零星散落的⾦箔。东⾯是通往⼤厅的⽊⻔。',
        'items':[{'⼀本厚重的古书':'“⼀本⽪⾯精装的古书，书⻚已经泛⻩，封⾯上⽤难以辨认的⽂字写着书名。翻开书⻚，⾥⾯似乎是关于古堡历史的记载'}],
        'exits':{'东':'Grand Hall'}  # 修改为简化的键
    },
    "Dining Room":{
        'name':'餐厅 (Dining Room）',
        'description':'你穿过拱形⽯⻔，来到了宽敞的餐厅。⻓⻓的橡⽊餐桌上布满了厚厚的灰尘，锈迹斑斑的银质餐具散落在桌⾯上，仿佛⼀场盛宴突然中断。墙壁上挂着巨⼤的狩猎场景油画，画布已经开始剥落。⻄⾯是通往⼤厅的拱形⽯⻔，北⾯是⼀扇破旧的⽊⻔，通向厨房。',
        'items':[{'餐桌上的银⾊烛台':'⼀个精致的银⾊烛台，上⾯镶嵌着⼀些宝⽯，但⼤部分已经脱落。'}],
        'exits':{'西':'Grand Hall','北':'Kitchen'}  # 修改为简化的键
    },
    "Kitchen":{
        'name':'厨房 (Kitchen)',
        'description':'你推开破旧的⽊⻔，进⼊了阴冷潮湿的厨房。腐烂的⽓味扑⿐⽽来，令⼈作呕。⽣锈的厨具散落在各处，巨⼤的壁炉已经冰冷，炉膛⾥堆满了⿊⾊的灰烬。南⾯是餐厅。地板中央，你注意到⼀块不寻常的⽊板，似乎可以移动，也许是⼀个隐蔽的活板⻔，通往地下。',
        'items':[
                 {'壁炉旁的⽕柴':'⼀盒潮湿的⽕柴，看起来还能⽤，也许可以点燃什么。'},
                 {'水槽边的水桶':'⼀个破旧的⽊⽔桶，⾥⾯积满了浑浊的⾬⽔。'}
                 ],
        'exits':{'南':'Dining Room','down':'Escape'}  # 修改为简化的键
    },
    "Escape":{
        "name": "地下通道",
        "description": "你成功逃离了古堡！",
        "items": [],
        "exits": {}
    }
}

#初始化房间和背包
current_room='Foyer'
inventory=[]

#处理玩家指令函数
def handle_input(command):
    messages=command.split()
    action=messages[0].lower()

    if action=='help':
        help_item()

    elif action=='look':
        describe_room(current_room)

    elif action=='go':
            direction=messages[1]
            move_player(direction)


    elif action=='take':

            item_name=messages[1]
            take_item(item_name)


    elif action=='inventory':
        show_inventory()

    elif action in ['quit', 'exit']:
        print("感谢游玩！再见！")
        exit()
    else:
        print("无效指令。请输入 help 查看可用指令。")
#help指令函数
def help_item():
    print("可⽤指令：")
    print("help - 显示帮助信息")
    print("look - 查看当前房间")
    print("go [⽅向] - 向指定⽅向移动 (北, 南, 东, 西, down)")
    print("take [物品名称] - 拾取物品")
    print("inventory - 查看背包")
    print("quit/exit - 退出游戏")

#显示房间描述
def describe_room(room_name):
    room=rooms[room_name]
    print(f"你身处{room['name']}")
    print(f"{room['description']}")
    if room["items"]:
        print("房间里有：")
        for item in room["items"]:
            for item_name, item_description in item.items():
                print(f"{item_name} {item_description}")
    else:
        print("房间里没有物品。")
    print("你可以向以下方向移动：")
    for direction, target in room["exits"].items():
        print(f"- {direction}（{target}）")

#移动玩家位置函数
def move_player(direction):
    global current_room
    if direction in rooms[current_room]["exits"]:
        current_room = rooms[current_room]["exits"][direction]
        if current_room == "Escape":
            print("你成功逃离了古堡！")
            exit()
        describe_room(current_room)

    else:
        print("那边没有路")

#处理拾取物品函数
def take_item(item_name):
    global current_room, inventory
    room=rooms[current_room]
    for item in room["items"]:
        if item_name in item:
            room["items"].remove(item)
            inventory.append(item)
            print(f"你拿起了 {item_name}。")
            return
    print(f"房间里没有 {item_name}。")

#查看背包函数
def show_inventory():
    if inventory:
        print('你的背包里有：')
        for item in inventory:
            for item_name, item_description in item.items():
                print(f"{item_name}  {item_description}")
    else:
        print('你的背包是空的。')

#主函数:主循环
def game_loop():
    print('欢迎来到“神秘的古堡”！')
    describe_room(current_room)
    while True:
        command = input('> ')
        handle_input(command)

# 启动游戏
game_loop()