from instagrapi import Client
import random
import time
import os

def print_banner():
    banner = """
\033[91m
oooooo   oooo ooooooooo.                     ooooo   .oooooo.         
 `888.   .8'  `888   `Y88.                   `888'  d8P'  `Y8b        
  `888. .8'    888   .d88'                    888  888                
   `888.8'     888ooo88P'                     888  888                
    `888'      888`88b.         8888888       888  888     ooooo      
     888       888  `88b.                     888  `88.    .88'       
    o888o     o888o  o888o                   o888o  `Y8bood8P'        
\033[0m                                                                 
                                                                                            
    """
    print(banner)

username = "_yrdestination"
password = "YRdesti@408"
client = Client()
#client.set_user_agent("Instagram 123.0.0.26.121 Android (28/9; 320dpi; 720x1280; Xiaomi; Redmi 6; 1234567; en_US)")
print("\033[93m            Logging in.............\033[0m")
client.login(username, password)
print(" \033[92m              Login Completed !\033[0m")
print("\033[95m            Welcome YR Destination!!!\033[0m")



hashtags_list = [
    "nature", "travel", "photography", "girlsfashion", "beautifulgirls", 
    "food", "lovecouples", "explore", "wanderlust", "adventure", 
    "vacation", "instatravel", "travelgram", "beautifuldestinations", 
    "wanderer", "naturelovers", "sunset", "sunrise", "landscape",
    "scenic", "travelphotography", "naturephotography", "wildlife", 
    "outdooradventures", "adventuretime", "roadtrip", "backpacking", 
    "couplegoals", "travelcouple", "mountainlife", "beachlife", 
    "islandvibes", "luxurytravel", "vacationmode", "cityscape", 
    "urbanexplorer", "exploretheworld", "hiking", "naturewalks", 
    "campinglife", "oceanside", "paradise", "love", "instalove", 
    "romanticplaces", "adventurecouple", "coupleadventures", 
    "exploretogether", "outdoorlovers", "discoverearth", 
    "landscapelovers", "earthfocus", 
    "srilanka", "wonderofasia", "srilankatravel", "exploresrilanka", 
    "visitsrilanka", "lovesrilanka", "srilankadaily", "srilankanature", 
    "srilankabeaches", "srilankaculture", "srilankalife", "lka", 
    "ceylon", "beautifulsrilanka", "srilankascenery", "srilankamountains", 
    "srilankansunset", "srilankasunrise", "srilankaphotography", 
    "srilankaadventures", "srilankavacation", "srilankatrip", 
    "srilankanfood", "srilankatourism", "srilankatour", "unseenlanka", 
    "srilankaparadise", "srilankadiaries"
]


def random_hashtag():
    return random.choice(hashtags_list)

# Existing sections (like, follow, unfollow, comment) remain unchanged
def open_like_section():
    try:
        hashtag = random_hashtag()
        print(f"Selected Hashtag: #{hashtag}")
        amount = random.randint(1, 5)  # Reduced amount for more human-like behavior
        posts = client.hashtag_medias_recent(hashtag, amount)
        for i in range(amount):
            print(f"Post {str(i + 1)}")
            client.media_like(posts[i].id)
            time.sleep(random.randint(30, 60))  # Increased time delay
            print(f"Liked post {posts[i].id} by user {posts[i].user.username}")
    except Exception as e:
        print(f"Error in like section: {e}")

def open_following_section():
    try:
        hashtag = random_hashtag()
        print(f"Selected Hashtag: #{hashtag}")
        amount = random.randint(1, 8)  # Reduced to 1-3 follows to avoid spam behavior
        posts = client.hashtag_medias_recent(hashtag, amount)
        for i in range(amount):
            print(f"{str(i + 1)}. Post ID: {posts[i].id}, User: {posts[i].user.username}")
            client.user_follow(posts[i].user.pk)
            time.sleep(random.randint(90, 120))  # Increased delay
            print(f"Followed user: {posts[i].user.username}")
    except Exception as e:
        print(f"Error in follow section: {e}")

def open_unfollow_section():
    try:
        amount = random.randint(3, 8)
        account_info = client.user_info_by_username(username)
        followings = client.user_following(account_info.pk)
        for i, user_id in enumerate(list(followings.keys())[:amount]):
            client.user_unfollow(user_id)
            time.sleep(random.randint(120, 200))  # Increased delay
            print(f"Unfollowed {user_id}")
    except Exception as e:
        print(f"Error in unfollow section: {e}")

def open_comment_section():
    try:
        hashtag = random_hashtag()
        print(f"Selected Hashtag: #{hashtag}")
        amount = random.randint(1, 3)  # Reduced to 1-3 comments
        posts = client.hashtag_medias_recent(hashtag, amount)
        comments = [
            "Amazing! 😍", "Love it! ❤", "Wow! 🔥", "Beautiful! 🌸", 
            "Nice shot! 👏", "Perfect! 💯", "Awesome! 🙌", "Incredible! 🤩", 
            "Great pic! 📸", "So cool! 😎", "Wonderful! 💐", "Breathtaking! 🌅", 
            "Lovely! 💖", "Epic! 🎉", "Fantastic! 🌟", "Stunning! 🌄", 
            "Impressive! ✨", "Superb! 👌", "Gorgeous! 💙", "Brilliant! 💥", 
            "Adorable! 😍", "Inspiring! 💫", "Nice! 👍", "So pretty! 🌷", 
            "Classy! 👏", "Fabulous! 💕", "Wow, just wow! 🤯", 
            "Spectacular! 💥", "Majestic! 🌲", "Mind-blowing! 💫", 
            "Picture perfect! 📸", "On point! ✔", "Just wow! 😍", 
            "Outstanding! 🏞", "Pure magic! ✨", "Awesome view! 🔥", 
            "Gorgeous view! 🌄", "Cute! 😊", "Excellent! 💯", "Iconic! 🌟", 
            "Pure beauty! 💙", "So peaceful! 🌿", "Perfection! 👏", 
            "Eye-catching! 👁", "Love this! 💗", "Too good! 🙌", 
            "Wonderful vibes! 🌺", "Impressive view! 😍", "So serene! 🌲",
            "😍🔥", "👏❤", "✨💯", "🌄💖", "😎💥", "📸💙", "🌟🎉", "🔥👌","🌷💫","💯🌅"
        ]
        for i in range(amount):
            selected_comment = random.choice(comments)
            print(f"Post {str(i + 1)}")
            client.media_comment(posts[i].id, selected_comment)
            time.sleep(random.randint(100, 200))  # Increased delay
            print(f"Commented on post {posts[i].id}: {selected_comment}")
    except Exception as e:
        print(f"Error in comment section: {e}")

def random_task():
    tasks = [
        open_like_section,
        open_following_section,
        open_unfollow_section,
        open_comment_section,
    ]
    return random.sample(tasks, 1)  # Select only one task per cycle to reduce spam activity

def run_program():
    while True:  # Loop will run indefinitely
        print_banner()
        tasks = random_task()
        for task in tasks:
            task()  # Execute the selected tasime

        wait_time = random.randint(1000, 2000)
        print(f"Waiting for {wait_time // 60} minutes and {wait_time % 60} seconds before the next tasks.")
        time.sleep(wait_time)

run_program()