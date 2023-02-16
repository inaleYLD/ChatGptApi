from flask import jsonify


class ChatGptService:
    def __init__(self, chatgpt):
        self.chatgpt = chatgpt

    def send(self, message):
        chatgpt = self.chatgpt
        if chatgpt.send(message=message):
            return jsonify({"result": "Message sent successfully"})
        else:
            return jsonify({"result": "Message sent failed"})

    def get_all_replies(self):
        return jsonify({'result': self.chatgpt.get_all_replies()})

    def repling(self):
        return jsonify({'result': self.chatgpt.repling()})

    def get_last_reply(self):
        return jsonify({'result': self.chatgpt.get_last_reply()})

    def get_all_chat(self):
        return jsonify({'result': self.chatgpt.get_all_chat()})

    def choose_chat(self, ref):
        if self.chatgpt.choose_chat(ref=ref):
            return jsonify({'result': "Choose succeeded"})
        else:
            return jsonify({'result': "Choose failed"})

    def delete_chat(self):
        if self.chatgpt.delete_chat():
            return jsonify({'result': "Delete chat succeeded"})
        else:
            return jsonify({'result': "Delete chat failed"})

    def rename_chat(self, name):
        if self.chatgpt.rename_chat(name=name):
            return jsonify({'result': "Rename chat succeeded"})
        else:
            return jsonify({'result': "Rename chat failed"})

    def new_chat(self):
        if self.chatgpt.new_chat():
            return jsonify({'result': "New build chat succeeded"})
        else:
            return jsonify({'result': "New build chat failed"})

    def reload(self):
        self.chatgpt.open()
        return jsonify({'result': "Reload succeeded"})
