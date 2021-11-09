PaddleTB = Class{}

--initialize a paddle
function PaddleTB:init(x, y, width, height)
     self.x = x
     self.y = y
     self.width = width
     self.height = height
     --dy is the paddle speed from main.lua
     self.dx = 0
 end

--update my paddle
function PaddleTB:update(dt)
     if self.dx<0 then
          self.x = math.max(0, self.x + self.dx * dt)
     else
          self.x = math.min(VIRTUAL_WIDTH - self.width, self.x + self.dx * dt)
     end
end

--render my paddle
function PaddleTB:render()
     love.graphics.rectangle('fill', self.x, self.y, self.width, self.height)
 end
