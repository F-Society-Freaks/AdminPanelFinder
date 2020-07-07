# Created by LimerBoy
# https://github.com/LimerBoy/AdminPanelFinder

# Save text to file
def Log(text):
    print(text)
    with open("result.txt", "a") as file:
        file.write(text + "\n")