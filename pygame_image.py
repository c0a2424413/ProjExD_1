import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    tmr = 0
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg") #背景画像のサーフェイス
    bg_img2 = pg.transform.flip(bg_img,True, False) #背景画像の反転
    kk_img = pg.image.load("fig/3.png") #こうかとん画像のサーフェイス
    kk_img = pg.transform.flip(kk_img, True, False) #こうかとん反転
    kk_rct = kk_img.get_rect()#rectを取得 
    kk_rct.center = 300, 200#中心座礁の設定
    
    while True:
        dx=0
        dy=0
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        key_lst =pg.key.get_pressed()
        #こうかとん矢印キー移動
        if key_lst[pg.K_UP]:
            dy= -1
        if key_lst[pg.K_DOWN]:
            dy= +1
        if key_lst[pg.K_RIGHT]:
            dx = +2
        if key_lst[pg.K_LEFT]:
            dx = -1
        kk_rct.move_ip((dx-1,dy))
        tmr1 = tmr%3200
        screen.blit(bg_img, [-tmr1, 0]) #1枚目
        screen.blit(bg_img2,[-tmr1+1600,0]) #2枚目
        screen.blit(bg_img,[-tmr1+3200,0])
        screen.blit(kk_img, kk_rct)#こうかとん表示
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()