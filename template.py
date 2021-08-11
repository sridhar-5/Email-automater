from string import Template

def readTemplate():
    MessageFile = open("message.txt","r")
    MessageFileContent = MessageFile.read()

    #returning the template object made from the content of the message file
    return Template(MessageFileContent)