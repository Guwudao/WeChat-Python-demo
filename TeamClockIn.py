
import re

leader_list = ['许月英', '苟肖朋', '苏俊', '周亚', '朱纯佳', '张璐', '胡超', '赖淑茹', '林俊杰', '李凯', '陈少轩', '杨佳', '田晶/王杨', '刘昌旭', '赵得华', '谢研', '候梦璇', '王腾/林健卜']

team_list = ['WeChat', 'Staff', 'Payment', 'China', 'GBA', 'MVTM', 'Mobile', 'Saa', 'MobileX', 'MobilexX', 'Apollo', 'API', 'SMP', 'louis', 'cca', 'GBA', 'MobileR', 'GBA']

def unclock_list(today):

    result_list = []
    for team, leader in zip(team_list, leader_list):
        if leader not in today:
            unclock = team + " " + leader
            result_list.append(unclock)
            # print(unclock)

    index = today.index("1.")
    new_today = today[index:]
    today_list = new_today.split("\n")
    sum = 0
    for t in today_list:
        start_index = t.index(".")
        team_sp = t[start_index+1:]
        # print(team_sp)
        num = re.findall(r"\d+\.?\d*", team_sp)
        sum += int(num[len(num)-1])
        # print(num[len(num)-1])

    print("打卡总人数：" + str(sum))
    print(result_list)
    return (result_list, sum)