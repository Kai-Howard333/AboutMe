push = require 'push'
Class = require 'class'
require 'Ball'
require 'Paddle'

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

VIRTUAL_WIDTH = 432
VIRTUAL_HEIGHT = 243

-- speed at which we will move the paddles; multiplied by dt in updateFunction
PADDLE_SPEED = 200

--A function to start up the window that initialize the game
function love.load()
     -- "seed" the RNG so that calls to random are always random
     -- utilizing the current time, since that will vary on start up
     math.randomseed(os.time())

     love.window.setTitle("Pong")

     --nearest-neightbor filtering on upscaling and downscaling to prevent blurriness
     love.graphics.setDefaultFilter('nearest','nearest')

     --var     = module.module.method('fileName',fontsize)
     smallFont = love.graphics.newFont('font.ttf',8)
     scoreFont = love.graphics.newFont('font.ttf',32)

     --initalized our virtual resolution, which is rendered inside of our actual window
     push:setupScreen(VIRTUAL_WIDTH,VIRTUAL_HEIGHT,WINDOW_WIDTH,WINDOW_HEIGHT,{
          fullscreen=false,
          resizable=false,
          vsync=true
     })

     -- score values:  render these scores on the screen
     player1Score=0
     player2Score=0

     --either going to be 1 or 2; whomever is scored on gets to serve the following turn
     servingPlayer=1

     --paddle positions on the Y axis
     --object = Constructor(x,y,width,height)
     player1 = Paddle(10, 30, 5, 20)
     player2 = Paddle(VIRTUAL_WIDTH - 10, VIRTUAL_HEIGHT - 30, 5, 20)

     
     --object ball = Ball(x,y,width,height)
     ball = Ball(VIRTUAL_WIDTH/2-2,VIRTUAL_HEIGHT/2-2,4,4)

     --we start at a 'start' state so no movement
     gameState = 'start'

end

-- runs every frame, with "dt" passed in, our delta in seconds since the last frame.
function love.update(dt)
     -- update our ball based on its DX and DY only if we're in play state;
     -- scale the velocity by dt so movement is framerate-independent
     if gameState == 'serve' then
          -- before switching to play, intialize ball's velocity
          --     based on the last person to score
          ball.dy = math.random(-50,50)
          if servingPlayer==1 then
               ball.dx = math.random(140,200)
          else
               ball.dx = -math.random(140,200)
          end
     elseif gameState == 'play' then
          --[[
               detech ball collision with paddles,
                    reversing dx if true and slightly increasing the speed(dx)
                    altering the dy based on the position of collision
          ]]
          if ball:collides(player1) then
               ball.dx = -ball.dx * 1.03     --increased the speed
               ball.x = player1.x +5         --moving back to not bounce in the paddle

               --keep velocity going in the same direction, but randomize it
               if ball.dy < 0 then
                    ball.dy = -math.random(10,150)
               else 
                    ball.dy = math.random(10,150)
               end
          end
          if ball:collides(player2) then
               ball.dx = -ball.dx * 1.03     --increased the speed
               ball.x = player2.x - 4         --moving back to not bounce in the paddle

               --keep velocity going in the same direction, but randomize it
               if ball.dy < 0 then
                    ball.dy = -math.random(10,150)
               else 
                    ball.dy = math.random(10,150)
               end
          end
          --detect boundary collision for the walls
          if ball.y <=0 then
               ball.y=0
               ball.dy = -ball.dy
          end
          if ball.y >=VIRTUAL_HEIGHT-4 then
               ball.y = VIRTUAL_HEIGHT-4
               ball.dy = -ball.dy
          end

          --going past the left side of the screen
          if ball.x < 0 then
               servingPlayer = 1
               player2Score = player2Score + 1
               if player2Score == 3 then
                    winningPlayer=2
                    gameState = 'done'
               else
                    gameState='serve'
                    ball:reset()
               end
          end
          --going past the right side of the screen
          if ball.x > VIRTUAL_WIDTH then
               servingPlayer = 2
               player1Score = player1Score + 1
               if player1Score == 3 then
                    winningPlayer=1
                    gameState = 'done'
               else
                    gameState='serve'
                    ball:reset()
               end
          end
          

          ball:update(dt)
          -- player 1 movement
          if love.keyboard.isDown('w') then
               player1.dy = -PADDLE_SPEED
          elseif love.keyboard.isDown('s') then
               player1.dy = PADDLE_SPEED
          else
               player1.dy = 0
          end
     
          -- player 2 movement
          if love.keyboard.isDown('up') then
               player2.dy = -PADDLE_SPEED
          elseif love.keyboard.isDown('down') then
               player2.dy = PADDLE_SPEED
          else
               player2.dy = 0
          end
          player1:update(dt)
          player2:update(dt)
     end

     
 
     
 
     
 end


--[[
     Keyboard handling, called by LOVE2D each frame;
          passes in the key we pressed so we can acess.
]]
function love.keypressed(key)
     --keys can be accessed by string name
     if key == 'escape' then
          --functione LOVE gives us to terminate application
          love.event.quit()
     elseif key == 'enter' or key=='return' then
          if gameState=='start' then
               gameState='serve'
          elseif gameState=='serve' then
               gameState='play'
          elseif gameState=='done' then
               --simply restart the game
               gameState = 'serve'
               ball:reset()
               player1Score=0
               player2Score=0
               --who serves first
               if winningPlayer == 1 then
                    servingPlayer=2
               else
                    servingPlayer = 1
               end
          end
     end
end

--update the screen with information: draw anything that is needed
--function module.draw()
function love.draw()
     --begin rendering a virtual resolution
     push:apply('start')

     -- clear the screen with a specific color; in this case, a color similar
     -- to some versions of the original Pong
     love.graphics.clear(40, 45, 52, 255)

     -- draw welcome text toward the top of the screen
     love.graphics.setFont(smallFont)
     if gameState == 'start' then
          love.graphics.printf('Welcome to Pong!', 0, 20, VIRTUAL_WIDTH, 'center')
          love.graphics.printf('Press Enter to begin!', 0, 30, VIRTUAL_WIDTH, 'center')
     
     elseif gameState == 'serve' then
          love.graphics.printf('Player ' .. tostring(servingPlayer) .. "'s serve!",
                     0, 20, VIRTUAL_WIDTH, 'center')
     
     elseif gameState == 'play' then
          --no message because we are playing
     
     elseif gameState == 'done' then
          love.graphics.setFont(scoreFont)
          love.graphics.printf('Player ' .. tostring(winningPlayer) .. "wins!",
                     0, 30, VIRTUAL_WIDTH, 'center')
          love.graphics.setFont(smallFont)
          love.graphics.printf('Press Enter to restart!',0, 20, VIRTUAL_WIDTH, 'center')
     end


     love.graphics.setFont(scoreFont)
     love.graphics.print(tostring(player1Score),VIRTUAL_WIDTH/2-60,VIRTUAL_HEIGHT/3)
     love.graphics.print(tostring(player2Score),VIRTUAL_WIDTH/2+50,VIRTUAL_HEIGHT/3)

     player1:render()
     player2:render()
     ball:render()

     displayFPS()

     -- end rendering at virtual resolution
     push:apply('end')
end

--frame per second not first person shooter
function displayFPS()
     love.graphics.setFont(smallFont)
     --r,g,b,a
     love.graphics.setColor(255,0,0,255)
     love.graphics.print("FPS: ".. tostring(love.timer.getFPS()),10,10)
end