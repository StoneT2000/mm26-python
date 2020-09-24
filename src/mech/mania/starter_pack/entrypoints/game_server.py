import sys

from flask import Flask, request
from mech.mania.engine.domain.model import character_pb2
from mech.mania.engine.domain.model import player_pb2
from mech.mania.starter_pack.domain.memory.memory_object import MemoryObject
from mech.mania.starter_pack.domain.model.game_state import GameState
from mech.mania.starter_pack.domain.strategy import Strategy


class GameServer:
    def __init__(self, url, port, testing_objects=None):
        self.url = url
        self.port = port
        self.debug = False
        self.memory = MemoryObject()
        self.strategy = Strategy(self.memory)

        if testing_objects is not None:
            self.atomicInt = testing_objects
            self.debug = True
        app = Flask(__name__)

        @app.route('/')
        def main_page():
            return "Welcome to MechMania26!"

        @app.route('/server', methods=['POST'])
        def send_decision():
            payload = request.get_data()

            player_turn = player_pb2.PlayerTurn()
            player_turn.ParseFromString(payload)

            print(f"Received playerTurn {player_turn.player_name}")

            game_state = GameState(player_turn.game_state)
            player_name = player_turn.player_name

            response_msg = character_pb2.CharacterDecision()

            try:
                decision = self.strategy.make_decision(player_name, game_state)
            except:
                print("Exception making decision: {0}".format(sys.exc_info()[0]))
                decision = None

            if decision is not None:
                response_msg = decision.build_proto_class_character_decision()
            else:
                # Build NONE decision if contestant code failed
                response_msg.decision_type = character_pb2.NONE
                response_msg.action_position = None
                response_msg.index = -1

            if self.debug:
                self.atomicInt.increment()

            print("Sending playerDecision")

            return response_msg.SerializeToString()

        @app.route('/shutdown', methods=['POST'])
        def shutdown():
            shutdown_server()
            return 'Server shutting down...'

        def shutdown_server():
            func = request.environ.get('werkzeug.server.shutdown')
            if func is None:
                raise RuntimeError('Not running with the Werkzeug Server')
            func()

        @app.route('/health')
        def health():
            return 200

        try:
            app.run(host=self.url, port=self.port)
        except Exception as e:
            print("Failed to start GameServer: " + e)


if __name__ == "__main__":
    url = sys.argv[1]
    port = int(sys.argv[2])
    GameServer(url, port)
