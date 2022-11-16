class EmailData:
    def __init__(self, sender, receiver , content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True


    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"

e_mails_data = []
e_mail_data = input()

while e_mail_data != "Stop":
    sender, receiver, content = e_mail_data.split()
    current_email = EmailData(sender, receiver, content)
    e_mails_data.append(current_email)
    e_mail_data = input()


sent_e_mails_indices = input().split(", ")
sent_e_mails_indices = [int(index) for index in sent_e_mails_indices]

for index_to_send in sent_e_mails_indices:
    current_email_data = e_mails_data[index_to_send]
    current_email_data.send()

for current_email_data in e_mails_data:
    print(current_email_data.get_info())