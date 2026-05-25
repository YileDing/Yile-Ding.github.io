import random

class CollegeSimulator:
    def __init__(self):
        self.gpa = 50
        self.health = 50
        self.mental = 50
        self.social = 10
        self.money = 500
        self.month = 1
        self.total_months = 24
        self.scholarship = False
        self.dropped_out = False
        self.recruited = False

        self.options = {
            '1': {
                'name': '去图书馆学习',
                'events': [
                    ("你在图书馆偶遇了一位教授，他给了你一些学习建议。", 3, 0, -1, 0, 0),
                    ("你找到了一本非常有用的参考书，学习效率大幅提升。", 4, 0, -1, 0, 0),
                    ("你在图书馆认识了一个学习伙伴，你们一起学习进步很快。", 4, 0, -2, 1, 0),
                    ("你熬夜学习，第二天感到非常疲惫。", 2, -3, -2, 0, 0)
                ]
            },
            '2': {
                'name': '去健身房锻炼',
                'events': [
                    ("你参加了校园运动会，获得了跑步比赛的奖项。", 0, 1, 1, 0, 0),
                    ("你在健身房遇到了一位专业教练，他给了你一些锻炼建议。", 0, 3, 0, 0, 0),
                    ("你坚持锻炼，身体素质明显提高。", -1, 2, 0, 0, 0),
                    ("你在锻炼时不小心受伤了，需要休息几天。", -2, -3, -1, 0, 0)
                ]
            },
            '3': {
                'name': '参加社团活动',
                'events': [
                    ("你加入了一个社团，认识了很多新朋友。", 0, 0, 1, 0, -30),
                    ("你在社团活动中表现出色，被选为社团干部。", -1, 0, 0, 2, 0),
                    ("社团组织了一次公益活动，你收获了很多。", 0, 1, 1, 1, -50),
                    ("社团活动占用了太多时间，你感到有些疲惫。", -2, -2, -2, 0, -20)
                ]
            },
            '4': {
                'name': '和朋友出去玩',
                'cost': 150,
                'events': [
                    ("你和朋友出去旅游，放松了心情。", -2, 0, 2, 0, -300),
                    ("你和朋友参加了一个派对，玩得很开心。", 0, 0, 1, 0, -150),
                    ("你和朋友一起看了一场精彩的电影，心情愉悦。", 0, 0, 1, 0, -100),
                    ("你和朋友玩得太晚，第二天感到疲惫。", -2, -2, 1, 0, -200)
                ]
            },
            '5': {
                'name': '做兼职工作',
                'events': [
                    ("你在兼职工作中表现出色，得到了晋升。", 0, 0, 1, 4, 500),
                    ("你在兼职工作中学习到了很多实用技能。", 0, 0, 0, 3, 300),
                    ("你通过兼职工作认识了一些行业人士，拓展了人脉。", 0, 0, 0, 3, 400),
                    ("兼职工作太累了，影响了你的学习和休息。", -3, -2, -2, 2, 200)
                ]
            },
            '6': {
                'name': '休息一天',
                'events': [
                    ("你好好休息了一天，精神焕发。", 1, 1, 2, 0, 0),
                    ("你在家看了一本好书，增长了见识。", 2, 0, 1, 0, 0),
                    ("你整理了房间，心情变得更加舒畅。", 1, 1, 2, 0, 0),
                    ("你整天无所事事，感到有些无聊。", 0, -1, -2, 0, 0)
                ]
            }
        }

    def get_progress_bar(self, value, label, bar_char='#'):
        bar_length = 20
        percent = value / 100
        filled_length = int(bar_length * percent)
        bar = bar_char * filled_length + '-' * (bar_length - filled_length)
        return f"{label}: [{bar}] {value}"

    def display_status(self):
        print(f"\n=== 第 {self.month} 月 ===")
        print(self.get_progress_bar(self.gpa, "学习成绩"))
        print(self.get_progress_bar(self.health, "身体健康"))
        print(self.get_progress_bar(self.mental, "心理健康"))
        print(self.get_progress_bar(self.social, "社会实践"))
        print(f"金钱: {self.money} 元")

        if self.scholarship:
            print("  [获得奖学金]")
        if self.recruited:
            print("  [已被单招]")

    def display_options(self):
        print("\n请选择本月要做的事情:")
        for key, option in self.options.items():
            cost_info = ""
            if key == '4' and option.get('cost'):
                cost_info = f" (需要{option['cost']}元)"
            print(f"{key}. {option['name']}{cost_info}")

    def get_player_choice(self):
        while True:
            choice = input("请输入选项编号(1-6): ")
            if choice not in self.options:
                print("无效选项，请重新输入")
                continue

            if choice == '4':
                cost = self.options['4'].get('cost', 150)
                if self.money < cost:
                    print(f"金钱不足！你只有{self.money}元，需要{cost}元才能出去玩。")
                    print("请选择其他活动或先做兼职赚钱。")
                    continue

            return choice

    def apply_event(self, event):
        description, gpa_delta, health_delta, mental_delta, social_delta, money_delta = event
        print(f"\n{description}")

        old_gpa = self.gpa
        old_health = self.health
        old_mental = self.mental
        old_social = self.social
        old_money = self.money

        self.gpa = max(0, min(100, self.gpa + gpa_delta))
        self.health = max(0, min(100, self.health + health_delta))
        self.mental = max(0, min(100, self.mental + mental_delta))
        self.social = max(0, min(100, self.social + social_delta))
        self.money = max(0, self.money + money_delta)

        print(f"学习成绩: {old_gpa} -> {self.gpa}")
        print(f"身体健康: {old_health} -> {self.health}")
        print(f"心理健康: {old_mental} -> {self.mental}")
        print(f"社会实践: {old_social} -> {self.social}")
        if money_delta != 0:
            print(f"金钱: {old_money} -> {self.money}")

    def monthly_expenses(self):
        expense = random.randint(200, 400)
        self.money -= expense
        print(f"\n本月生活开支: -{expense}元")
        print(f"剩余金钱: {self.money}元")

        if self.money < 0:
            print("\n[警告] 你的金钱为负数！需要尽快做兼职赚钱！")

    def monthly_subsidy(self):
        subsidy = 300
        self.money += subsidy
        print(f"\n本月生活补贴: +{subsidy}元")

    def check_monthly_events(self):
        if not self.scholarship and self.gpa > 80 and self.health > 70:
            self.scholarship = True
            self.money += 1000
            print("\n[喜报] 恭喜！由于你学习成绩优秀且身体健康，获得了奖学金1000元！")

        if not self.recruited and self.social > 80:
            self.recruited = True
            print("\n[喜报] 恭喜！由于你社会实践丰富，被大企业提前单招录取！")

        if not self.dropped_out and (self.health < 20 or self.mental < 20):
            self.dropped_out = True
            print("\n[警告] 你的身体或心理健康状况过低，需要休学治疗！")
            return False

        return True

    def calculate_final_score(self):
        weights = [0.35, 0.25, 0.25, 0.15]
        final_score = (self.gpa * weights[0] +
                       self.health * weights[1] +
                       self.mental * weights[2] +
                       self.social * weights[3])
        return final_score

    def get_ending(self, final_score):
        if final_score >= 85:
            return "[完美结局] 你成为了一名全面发展的优秀毕业生，获得了校优秀毕业生称号！"
        elif final_score >= 70:
            return "[良好结局] 你顺利毕业，并找到了一份理想的工作！"
        elif final_score >= 55:
            return "[普通结局] 你顺利完成了学业，开始规划未来的人生道路。"
        elif final_score >= 40:
            return "[勉强结局] 你勉强毕业了，但需要更加努力才能实现自己的目标。"
        else:
            return "[遗憾结局] 你的大学生活并不理想，需要反思和改进。"

    def show_intro(self):
        print("=" * 50)
        print("          大学生活模拟器")
        print("=" * 50)
        print()
        print("    开启你的大学生活之旅！")
        print()
        print("=" * 50)
        print("【游戏简介】")
        print("  你将扮演一名大学生，在24个月的时间里")
        print("  做出各种选择，平衡学业、健康和社交。")
        print()
        print("【四项属性】")
        print("  [书] 学习成绩 - 初始: 50")
        print("  [心] 身体健康 - 初始: 50")
        print("  [脑] 心理健康 - 初始: 50")
        print("  [人] 社会实践 - 初始: 10")
        print("  [钱] 金钱     - 初始: 500元")
        print()
        print("【每月收支】")
        print("  - 生活补贴: +300元/月")
        print("  - 生活开支: -200~400元/月")
        print("  - 和朋友出去玩需要150元")
        print("  - 做兼职可获得200~500元")
        print()
        print("【特殊事件】")
        print("  [奖] 奖学金: 学习>80 且 健康>70 (+1000元)")
        print("  [休] 休学: 健康<20 或 心理<20")
        print("  [聘] 单招: 社会实践>80")
        print()
        print("【游戏目标】")
        print("  平衡发展，追求完美结局！")
        print("=" * 50)
        input("  按回车键开始游戏...")
        print()

    def play(self):
        self.show_intro()

        print("游戏开始！")
        print("在接下来的24个月里，你将面临各种选择。")
        print("每个选择都会随机触发一个事件，影响你的各项属性。")
        print("注意管理你的金钱，没钱就没法出去玩哦！")
        print("祝你好运！\n")

        while self.month <= self.total_months:
            self.display_status()
            self.display_options()
            choice = self.get_player_choice()

            option = self.options[choice]
            event = random.choice(option['events'])
            self.apply_event(event)

            if not self.check_monthly_events():
                break

            self.monthly_subsidy()
            self.monthly_expenses()

            self.month += 1
            if self.month <= self.total_months:
                input("\n按回车键进入下一个月...")

        print("\n=== 游戏结束 ===")

        if self.dropped_out:
            print("[休学结局] 由于身体或心理健康问题，你不得不休学。请好好休养，期待你早日回归校园！")
            return

        print("最终状态:")
        print(f"学习成绩: {self.gpa}")
        print(f"身体健康: {self.health}")
        print(f"心理健康: {self.mental}")
        print(f"社会实践: {self.social}")
        print(f"金钱: {self.money}元")

        if self.scholarship:
            print("\n[成就] 获得奖学金")
        if self.recruited:
            print("[成就] 被大企业单招录取")

        final_score = self.calculate_final_score()
        print(f"\n最终成绩: {final_score:.2f}")

        ending = self.get_ending(final_score)
        if self.recruited:
            ending = "[单招结局] 恭喜！你被大企业提前录取，直接开启职业生涯！"
        print(ending)

if __name__ == "__main__":
    game = CollegeSimulator()
    game.play()