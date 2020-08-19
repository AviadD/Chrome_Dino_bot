import pyautogui as gui 
import keyboard
import time
import math



# Helper function to get value of pixel in image
def getPixel(Image,x, y):
    px = Image.load()
    return px[x, y]


def play():

    screenDimensions = {
    "top": 293,
    "left": 0,
    "width": 1920,
    "height": 465
    }

    # Intervals where will search obstacles (cactus\birds)
    y_cactus_search, x_start, x_end = 350, 435, 450
    y_birds_search = 275 
    
    # Time variables  
    last = 0
    total_time = 0
    
    while True:
        time1 = time.time()
        if keyboard.is_pressed('q'): # prass 'q' for stop the bot 
            break

        # Increase search width to the obstacle (cactus\birds) every second, to simulate the acceleration
        if math.floor(total_time) != last:
            x_end += 4
            if x_end >= screenDimensions['width']:
                x_end = screenDimensions['width']
            last = math.floor(total_time)


        # Get a screen shot
        sct_img = gui.screenshot(region=(screenDimensions['left'],screenDimensions['top'], screenDimensions['width'], screenDimensions['height']))

        # Get the color of the world background
        backgroundColor = getPixel(sct_img, 440, 30)

        for i in reversed(range(x_start, x_end)):
            # If pixel in the search interval with a colour than different from background color, so it is an obstacle 
            if getPixel(sct_img,i,y_cactus_search) != backgroundColor\
                    or getPixel(sct_img,i,y_birds_search) != backgroundColor:
                keyboard.press(' ') # jump
                break

        time2 = time.time() - time1
        total_time += time2


if __name__ == "__main__":
    print('Hey Dino Bot will start in 1 second (Prass \'Q\' to stop the bot)')
    time.sleep(1)
    keyboard.press(' ') # start the game
    play()
