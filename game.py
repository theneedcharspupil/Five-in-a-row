"""
Author: Lucky Pupil
Date:2022.02.19
Project Name: Five in a Row
"""
"""
游戏规则:
1.游戏开始后,黑色的玩家先下,白色的玩家后下。
2.如果以斜线,直线呈五个子连续的现象,则该玩家获胜。
游戏结束后,输出获胜者的名字。
游戏元素：
1.棋盘;
2.黑子;
3.白子;
"""
print(list(range(5)))
import time
import pygame
Screen = pygame.display.set_mode((800, 600))
def win_lose(x,y,xylist): # 判断输赢
    one = (x+1,y+1) in xylist and (x+2,y+2) in xylist and (x+3,y+3) in xylist and (x+4,y+4) in xylist #斜着的
    if  one:
        for f in range(5):
            pygame.draw.circle(Screen,(255,0,0),((x+f)*40,(y+f)*40),15)
            time.sleep(0.1)
        return True
    elif (x-1,y-1) in xylist and (x-2,y-2) in xylist and (x-3,y-3) in xylist and (x-4,y-4) in xylist: # 斜着的
        for f in range(5):
            pygame.draw.circle(Screen,(255,0,0),((x-f)*40,(y-f)*40),15)
            time.sleep(0.1)
        return True
    elif (x-1,y) in xylist and (x-2,y) in xylist and (x-3,y) in xylist and (x-4,y) in xylist: # 横着的
        for f in range(5):
            pygame.draw.circle(Screen,(255,0,0),((x-f)*40,(y)*40),15)
            time.sleep(0.1)
        return True
    elif (x,y-1) in xylist and (x,y-2) in xylist and (x,y-3) in xylist and (x,y-4) in xylist: # 竖着的
        for f in range(5):
            pygame.draw.circle(Screen,(255,0,0),((x)*40,(y-f)*40),15)
            time.sleep(0.1)
        return True
    elif (x+1,y) in xylist and (x+2,y) in xylist and (x+3,y) in xylist and (x+4,y) in xylist:# 横着的
        for f in range(5):
            pygame.draw.circle(Screen,(255,0,0),((x+f)*40,(y)*40),15)
            time.sleep(0.1)
        return True
    elif (x,y+1) in xylist and (x, y+2) in xylist and (x, y+3) in xylist and (x, y+4) in xylist: # 竖着的
        for f in range(5):
            pygame.draw.circle(Screen,(255,0,0),((x)*40,(y+f)*40),15)
            time.sleep(0.1)
        return True
    else:
        return False
def xy(pygame_x,pygame_y): # 由pygame自己的坐标返回五子棋坐标
    return (int(pygame_x / 40), int(pygame_y / 40))
import sys
def main():
    player_sort = True # 下子顺序，true为黑，false为白
    pygame.init()
    pygame.display.set_caption("五子棋")
    Screen.fill([0,255,255])  # 蓝色背景
    dot = [(i,j) for i in range(1,17) for j in range(1,23)] # 五子棋棋盘所有坐标
    for i in range(0,800,40):
        pygame.draw.line(Screen,(0,0,0),(i,0),(i,600)) # 绘制横线
    for i in range(0,600,40):
        pygame.draw.line(Screen,(0,0,0),(0,i),(800,i)) # 绘制竖线
    pygame.display.update()
    pygame.display.flip()
    white_xy_list = [] # 白色坐标列表
    black_xy_list = [] # 黑色坐标列表
    black_winner = False # 黑方赢
    white_winner = False # 白方赢
    while True:
        
        x,y = pygame.mouse.get_pos() # 鼠标坐标
        x,y = xy(x,y) # 转换
        for event in pygame.event.get():
            if (x,y) in dot and pygame.MOUSEBUTTONDOWN == event.type:
                if player_sort == True and (x,y) not in white_xy_list: # 下子条件
                    player_sort = False
                    black_winner = win_lose(x,y,black_xy_list) # 判断输赢
                    if black_winner == True:
                        print("黑方获胜")
                        pygame.display.set_caption("五子棋 -- 黑方获胜")
                    pygame.draw.circle(Screen,(0,0,0),(x*40,y*40),15) # 绘制棋子
                    print("黑方在坐标{},{}下子".format(x,y))
                    black_xy_list.append((x,y)) # 加入列表
                elif player_sort == False and (x,y) not in black_xy_list:
                    white_xy_list.append((x,y))
                    player_sort = True
                    white_winner = win_lose(x,y,white_xy_list)
                    if white_winner == True:
                        print("白方获胜")
                        pygame.display.set_caption("五子棋 -- 白方获胜")
                    print("白方在坐标{},{}下子".format(x,y))
                    pygame.draw.circle(Screen,(255,255,255),(x*40,y*40),15)
            if event.type == pygame.QUIT: # 退出判断
                pygame.quit()
                sys.exit()
        pygame.display.flip()
    
            
if __name__ == '__main__':
    main()
