class StateMachine:
    STATES = ['IDLE', 'DECODING', 'QTE', 'ESCAPE']

    def get_state(self, frame):
        # 基于CV分析返回当前状态
        if self._detect_qte(frame):
            return 'QTE'
        elif self._detect_cipher(frame):
            return 'DECODING'
        return 'IDLE'

    def get_actions(self, state):
        return {
            'DECODING': [
                {'type': 'key_press', 'key': 'e', 'duration': 0.5},
                {'type': 'move', 'x': 800, 'y': 600}
            ],
            'QTE': [
                {'type': 'click', 'x': 960, 'y': 540, 'clicks': 3}
            ]
        }[state]