game: banana split
a game where you collect bananas and your friend on the right makes the banana splits, you can play solo, or with a friend!
guide is in game and when you get to 30, there will be a cool surprise!


How to download and run:
- step 1: go to the release file and download the folder BananaSplit
- step 2: extract the folder and open it
- step 3: click the BananaSplit exe file and run it
- step 4: Have fun

<img width="1897" height="1085" alt="Screenshot 2026-11-15 003358" src="https://github.com/user-attachments/assets/001efbfe-4df6-4023-a03f-d36e50afce67" />
<img width="1890" height="1082" alt="Screenshot 2026-11-15 003329" src="https://github.com/user-attachments/assets/2b221d23-9552-4b9d-8402-b47974855807" />
<img width="1883" height="1071" alt="Screenshot 2026-11-15 003314" src="https://github.com/user-attachments/assets/d7db3da0-2695-4101-bf0d-ba47042e45ca" />
<img width="1905" height="1090" alt="Screenshot 2026-11-15 040639" src="https://github.com/user-attachments/assets/79b29c50-117d-4fa9-ae79-846cc3a54640" />



devlogs:

First hour:
functions: 
- Switched from c++ raylibs which was what i was using the past few weeks, to python pygame because i already understand
  basic python and pygame provides more efficient and useful builitin sprite functions and have pixel perfect collisions
  unlike raylibs where i have to create a hitbox.
- Learned how to initialize pygame window display images and sprites
- programmed 8 directional movement using wasd for left side and farm side only ( used a bit of math)
textures:
- created piixel art for background for the left side screen which is the farm
- created pixel art for 8 directional farmer sprites so diagonals and the vertical and horizontal directions.
other:
i also created folders and files for separate objects or functions of the game, suggested by a friend because i was putting all my code in one file..... but this forces me to learn how to be organized which is good.
New things learned: a whole new library ): but it will help, and it will be easier later on because i can check for collision of sprites easily.

second hour:

added three trees to the farm using a list to store their positions
made it so the player can walk behind and infront of trees
added collision to the tree trunks so the player can't walk thru them
made a player feet hitbox on the bottom of the player so to make the collisions
made a border around the farm
textures:

made a banaana tree, i think i did REALLY good on this one;.
troubles:

fixed the tree hitboxes because they werent in the right position most of the time
fixed the layering so the trees appear over the player when theyre behind them
new things learned:

learned how to use for loops and lists to store three tree positions and for loops to get attributes of each tree
used rectangles for hiboxes and collision

Third hour:

added banan bunches that can be collected when you get close
made a interaction system that uses E to pickup bananas
made it so the farmer can only carry one bunch at a time
added directionaal poosiitoning for bananas while farmer is carrying it, all 8 directions
also made the banana rotate depending on which way the farmer faces
textures:

created banana textures
new things learned:

learned how to use pygame.transform..rotate() and pygame.transform.flip() which allows me to rotate or invert the sprites

fourth hour:
functional:

added banana respawning with them respawning 6.7 seconds aftrer being collected
added collecting bananas and delivering them at the dropoff station.
made delivered bananas wait 2 seconds before moving on the conveyor belt.
made a banana delivered counter on the top left of the screen
textures:

created the conveyor belt texture
creaded the dropoff texture
new things i learned:

learned the pygame font function for text
learned pygame.time.get_ticks() to make the timer and wait time for the bananas
troubles:
had to rewrite code to implement the the next idea, because when i wrote code, it doesnt correlate for the next step i do so most the time i was rewriting code and repositioning, most annoying was positioning where things had to go.


Fifth hour:
textures:

created the second screen, cutting board
created a receiving box for bananas to arrive
created a bigger banana textures when dragged onto cutting board
fucntional:

created hitboxes for cutting board, receiving box, and bananas
implemented mouse cursor posiiton tracking.
added mouse interaction so the player must drag bananas from thebox onto the cutting board
new things learned:

learned how to track mouse pos with pygame and convert them to the games resolution
learned how to use hitboxes to detex mouse interactions
learned how to make drop and drop mechanics
trioubles:

had troubles getting the mouse coordinates to the match the games res
had trouble making the banana follow the cursor
fixed banana disappearing when released
ALOT of repositioning


sixth/seventh hour:
textures:

created chcolate, strawberry. and vanilla ice cream scoops
created chocolate, strawberry and vanilla ice cream choices buttons
created large peeled banana and and created large cut banana
created the tray
functions:

added banana peeling when player clicks unpeeled banana
added banana cutting on the second click
made a tray slide down from teh top of screen to underneath the cut bannaa
added three ice cream flavor selection that appears after the tray
made it possible to select up to three scoops of icecream
added displayingthe selected flavors in order from top to bottom of banana
new things learned:

learned how to use lists better to store multiple selections
learned how to use dictionaries better to cconnect flavor names with their sprites
learned how to animate kinddaa withcode
troubles:

had trouble getting ice cream buttons to click correctly
had troubles displaying ice cream scoops
had troubles adjusting the positions, this is pain
debugging debugging


eighth/ninth/tenth hour
textures:

created a serve button
created a main menu background
created play, guide, and stats buttons
created a guide screen and stats screen
created win and lose screens for both levels
functions:

added a serve button that appears after selecting 3 scoops
made it so clicking serve completes an order and adds to the order count
made everything reset after serving so the player can make another banana split
added a timer and order goal for both levels
made level 1 have 60 seconds and a goal of 8 orders
made level 2 have 90 seconds and a goal of 15 orders
made it so winning level 1 takes you to level 2
made it so finishing level 2 takes you back to a main menu
fixed it so clicking play always starts at level 1
added a guide screen with instructions on how to play
added a stats screen
added tracking for games played, games won, games lost, total orders, and highest orders
made stats save into a txt file and load when opening a game
sounds:

added menu music and game music
added win and lose music
added clicking, cutting, pickup, peeling, scooping, serving, and drop-off sounds
made a function for music so it doesn't restart every frame
new things learned:

learned how to save and load data using files
learned how to keep track of stats
learned more about using game states
learned how to use dictionaries even more
troubles:

had trouble getting a serve button to work
had trouble making a level 1 to level 2 transition work
had trouble with stats saving multiple times instead of just once
had trouble resetting everything when going back to a main menu
debugging debugging
SORRY! i was rushing to go somewhere and i had to do my coding or else i would lose time because i still have 10 more hours left and i need all the time i can get so i put it all in one commit. but im doing devlogs of every 2/3 hours because it seems more efficient and less time consuming, and i think better without doing other things but i was proud of this one, my game looks pretty good!



im not gonna do my usual bullet point but i will bulletpoint another way since im running out of time,

Hour 11: Secret Ending
Started working on a secret (not so secret) ending that plays when the player completes a certain amount of orders.
Made a rocket launch animaton that starts once the secret ending is triggered.
Added a powering up animatipn before the rocket actually launches.
Hour 12: Rocket and Sky Animation
Added a sky texture and made it infinitely scroll to make it look like the rocket is actually flying up.
Added smoke particals that follows the rocket as it moves.
Added stars that start appearing once the rocket gets higher into space.
Made the sky slowly get darker as the rocket goes up, and brighter again when it comes back dowm.
Added rotaton so the rocket can turn 180 degrees and start falling back down to Earth.
Hour 13: City Impact and Slime Explosion
Textures

Made a pixel art city backround for when the rocket comes back down to Earth.
Also made another version of the city but this time its covered in green slime.
Functionality and Animations

Made the animaton switch from the moving sky to the city backround.
Made a smaller version of the rocket and rotated it so it faces downwards.
Added a falling animation where the rocket slowly comes down and hits the city.
When the rocket hits the ground, it triggers a green slime explossion.
Made the green circle slowly expand until it covers the entire screem.
Added a 1 second pause before the circle starts shrinking, revealing the city thats now covered in slime.
Things Learned

Learned how to resize and rotate sprites using pygame.transform.
Learned how to make a background scroll infinitely.
Learned a bit more about particals and how to animate smoke and stars.
Used booleans and timers to control when diffrent animations should happen.
Learned how to make an expanding and shrinking circle using pygame.draw.circle().
Troubles

At first the city background was way too big so all I could see was the sky, had to resize it to fit the game.
The rocket was facing the wrong direction when falling down, so I had to rotatw it.
The green slime explossion kept growing forever, so I had to add a limit and make it shrink afterwards.
Had some trouble with the drawing order becuase I wanted the slime covered city to appear after the explosion.


Hour 14 – Secret Ending
Functionality

added timers to make all the animations happen in order
made the backgrounds change during the explosions
added a funny ending screen after the animation
changed the secret ending to 1 order for testing because im not doing 30 orders everytime
Textures / Animations
made a city background, slime version and destroyed version
added another falling object
made the rocket fall into the city and cause an explosion
added another explosion, screen shaking and a fade to black
Sounds
started figuring out where the secret ending sounds should play
Hour 15 – Stats and Bug Fixes
Functionality

changed the secret ending back to 30 orders
added a stats.txt file to save progress and made a stats screen
added an UNLOCKED indicator for the secret ending
fixed the game reseting when restarting or changing levels
fixed the level 2 win and lose screens
fixed the pause system and stopped players from interacting after the game ends
Textures / Animations
made the secret ending animations reset properly
fixed some animation timings and postions
Sounds
added background music for the menu, gameplay, winning and losing
added sounds for picking up bananas, cutting, peeling, scooping and serving
made the music change depending on the game screen
started adding sounds to the secret ending
Hour 16 – Final Touches
Functionality

added a 3, 2, 1 countdown and stopped the farmer from moving during it
fixed the timer so it starts after the countdown
added a hint about the secret ending in the how to play guide
added a purple progress bar for the secret ending
made the timer flash red when theres less than 10 seconds
Textures / Animations
added the countdown numbers and progress bar
made the secret ending hint yellow
added the flashing timer effect
Sounds
finished adding more secret ending sounds
adjusted the sounds to match the animations
Things Learned / Troubles (Hours 14–16)

learned more about using pygame.time.get_ticks() for timers and animations
learned how to make explosions, screen shaking and fading effects
learned how to save stats using txt files and calculate winrate
learned how to make a progress bar using pygame.draw.rect()
learned more about game states and reseting variables
had alot of trouble getting the secret ending animations to happen at the right time
fixing the game resets and pause system was annoying because there were so many varaibles
had some issues with the countdown and farmer movement but eventually fixed it
learned how to use pygame mixer for music and sound effects
learned how to package my game into an exe using pyinstaller
had to deal with the assets and libaries again which was pretty annoying
spent way too much time fixing small bugs when i thought i was finally done
