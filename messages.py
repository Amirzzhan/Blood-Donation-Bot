def greeting_message() -> str:
    return "Blood donation is one of the noblest deeds that man can do. A donor gives some part of himself to save " \
           "a life. Therefore, it is important to be utterly ready for this journey. Let us help you to become a hero!"


def ask_for_ready() -> list:
    return [
        "You can select an item from the menu to continue👇",
        "You can check your donor eligibility by pressing the 'Check your eligibility for blood donation ✅'.",
        "Stay informed! Read Articles 📖 to learn more about blood donation and its impact.",
        "Don't miss out on Upcoming events 🎉! Join our blood donation drives and save lives."
    ]



def question1() -> str:
    return "1) Вам есть 18 лет?"


def fail_question() -> str:
    return "We are sorry to inform you about your ineligibility for blood donation. However, those questions are " \
           "time-based; therefore, you can donate blood at the Astana blood center whenever the restricted time period" \
           " passes and you will be ready!"


def question2() -> str:
    return "2) Ваш вес больше 50?"


def fail_question2() -> str:
    return "Извините но мы не можем брать кровь у тех у кого вес меньше 50"


def success() -> str:
    return "Поздравляю!, вы нам подходите!🥳🥳🥳 \nСвяжитесь с членами Red Crescent Club по дальнейшим вопросам"


def send_status(user) -> str:
    return "Йо Аброр челик {} {} @{} готов к донорству".format(user.first_name, user.last_name, user.username)


def learn_more() -> str:
    return "Learn more on our instagram page: @nu_red_crescent"


def articles() -> str:
    return "More about blood donation:\n" \
           "1. Nutrition of the donor\n" \
           "2. Main benefits of blood donation\n" \
           "3. Breaking stereotypes: why you don’t donate blood\n" \
           "4. Who cannot donate blood? Contraindications\n" \
           "5. What will happen to the donor’s blood?\n" \
           "6. Frequently asked questions"


def upcoming_events_text() -> str:
    return str('NU Red Crescent Society announces «Blood Drive»🩸🚗\n\n' +
               'Our club invites you to celebrate Thematic Halloween in a meaningful way ➡️ donate blood to help '
               'patients survive surgeries and traumatic injuries📢\n\n' +
               '🖤 Come with a friend and share not just the spooky vibes but also the gift of life.🧛‍♀️🩸\n\n' +
               'There will also be a photo-zone where you can take pictures and create memories of your university '
               'life.\n\n' +
               '🗓Date: 30-31 October, 10 AM-3 PM\n' +
               '📍Venue: NU Main Atrium\n' +
               '🩸All blood types are eligible!\n' +
               '🧷 <a href="https://docs.google.com/forms/d/1hMkwbShnw2sa8krxVek0zqJRZvQJdhKBHyLY9HoWprw/edit'
               '">👻 Sign up now: Registration link</a>\n\n')
