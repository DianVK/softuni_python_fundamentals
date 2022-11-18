class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


all_emails = []
receive_emails = input()

while receive_emails != "Stop":
    seder, receiver, content = receive_emails.split()
    current_email = Email(seder, receiver, content)
    all_emails.append(current_email)
    receive_emails = input()

send_emails_index = [int(num) for num in input().split(", ")]
for index in send_emails_index:
    all_emails[index].send()

for mail in all_emails:
    print(f"{mail.get_info()}")