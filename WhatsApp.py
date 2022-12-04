#pip install pywhatkit

import pywhatkit

# Send whatsApp message right now
pywhatkit.sendwhatmsg_instantly("+201234567890", "Hi", 15, True, 2)

# Send whatsApp message at a specific time HH & MM
#pywhatkit.sendwhatmsg("Phone number", "your_msg", hours, minutes, wait, close_after_sending, close after)
pywhatkit.sendwhatmsg("+201234567890", "Hi", 13, 30, 15, True, 2)

# Send an Image to a Group with the Caption as Hello
pywhatkit.sendwhats_image("ABCDE123456789abc", "pics/my_image.png", "Caption_for_the_image")

# Send an Image to a Contact with the no Caption
pywhatkit.sendwhats_image("+201234567890", "pics/my_image.png")

# Send WhatsApp Message on a Group at a specific time HH, MM by using the group ID
pywhatkit.sendwhatmsg_to_group("ABCDE123456789abc", "Hello to the Group...", 0, 0)

# Send a WhatsApp Message on a Group right now
pywhatkit.sendwhatmsg_to_group_instantly("ABCDE123456789abc", "Hey All!")
