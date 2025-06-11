#!/usr/bin/env python3

def send_email(to_address,subject = "Email", body = ""):
    print("Recipient:",to_address)
    print("Subject:",subject)
    print("Body:",body)

send_email("demo@redhat.com")
send_email("demo@redhat.com",subject="Reminder",body="Reminder email")
