# 🎉 Automatic Birthday Email Sender

This project automatically sends personalized birthday emails using Python. It reads birthdays from a CSV file, selects a random email template, and sends a customized greeting to the person whose birthday is today.

---

## 🛠 Features

- Automatically checks for birthdays from a CSV file.
- Sends personalized birthday emails.
- Randomly selects one of multiple email templates for variety.
- Uses Gmail SMTP for sending emails.

---

## ⚙️ How It Works

1. Store birthdays in a CSV file with columns: `name`, `email`, `year`, `month`, `day`.
2. Prepare 1–3 text templates in the `letter_templates` folder. Use `[NAME]` as a placeholder for the recipient's name.
3. The script checks if today matches any birthday.
4. If a match is found:
   - Randomly selects a template.
   - Replaces `[NAME]` with the recipient's name.
   - Sends the email via Gmail SMTP.

---

## 📁 File Structure

