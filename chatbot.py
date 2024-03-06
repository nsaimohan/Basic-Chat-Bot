from nltk.chat.util import Chat,reflections
pairs=[
    [r'hi',["Hey! How is it going?...What's up?"]],
    [r'how are you',["I'm doing great,thanks for asking! Just here,ready to chat. How about you? How are you doing?😊"]],
    [r'are you ok',["Yes I'm ok! Tell me How can I Help You??"]],
    [r'I love you',["Aww! That's so sweet!❤️,I too love me!!"]],
    [r'had your lunch',["I dont eat anything because i am machine"]],
    [r'tell me a joke',[" A joke is a joke that is used to laugh  ..... "]],
]
chat=Chat(pairs,reflections)
chat.converse()
