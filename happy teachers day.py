import time
import random
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

bouquet = r"""
      .-.
     /   \      🌸
    |     |   🌼  🌺
     \   /     🌸
      `-’
     _|=|_
    |_____|   Here's a bouquet for you, Ma'am!
"""

quotes = [
    "A good teacher is like a candle—it consumes itself to light the way for others.",
    "Teaching is the one profession that creates all other professions.",
    "The influence of a great teacher can never be erased.",
    "To the world, you may be just a teacher, but to your students, you are a hero.",
    "Teachers plant the seeds of knowledge that last a lifetime."
]

student_messages = [
    "Anshul: Your lessons were more than just subjects — they were life lessons.",
    "Viraaj: You made learning fun and meaningful. Happy Teacher's Day!",
    "Anuska: Thank you for always being so kind and supportive, Ma’am.",
    "Ayaan: Your encouragement gave me confidence. Grateful for you always!",
    "Aarav: You saw potential in me when I couldn’t see it myself.",
    "Navatej: You’ve been a guiding light, and I’ll always remember your wisdom."
]



poem = """
You guided us when we were lost,  
You supported us when we were weak,  
You believed in us when we doubted ourselves.  
For all of this, and so much more —  
Thank you, Swathi Ma’am. 💖
"""

def welcome():
    clear()
    print("✨✨✨ WELCOME ✨✨✨")
    print("Loading your Digital Teacher's Day Gift...\n")
    time.sleep(2)

def show_bouquet():
    clear()
    print(bouquet)
    time.sleep(3)

def show_message():
    clear()
    print("🌟 Happy Teacher’s Day, Swathi Ma’am! 🌟\n")
    time.sleep(1)
    print("Thank you for being an incredible teacher, mentor, and inspiration.")
    time.sleep(1)
    print("We made this little digital gift just for you 💝\n")
    time.sleep(2)

def show_student_messages():
    clear()
    print("💌 Messages from your Students 💌\n")
    for msg in student_messages:
        print(f"• {msg}")
        time.sleep(1)
    input("\n(Press Enter to continue...)")

def show_poem():
    clear()
    print("📜 A Poem for You:\n")
    print(poem)
    input("\n(Press Enter to continue...)")

def surprise_box():
    clear()
    print("🎁 Unwrapping Your Surprise Box...\n")
    time.sleep(2)
    print("You got a random quote!\n")
    print("💬", random.choice(quotes))
    input("\n(Press Enter to finish the gift...)")

def final_message():
    clear()
    print("🎉 Thank you for everything, Swathi Ma’am! 🎉")
    print("We love and appreciate you more than words can say.\n")
    print("Wishing you a joyful Teacher’s Day! 🥰")
    print("\nWith love,")
    print("— Your Students 💐")
    print("\n(You may now close the gift box 😊)")

def digital_gift():
    welcome()
    show_bouquet()
    show_message()
    show_student_messages()
    show_poem()
    surprise_box()
    final_message()

if __name__ == "__main__":
    digital_gift()
