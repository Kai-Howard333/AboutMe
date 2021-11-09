PaddleLR = Class{}

--initialize a paddle
function PaddleLR:init(x, y, width, height)
     self.x = x
     self.y = y
     self.width = width
     self.height = height
     --dy is the paddle speed from main.lua
     self.dy = 0
 end

--update my paddle
function PaddleLR:update(dt)
     if self.dy<0 then
          self.y = math.max(0, self.y + self.dy * dt)
     else
          self.y = math.min(VIRTUAL_HEIGHT - self.height, self.y + self.dy * dt)
     end
end

--render my paddle
function PaddleLR:render()
     love.graphics.rectangle('fill', self.x, self.y, self.width, self.height)
 end