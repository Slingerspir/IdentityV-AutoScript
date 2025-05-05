import random
import time

class AntiBanSystem:
    HUMAN_LIKE_PARAMS = {
        'move_speed_variance': 0.2,
        'click_offset': 15
    }

    @staticmethod
    def random_trajectory(start, end):
        # 生成带有随机偏移的移动路径
        control_point = (
            (start[0] + end[0])/2 + random.randint(-50,50),
            (start[1] + end[1])/2 + random.randint(-50,50)
        )
        return [start, control_point, end]

    @classmethod
    def get_random_delay(cls, base=0.3):
        return base * (1 + random.uniform(-0.2, 0.2))