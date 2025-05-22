# # # # import pyautogui
# # # # import time
# # # # import pyperclip
# # # # from openai import OpenAI

# # # # pyautogui.click (1639,1412)
# # # # time.sleep(1)

# # # # pyautogui.moveTo(684,316)
# # # # pyautogui.dragTo(895, 901, duration=1.0, button='left')
# # # # pyautogui.hotkey('ctrl','c')
# # # # pyautogui.click (955,940)
# # # # time.sleep(1)

# # # # chat_history=pyperclip.paste()
# # # # print(chat_history)

# # # # completion =client.chat.completions.create(
# # # #     model="gpt-3.5-turbo",
# # # #     messages=[
# # # #         {"role":"system","content":"you are a person named harry who speaks hindi as well as english. He is from India and is coder. you analyze chat history and respond like Harry"},
# # # #         {"role":"user","content":chat_history}

# # # #     ]
# # # # )

# # # # response=completion.choices[0].message.content
# # # # pyperclip.copy(response)

# # # # pyautogui.click(1808, 1328)
# # # # time.sleep(1)

# # # # pyautogui.hotkey('ctrl','v')
# # # # time.sleep(1)

# # # # pyautogui.press('enter')

# # # import pyautogui
# # # import time
# # # import pyperclip
# # # import openai

# # # # Set up OpenAI API key
# # # openai.api_key = 'your-api-key'

# # # # Click on a specific position
# # # pyautogui.click(1639, 1412)
# # # time.sleep(1)

# # # # Select and copy chat history
# # # pyautogui.moveTo(684, 316)
# # # pyautogui.dragTo(895, 901, duration=1.0, button='left')
# # # pyautogui.hotkey('ctrl', 'c')
# # # pyautogui.click(955, 940)
# # # time.sleep(1)

# # # chat_history = pyperclip.paste()
# # # print(chat_history)

# # # # Create a completion request to OpenAI
# # # completion = openai.ChatCompletion.create(
# # #     model="gpt-3.5-turbo",
# # #     messages=[
# # #         {"role": "system", "content": "You are a person named Harry who speaks Hindi as well as English. He is from India and is a coder. Analyze chat history and respond like Harry."},
# # #         {"role": "user", "content": chat_history}
# # #     ]
# # # )

# # # response = completion.choices[0].message.content
# # # pyperclip.copy(response)

# # # # Paste and send the response
# # # pyautogui.click(1808, 1328)
# # # time.sleep(1)
# # # pyautogui.hotkey('ctrl', 'v')
# # # time.sleep(1)
# # # pyautogui.press('enter')

# # import pyautogui
# # import time
# # import pyperclip
# # import openai

# # # Set up OpenAI API key
# # openai.api_key = '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'

# # # Click on a specific position
# # pyautogui.click(1639, 1412)
# # time.sleep(1)

# # # Select and copy chat history
# # pyautogui.moveTo(684, 316)
# # pyautogui.dragTo(895, 901, duration=1.0, button='left')
# # pyautogui.hotkey('ctrl', 'c')
# # pyautogui.click(955, 940)
# # time.sleep(1)

# # chat_history = pyperclip.paste()
# # print(chat_history)

# # # Create a completion request to OpenAI using the updated API call
# # completion = openai.ChatCompletion.create(
# #     model="gpt-3.5-turbo",
# #     messages=[
# #         {"role": "system", "content": "You are a person named Naruto who speaks Hindi as well as English. you are from India and you are a coder. Analyze chat history and respond like Naruto. Output should be the next chat response as Naruto"},
# #         {"role": "user", "content": chat_history}
# #     ]
# # )

# # response = completion.choices[0].message['content']
# # pyperclip.copy(response)

# # # Paste and send the response
# # pyautogui.click(1808, 1328)
# # time.sleep(1)


# # pyautogui.hotkey('ctrl', 'v')
# # time.sleep(1)
# # pyautogui.press('enter')


# import pyautogui
# import time
# import pyperclip
# from openai import OpenAI




# client = OpenAI(
#   api_key="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",
# )

# def is_last_message_from_sender(chat_log, sender_name="Rohan Das"):
#     # Split the chat log into individual messages
#     messages = chat_log.strip().split("/2024] ")[-1]
#     if sender_name in messages:
#         return True 
#     return False
    
    

#     # Step 1: Click on the chrome icon at coordinates (1639, 1412)
# pyautogui.click(1639, 1412)

# time.sleep(1)  # Wait for 1 second to ensure the click is registered
# while True:
#     time.sleep(5)
#     # Step 2: Drag the mouse from (1003, 237) to (2187, 1258) to select the text
#     pyautogui.moveTo(737,272)
#     pyautogui.dragTo(1737, 900, duration=2.0, button='left')  # Drag for 1 second

#     # Step 3: Copy the selected text to the clipboard
#     pyautogui.hotkey('ctrl', 'c')
#     time.sleep(2)  # Wait for 1 second to ensure the copy command is completed
#     pyautogui.click(845, 972)

#     # Step 4: Retrieve the text from the clipboard and store it in a variable
#     chat_history = pyperclip.paste()

#     # Print the copied text to verify
#     print(chat_history)
#     print(is_last_message_from_sender(chat_history))
#     if is_last_message_from_sender(chat_history):
#         completion = client.chat.completions.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {"role": "system", "content": "You are a person named Pratham who speaks hindi as well as english. You are from India and you are a coder. You analyze chat history and roast people in a funny way. Output should be the next chat response (text message only)"},
#             {"role": "system", "content": "Do not start like this [21:02, 12/6/2024] Aman Kumar Verma: "},
#             {"role": "user", "content": chat_history}
#         ]
#         )

#         response = completion.choices[0].message.content
#         pyperclip.copy(response)

#         # Step 5: Click at coordinates (1808, 1328)
#         pyautogui.click(1808, 1328)
#         time.sleep(1)  # Wait for 1 second to ensure the click is registered

#         # Step 6: Paste the text
#         pyautogui.hotkey('ctrl', 'v')
#         time.sleep(1)  # Wait for 1 second to ensure the paste command is completed

#         # Step 7: Press Enter
#         pyautogui.press('enter').


import pyautogui
import time
import pyperclip
import openai

# Initialize OpenAI with your API key
openai.api_key = "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"

def is_last_message_from_sender(chat_log, sender_name="Rohan Das"):
    # Extract the last message from the chat log
    messages = chat_log.strip().split("/2024] ")[-1]
    if sender_name in messages:
        return True 
    return False

# Step 1: Click on the Chrome icon at coordinates (1639, 1412)
pyautogui.click(1258, 1047)

time.sleep(1)  # Wait for 1 second to ensure the click is registered

while True:
    time.sleep(5)
    
    # Step 2: Drag the mouse to select the text
    pyautogui.moveTo(716, 272)
    pyautogui.dragTo(1462, 880, duration=2.0, button='left')  # Drag to select

    # Step 3: Copy the selected text to the clipboard
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(2)  # Wait for the copy command to complete
    pyautogui.click(838, 968)

    # Step 4: Retrieve the text from the clipboard
    chat_history = pyperclip.paste()

    # Print the copied text to verify
    print(chat_history)
    print(is_last_message_from_sender(chat_history))
    
    if is_last_message_from_sender(chat_history):
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a person named Pratham who speaks Hindi as well as English. You are from India and you are a coder. You analyze chat history and roast people in a funny way. Output should be the next chat response (text message only)."},
                {"role": "system", "content": "Do not start like this [21:02, 12/6/2024] Rohan Das: "},
                {"role": "user", "content": chat_history}
            ]
        )

        response = completion.choices[0].message["content"]
        pyperclip.copy(response)

        # Step 5: Click at coordinates (1808, 1328)
        pyautogui.click(838, 968)
        time.sleep(1)  # Wait for the click to register

        # Step 6: Paste the text
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)  # Wait for the paste command to complete

        # Step 7: Press Enter
        pyautogui.press('enter')
