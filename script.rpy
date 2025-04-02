# Game setup
init python:
    from random import randint

    # Initialize game variables
    current_time = 0
    customer_patience = 100
    self_boredom = 0
    manager_annoyance = 0
    theft_loss = 0
    
    # Define character images
    player_image = "player_neutral.png"
    partner_image = "partner_enthusiastic.png"
    sales_veteran_image = "sales_veteran_neutral.png"
    sales_young_image = "sales_young_neutral.png"
    sales_manager_image = "sales_manager_neutral.png"
    product_manager_image = "product_manager_neutral.png"
    repair_manager_image = "repair_manager_neutral.png"
    gm_image = "gm_neutral.png"
    
    # Define facial expressions
    expressions = {
        "neutral": "",
        "happy": "_happy",
        "sad": "_sad",
        "angry": "_angry",
        "worried": "_worried",
        "surprised": "_surprised"
    }
    
    # Function to update images with expressions
    def update_expression(image, expression):
        if expression in expressions:
            return image + expressions[expression]
        else:
            return image

# Define characters
define player = Character("Player", player_image)
define partner = Character("Partner", partner_image)
define sales_veteran = Character("Sales Veteran", sales_veteran_image)
define sales_young = Character("Young Sales Associate", sales_young_image)
define sales_manager = Character("Sales Manager", sales_manager_image)
define product_manager = Character("Product Manager", product_manager_image)
define repair_manager = Character("Repair Manager", repair_manager_image)
define gm = Character("General Manager", gm_image)

# Define scenes
define store_entrance = Scene("store_entrance")
define desk = Scene("desk")
define security_room = Scene("security_room")
define break_room = Scene("break_room")
define gameover_screen = Scene("gameover_screen")

# Define assets for expressions
define player_neutral = "player" + expressions["neutral"]
define player_happy = "player" + expressions["happy"]
define player_sad = "player" + expressions["sad"]
define player_worried = "player" + expressions["worried"]
define player_surprised = "player" + expressions["surprised"]

# Define expressions
define player_expressions = {
    "neutral": player_neutral,
    "happy": player_happy,
    "sad": player_sad,
    "worried": player_worried,
    "surprised": player_surprised
}

# Define the main menu
label main_menu:
    return
# Define the game's start screen
label start_screen:
    show screen start

# Define the game's start function
label start_game:
    $ current_time = 0
    $ player.image = player_expressions["neutral"]
    $ gm.say("Welcome to your new role as a Front-Desk Host and Asset Protection Associate.")
    $ gm.say("Your shift starts now.")
    $ store_entrance.play()
label start_game:
    $ current_time = 0
    $ player.image = player_expressions["neutral"]
    $ gm.say("Welcome to your new role as a Front-Desk Host and Asset Protection Associate.")
    $ gm.say("Your shift starts now.")
    $ store_entrance.play()

# Define the function to update the time
label update_time:
    $ current_time += 1
    if current_time % 60 == 0:
        $ current_time_str = "{:02d}:{:02d}".format(current_time // 60, current_time % 60)
        $ time_display = "Time: " + current_time_str
        $ show_variable("time_display")

# Define the function to handle dialogue choices
label dialogue_choice(option, expression):
    $ customer_patience, self_boredom, manager_annoyance
    $ player.image = player_expressions[expression]
    if option == 1:
        # Example positive customer interaction
        $ customer_patience += 20
        $ self_boredom -= 5
        $ manager_annoyance -= 5
        return "Thank you for your help!"
    elif option == 2:
        # Example negative customer interaction
        $ customer_patience -= 10
        $ self_boredom += 5
        $ manager_annoyance += 5
        return "I understand you're busy."
    else:
        return "I'm not sure how to respond."

# Define the desk scene
label desk_interaction:
    $ current_time
    while current_time < 240:  # 240 minutes for a 4-hour shift
        $ customer_arrives = Scene("customer_arrives")
        $ customer = Character("Customer", "customer_neutral.png")
        $ customer.say("Hi, I need some help with a product.")
        menu:
            "How would you like to respond?"
            "Offer help enthusiastically":
                $ response = dialogue_choice(1, "happy")
                $ customer.say(response)
            "Seem disinterested":
                $ response = dialogue_choice(2, "sad")
                $ customer.say(response)
        $ current_time += 5
        $ customer.image = update_expression(customer.image, customer_patience)
        $ partner.say("Great job, partner! Keep it up!")
        $ partner.image = update_expression(partner.image, "happy")
        call update_time()

# Define the customer interaction function
label customer_interaction:
    $ customer_patience, self_boredom, manager_annoyance
    if customer_patience > 50:
        $ customer_patience -= 10
        $ self_boredom -= 5
        $ manager_annoyance -= 5
        return "Thank you so much! You're amazing at your job!"
    else:
        $ customer_patience -= 10
        $ self_boredom += 5
        $ manager_annoyance += 5
        return "Okay, I guess you're busy."

# Define the store entrance scene
label store_entrance_scene:
    $ gm.say("Your role is crucial for both customer service and asset protection.")
    $ gm.say("Remember to balance both aspects throughout your shift.")
    $ gm.image = gm.update_expression("neutral")
    $ gm.say("You can take breaks at any time by going to the break room.")
    $ gm.say("Now, let's get to work.")
    $ store_entrance.play()

# Define the desk scene
label desk_scene:
    $ player.image = player_expressions["neutral"]
    $ player.say("Welcome to the front desk.")
    $ partner.say("Hi, I'm your partner for today.")
    $ partner.image = update_expression(partner_image, "neutral")
    menu:
        "Choose your next action"
        "Handle Customer Interaction":
            call desk_interaction
        "Check Security Cameras":
            call security_room_scene
        "Take a Break":
            call break_room_scene
        "Continue Working":
            call continue_work_scene

# Define the security room scene
label security_room_scene:
    $ player.say("I'll be in the security room checking the cameras.")
    $ player.image = player_expressions["worried"]
    menu:
        "Choose your next action"
        "Return to Desk":
            call desk_scene
        "Investigate Theft Alert":
            call theft_alert_scene

# Define the theft alert scene
label theft_alert_scene:
    $ theft_loss, manager_annoyance
    $ theft_loss += 10
    $ manager_annoyance += 10
    $ player.say("Theft alert! I need to handle this.")
    $ player.image = player_expressions["worried"]
    menu:
        "Choose your next action"
        "Call for Backup":
            call call_backup_scene
        "Confront Thief":
            call confront_thief_scene

# Define the call for backup function
label call_backup_scene:
    $ player.say("I'm calling for backup.")
    $ player.image = player_expressions["neutral"]
    menu:
        "Choose your next action"
        "Return to Desk":
            call desk_scene

# Define the confront thief function
label confront_thief_scene:
    $ player.say("I'll confront the thief.")
    $ player.image = player_expressions["angry"]
    menu:
        "Choose your next action"
        "Use Non-Violent Approach":
            call non_violent_confront_scene
        "Use Violent Approach":
            call violent_confront_scene

# Define the non-violent confrontation
label non_violent_confront_scene:
    $ player.say("Excuse me, you need to come with me.")
    $ player.image = player_expressions["neutral"]
    menu:
        "Choose your next action"
        "Return to Desk":
            call desk_scene

# Define the violent confrontation (not recommended)
label violent_confront_scene:
    $ player.say("This is not the way to handle it.")
    $ player.image = player_expressions["sad"]
    menu:
        "Choose your next action"
        "Return to Desk":
            call desk_scene

# Define the break room scene
label break_room_scene:
    $ player.say("I need a break.")
    $ player.image = player_expressions["happy"]
    $ self_boredom = max(self_boredom - 20, 0)
    menu:
        "Choose your next action"
        "Return to Desk":
            call desk_scene

# Define the continue working function
label continue_work_scene:
    $ player.say("I'll keep working.")
    $ player.image = player_expressions["neutral"]
    menu:
        "Choose your next action"
        "Handle Customer Interaction":
            call desk_interaction
        "Check Security Cameras":
            call security_room_scene
        "Take a Break":
            call break_room_scene

# Define the end of shift scene
label end_of_shift_scene:
    $ player.say("It's the end of my shift.")
    $ player.image = player_expressions["neutral"]
    if theft_loss > 0:
        $ gm.say("We had some theft issues today.")
        $ gm.image = gm.update_expression("worried")
    else:
        $ gm.say("Great job keeping an eye on the store.")
        $ gm.image = gm.update_expression("happy")
    menu:
        "Choose your next action"
        "Continue Working":
            call continue_work_scene
        "End Shift":
            call main_menu

# Define the end of the game screen
label end_game_scene:
    show screen gameover
    return "Game Over"

# Define the game's gameover screen
label gameover_screen_scene:
    $ player.say("Your shift is over.")
    $ player.image = player_expressions["neutral"]
    $ show_variable("time_display")
    $ show_variable("manager_annoyance")
    $ show_variable("theft_loss")
    menu:
        "Choose your next action"
        "Start New Shift":
            call start_game
        "Return to Main Menu":
            call main_menu

# Define the screen assets
screen start:
    add player_neutral at center
    add "Time: 00:00" at bottom
    add "Patience: 100" at bottom
    add "Boredom: 0" at bottom
    add "Theft Loss: 0" at bottom

screen gameover:
    add player_neutral at center
    add "Time: " + str(current_time) + " minutes" at bottom
    add "Manager Annoyance: " + str(manager_annoyance) at bottom
    add "Theft Loss: " + str(theft_loss) at bottom

# Define the scenes
define store_entrance = Scene("store_entrance")
define desk = Scene("desk")
define security_room = Scene("security_room")
define break_room = Scene("break_room")
define gameover_screen = Scene("gameover_screen")

# Define the game's main function
label main:
    call start_game

# Run the game