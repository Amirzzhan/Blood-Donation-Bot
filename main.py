import telebot
import messages
import keyboard
import time
from decouple import config
from telebot.types import InputFile

# Load bot token and admin chat ID from environment variables
TOKEN = config('TELEGRAM_BOT_TOKEN')
admin_chat_id = config('ADMIN_CHAT_ID')
print(f"TOKEN: {TOKEN}")


# Dictionary to store user IDs and their questions
user_questions = {}


@bot.message_handler(commands=['get_admin_id'])
def get_admin_id(message):
    # This will send the chat_id of the admin to the bot
    bot.send_message(message.chat.id, f"Your chat ID is: {message.chat.id}")


@bot.message_handler(commands=['test_admin'])
def test_admin(message):
    try:
        bot.send_message(admin_chat_id, "Testing message to admin!")
        bot.send_message(message.chat.id, "Message sent to admin successfully!")
    except Exception as e:
        bot.send_message(message.chat.id, f"Error: {e}")


@bot.message_handler(commands=['start'])
def start_command(message):
    # Send greeting message
    bot.send_message(message.chat.id, messages.greeting_message())
    # Looping through each message in ask_for_ready() and sending them separately
    for ready_message in messages.ask_for_ready():
        bot.send_message(message.chat.id, ready_message)
    # Sending the keyboard after the messages
    bot.send_message(message.chat.id, "Choose an option:", reply_markup=keyboard.start_keyboard())


@bot.message_handler(commands=['q'])
def handle_question(message):
    user = message.from_user
    question = message.text[len('/q '):]  # Extract the question text after /q

    # Store the user ID and the question for future reference
    user_questions[user.id] = message.chat.id
    print(f"Stored user: {user.id}, chat_id: {message.chat.id}")

    # Forward the question to admin with user details
    bot.send_message(admin_chat_id,
                     f"New question from @{user.username} (ID: {user.id}, Name: {user.first_name}):\n{question}")

    # Notify the user that their question has been received
    bot.send_message(message.chat.id, "Your question has been sent to the admin. You will receive a reply soon.")


@bot.message_handler(commands=['answer'])
def handle_admin_answer(message):
    parts = message.text.split(maxsplit=2)  # Split the command text
    if len(parts) < 3:
        bot.send_message(message.chat.id, "Usage: /answer [user_id] [response]")
        return

    user_id = int(parts[1])  # Retrieve user ID
    response = parts[2]  # Admin's response message

    # Send admin's response to the original user if the user ID exists in the stored questions
    if user_id in user_questions:
        user_chat_id = user_questions[user_id]  # Retrieve the original user's chat ID
        bot.send_message(user_chat_id, f"Admin has replied to your question:\n{response}")
        # Notify admin that the response has been sent
        bot.send_message(message.chat.id, f"Your answer has been sent to the user (ID: {user_id}).")
    else:
        # If the user ID is not found, notify the admin
        bot.send_message(message.chat.id, f"User ID {user_id} not found.")


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    data = call.data
    last_message_id = call.message.message_id

    if data == 'other_posts':
        bot.send_message(call.from_user.id, messages.articles(), reply_markup=keyboard.articles())

    if data == 'Fail':
        bot.edit_message_reply_markup(call.from_user.id, message_id=last_message_id, reply_markup=None)
        time.sleep(0.5)
        bot.send_message(call.from_user.id, messages.fail_question())

    if data == 'post1':
        bot.send_message(call.from_user.id, 'Nutrition of the donor:'
                                            'https://www.instagram.com/p/CZRwz49sinF/?igshid=YmMyMTA2M2Y=', reply_markup=keyboard.articles_others())

    if data == 'post2':
        bot.send_message(call.from_user.id, 'Main benefits of blood donation : \n\nhttps://www.instagram.com/p/CKBp5ZxHqj_/?igshid=YmMyMTA2M2Y=', reply_markup=keyboard.articles_others())

    if data == 'post3':
        bot.send_photo(call.from_user.id, InputFile('img/post3.jpg'), caption="Breaking stereotypes", reply_markup=keyboard.articles_others())

    if data == 'post4':
        bot.send_photo(call.from_user.id, InputFile('img/post4.jpg'), caption="Contraindications", reply_markup=keyboard.articles_others())

    if data == 'post5':
        bot.send_photo(call.from_user.id, InputFile('img/post5.jpg'), caption="What will happen to the donor’s blood", reply_markup=keyboard.articles_others())

    if data == 'post6':
        bot.send_photo(call.from_user.id, InputFile('img/faq1.jpg'))
        bot.send_photo(call.from_user.id, InputFile('img/faq2.jpg'))
        bot.send_photo(call.from_user.id, InputFile('img/faq3.jpg'))
        bot.send_photo(call.from_user.id, InputFile('img/faq4.jpg'), reply_markup=keyboard.articles_others())

    if data == 'go_question2':
        bot.edit_message_reply_markup(call.from_user.id, message_id=last_message_id, reply_markup=None)
        time.sleep(0.5)
        bot.send_message(call.from_user.id, "Is your weight 50 kg and higher?", reply_markup=keyboard.question2())

    if data == 'go_question3':
        bot.edit_message_reply_markup(call.from_user.id, message_id=last_message_id, reply_markup=None)
        time.sleep(0.5)
        bot.send_message(call.from_user.id, "I have not consumed alcohol in 48 hours", reply_markup=keyboard.question3())

    if data == 'go_question4':
        bot.edit_message_reply_markup(call.from_user.id, message_id=last_message_id, reply_markup=None)
        time.sleep(0.5)
        bot.send_message(call.from_user.id, "I have not smoked for 2 hours", reply_markup=keyboard.question4())

    if data == 'go_question5':
        bot.edit_message_reply_markup(call.from_user.id, message_id=last_message_id, reply_markup=None)
        time.sleep(0.5)
        bot.send_message(call.from_user.id, "It’s been 5 days since my period (for girls)", reply_markup=keyboard.question5())

    if data == 'go_question6':
        bot.edit_message_reply_markup(call.from_user.id, message_id=last_message_id, reply_markup=None)
        time.sleep(0.5)
        bot.send_message(call.from_user.id, "I haven’t been vaccinated for 2 weeks", reply_markup=keyboard.question6())

    if data == 'go_question7':
        bot.edit_message_reply_markup(call.from_user.id, message_id=last_message_id, reply_markup=None)
        time.sleep(0.5)
        bot.send_message(call.from_user.id, "I haven’t had a tattoo/piercing in 6 months", reply_markup=keyboard.question7())

    if data == 'go_question8':
        bot.edit_message_reply_markup(call.from_user.id, message_id=last_message_id, reply_markup=None)
        time.sleep(0.5)
        bot.send_message(call.from_user.id, "I haven’t had a tooth removed in the last 10 days", reply_markup=keyboard.question8())

    if data == 'go_question9':
        bot.edit_message_reply_markup(call.from_user.id, message_id=last_message_id, reply_markup=None)
        time.sleep(0.5)
        bot.send_message(call.from_user.id, "It was one month since the recovery of my flu/sore throat", reply_markup=keyboard.question9())

    if data == 'go_question10':
        bot.edit_message_reply_markup(call.from_user.id, message_id=last_message_id, reply_markup=None)
        time.sleep(0.5)
        bot.send_message(call.from_user.id, "I haven’t been allergic for 2 months", reply_markup=keyboard.question10())

    if data == 'go_question11':
        bot.edit_message_reply_markup(call.from_user.id, message_id=last_message_id, reply_markup=None)
        time.sleep(0.5)
        bot.send_message(call.from_user.id, "I didn’t consume eggs, dairy products, smoked, spicy and fatty products the day before donation", reply_markup=keyboard.question11())

    if data == 'success':
        bot.edit_message_reply_markup(call.from_user.id, message_id=last_message_id, reply_markup=None)
        time.sleep(0.5)
        bot.send_message(call.from_user.id, "Congratulations! 🎉🎉🎉 You are eligible to donate blood based on common"
                                            " requirements! Now check our check-list to see permanent contraindications"
                                            " and make sure you are utterly ready to become a hero! Other than that "
                                            "welcome to our family of blood donors! If you have specific questions, "
                                            "choose the ASK QUESTION item on menu.")


@bot.message_handler(func=lambda message: True)
def message_handler(message):
    if message.text == "Check your eligibility for blood donation ✅":
        bot.send_message(message.chat.id, "Are you 18 years old or above?", reply_markup=keyboard.question1())
    if message.text == 'Articles 📖':
        bot.send_message(message.chat.id, messages.articles(), reply_markup=keyboard.articles())
    if message.text == 'Ask a question ❓':
        bot.send_message(message.chat.id, "Please, start your question with command /q")
        bot.send_message(message.chat.id, "for example: '/q How can I contact member of Red Crescent Club?'")
    if message.text == 'Upcoming events 🎉':
        bot.send_photo(message.chat.id, InputFile('img/poster.PNG'), messages.upcoming_events_text(), parse_mode='HTML')


bot.polling()
