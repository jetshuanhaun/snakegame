import sys
import random
import pygame
from pygame.locals import *

#目标方块的的颜色为红色
foodColor = pygame.Color(255,0,0)
#游戏背景色为黑色
bgColor = pygame.Color(0,0,0)
#贪吃蛇颜色为白色
snakeColor = pygame.Color(255,255,255)

#游戏结束的函数
def gameOver():
    pygame.quit()
    sys.exit()

#定义分数文本
def show_text(screen, positon, text, color, font_bold = False, font_size = 40, font_italic = False):
    #获取系统字体，并设置文字大小
    cur_font = pygame.font.SysFont("宋体", font_size)
    #设置是否加粗属性
    cur_font.set_bold(font_bold)
    #设置是否斜体属性
    cur_font.set_italic(font_italic)
    #设置文字内容
    text_fmt = cur_font.render(text, 1, color)
    #绘制文字
    screen.blit(text_fmt, positon)

#定义主函数
def main():
    #初始化pygame
    pygame.init()
    #定义一个速度的函数
    snakeSpeed = pygame.time.Clock()
    #定义游戏界面大小
    gameSurface = pygame.display.set_mode((640,480))
    #在游戏界面标识为贪吃蛇
    pygame.display.set_caption("焕焕贪吃蛇1.0")

    #贪吃蛇的初始位置及长度
    snake_position = [100,100]
    snake_body = [[100,100],[80,100],[60,100]]

    #食物的初始位置
    food_position = [300,300]

    #食物的状态
    food_flag = 1

    #贪吃蛇的初始方向
    direction = "right"
    #贪吃蛇的方向变量
    chang_direction = direction
    #初始话分数
    score = 0

    """
    # 初始化音乐
    pygame.mixer.init()
    pygame.mixer.music.load("music.mp3")
    # 播放音乐
    pygame.mixer.music.play()
    """


    while True:


        #事件交互
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    chang_direction = "right"
                if event.key == K_LEFT:
                    chang_direction = "left"
                if event.key == K_UP:
                    chang_direction = "up"
                if event.key == K_DOWN:
                    chang_direction = "down"
                if event.key == K_ESCAPE:
                    pygame.event.post(pygame.event.Event(QUIT))

        #键盘控制移动方向
        if chang_direction == "left" and not direction == "right":
            direction = chang_direction
        if chang_direction == "right" and not direction == "left":
            direction = chang_direction
        if chang_direction == "up" and not direction == "down":
            direction =chang_direction
        if chang_direction == "down" and not direction == "up":
            direction = chang_direction

        #根据方向来移动贪吃蛇
        if direction == 'right':
            snake_position[0] += 20

        if direction == 'left':
            snake_position[0] -= 20

        if direction == 'up':
            snake_position[1] -= 20

        if direction == 'down':
            snake_position[1] += 20

        # 贪吃蛇的头和身体碰撞
        for body in snake_body:
            if snake_position[0] == body[0] and snake_position[1] == body[1]:
                gameOver()

        #贪吃蛇移动
        snake_body.insert(0,list(snake_position))
        if snake_position[0] == food_position[0] and snake_position[1] == food_position[1]:
            food_flag = 0
        else:
            # 如果没吃到，蛇尾弹出栈
            snake_body.pop()


        #吃掉一个加5分
        if food_flag==0:
            score +=5

        #食物如果被吃掉了
        if food_flag==0:
            x = random.randint(1,30)
            y = random.randint(1,20)
            # 20*20的像素为一个小矩形
            food_position = [int(x*20),int(y*20)]
            food_flag = 1


        #背景绘制
        gameSurface.fill(bgColor)
        #绘制贪吃蛇
        for position in snake_body:
            pygame.draw.rect(gameSurface, snakeColor, pygame.Rect(position[0], position[1], 20, 20))
        pygame.display.flip()

        #绘制食物方块
        pygame.draw.rect(gameSurface,foodColor,pygame.Rect(food_position[0],food_position[1],20,20))
        pygame.display.flip()

        # 判断死亡
        if snake_position[0] > 640 or snake_position[0] < 0:
            gameOver()
        elif snake_position[1] > 480 or snake_position[1] < 0:
            gameOver()

        """
        #显示分数
        show_text(gameSurface,(20,30),'score:'+str(score),(223,223,223))
        """
        pygame.display.update()

        snakeSpeed.tick(5)

if __name__ == "__main__":
    while(1):
        main()