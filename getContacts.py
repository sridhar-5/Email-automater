def getContacts():
    names = []
    emails = []

    #reading both the files
    namesFile = open("names.txt", "r")
    for eachName in namesFile:
        name = eachName.split("\n")
        names.append(name[0])

    emailsFile = open("mails.txt")
    for eachEmail in emailsFile:
        email = eachEmail.split("\n")
        emails.append(email[0])

    return names,emails
