Ball = Class{}

--initialize our ball or create instructions for the ball
-- def __init__(self,arguments):
function Ball:init(x,y,width,height)
     self.x = x
     self.y = y
     --this.whatever = whatever
     self.width = width
     self.height = height

     --along with the default info, we need the velocity variables dx and dy
     self.dy = math.random(2) == 1 and -100 or 100
     self.dx = math.random(-50, 50)
end

--reset function to move it back to the middle of the screen
function Ball:reset(paddle)
     self.x = paddle.x
     self.y = paddle.y
     self.dx = math.random(2) == 1 and -100 or 100
     self.dy = math.random(-50, 50)
end

function Ball:collides(paddle)
     --checking to see if I collided with the walls
     --cecking to see if the bottom edge of either is higher than the top edge 
     --   of the other 
     if self.y > (paddle.y + paddle.height) or paddle.y > self.y + self.height then
          return false
     end

     --checking to see if I collided with the paddles
     if self.x > (paddle.x + paddle.width) or paddle.x > (self.x + self.width) then
          return false
     end
     
     return true
end

--update function that tells the ball what to do
function Ball:update(dt)
     self.x = self.x + self.dx*dt
     self.y = self.y + self.dy*dt
end

--render the ball to the screen
function Ball:render()
     love.graphics.rectangle('fill',self.x,self.y,self.width,self.height)
end