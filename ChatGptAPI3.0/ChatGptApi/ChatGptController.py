from ChatGptApi.ChatGpt import ChatGpt
from ChatGptApi.ChatGptService import ChatGptService
from flask import Flask
from flask import request

app = Flask(__name__)


class ChatGptController:
    def __init__(self):
        self.app = app
        self.service = ChatGptService(chatgpt=ChatGpt())
        self.add_routes()

    def add_routes(self):
        @app.route('/api/message', methods=['POST'])
        def send():
            message = request.get_json()['message']
            return self.service.send(message=message)

        @app.route('/api/getallreplies', methods=['GET'])
        def get_all_replies():
            return self.service.get_all_replies()

        @app.route('/api/repling', methods=['GET'])
        def repling():
            return self.service.repling()

        @app.route('/api/getlastreply', methods=['GET'])
        def get_last_reply():
            return self.service.get_last_reply()

        @app.route('/api/getallchat', methods=['GET'])
        def get_all_chat():
            return self.service.get_all_chat()

        @app.route('/api/choosechat', methods=['POST'])
        def choose_chat():
            ref = request.get_json()['ref']
            return self.service.choose_chat(ref=ref)

        @app.route('/api/deletechat', methods=['GET'])
        def delete_chat():
            return self.service.delete_chat()

        @app.route('/api/renamechat', methods=['POST'])
        def rename_chat():
            name = request.get_json()['name']
            return self.service.rename_chat(name=name)

        @app.route('/api/newchat', methods=['GET'])
        def new_chat():
            return self.service.new_chat()

        @app.route('/api/reload', methods=['GET'])
        def reload():
            return self.service.reload()
