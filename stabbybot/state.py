# -*- coding: utf-8 -*-

#
# stabbybot comm
# https://github.com/vesche/stabbybot
#

class GameState():
    def __init__(self):
        self.game_state = {
            'perception': [],
            'kill_info': {'uid': None, 'x': None, 'y': None, 'killer': None},
            'dead': False
        }

    def perception(self, data):
        self.game_state['perception'] = []

        data = data.split('|')
        data.pop()
        for i in data:
            uid, x, y, status, direction = i.split(',')
            self.game_state['perception'].append(
                {'uid': uid, 'x': x, 'y': y, 'status': status, 'direction': direction}
            )

    def kill_info(self, data):
        uid, x, y, killer = data.split(',')
        self.game_state['kill_info'] = {'uid': uid, 'x': x, 'y': y, 'killer': killer}
    
    def killed_by(self, data):
        self.game_state['dead'] = True