from typing import List

from config import ConfigInterface


class ArkLotteryZzConfig(ConfigInterface):
    def __init__(self):
        self.title = "集卡观赛两不误，战灵天舞套装、+11增幅券等你拿！"
        self.arkId = "1392_55"
        self.loginActId = "act_dnf_ark10"
        self.backActId = "act_dnf_xinyun4"
        self.actid = 4166
        self.actName = "dnf-ark10"
        self.gameid = "dnf"
        self.verifyid = "qqvipdnf10"
        self.isMobileGame = False
        self.gameInfo = ArkLotteryGameInfo()
        self.cardGroups = ArkLotteryCardGroups()
        self.prizeGroups = ArkLotteryPrizeGroups()
        self.quals = ArkLotteryQuals()
        self.rules = ArkLotteryRules()
        self.zZConfigerUpdateTime = 1607683661


class ArkLotteryGameInfo(ConfigInterface):
    def __init__(self):
        self.isMobile = 2
        self.androidSchema = "111"
        self.androidDown = "111"
        self.iosSchema = "111"
        self.iosDown = "111"


class ArkLotteryCardGroups(ConfigInterface):
    def __init__(self):
        self.group1 = ArkLotteryCardGroup()  # type: ArkLotteryCardGroup
        self.group2 = ArkLotteryCardGroup()  # type: ArkLotteryCardGroup
        self.group3 = ArkLotteryCardGroup()  # type: ArkLotteryCardGroup


class ArkLotteryCardGroup(ConfigInterface):
    def __init__(self):
        self.title = "全民竞速"
        self.cardList = []  # type: List[ArkLotteryCard]

    def fields_to_fill(self):
        return [
            ('cardList', ArkLotteryCard),
        ]


class ArkLotteryCard(ConfigInterface):
    def __init__(self):
        self.name = "巅峰大佬刷竞速"
        self.id = 118409
        self.prizeId = 44460
        self.lotterySwitchId = 28608


class ArkLotteryPrizeGroups(ConfigInterface):
    def __init__(self):
        self.group1 = ArkLotteryPrizeGroup()  # type: ArkLotteryPrizeGroup
        self.group2 = ArkLotteryPrizeGroup()  # type: ArkLotteryPrizeGroup
        self.group3 = ArkLotteryPrizeGroup()  # type: ArkLotteryPrizeGroup
        self.group4 = ArkLotteryPrizeGroup()  # type: ArkLotteryPrizeGroup


class ArkLotteryPrizeGroup(ConfigInterface):
    def __init__(self):
        self.title = "全民竞速礼包"
        self.rule = 28592
        self.qual = 118420
        self.backName = "act_dnf_huiliu4"
        self.backRule = 28595
        self.backQual = 118420


class ArkLotteryQuals(ConfigInterface):
    def __init__(self):
        self.lottery = 118424
        self.login = 118423
        self.share = 118422
        self.imback = 118412
        self.video = 118425
        self.mid1id = 118416
        self.mid2id = 118415


class ArkLotteryRules(ConfigInterface):
    def __init__(self):
        self.lottery = 28585
        self.login = 28613
        self.share = 28596
        self.imback = 28614
        self.video = 28616
        self.loginPage = 28615
        self.lotteryByCard = 28584
        self.midRule1 = 28610
        self.midRule2 = 28609
        self.midBack1 = 28612
        self.midBack2 = 28611
