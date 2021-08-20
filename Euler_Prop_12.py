from manim import *
import numpy as np

class PropEuclid12(Scene):
    def construct(self):
        bidang = NumberPlane(
            x_range=[-10, 10, 1],
            y_range=[-10, 10, 1],
            axis_config={"include_numbers": False},
        )
        
        self.add(bidang)
        
        judul = Text("Proposisi #12 Euclid\n \'Elements\' Buku 1", should_center=False).move_to([-5,3,0]).scale(0.5)
        self.play(Write(judul))
        
        teks1 = Text("Tugas: \n Buatlah garis melewati C\n dan tegak lurus AB", should_center=True).move_to([4.7,3,0]).scale(0.45)
        self.play(Write(teks1))
        
        titik_A = Dot(point=[-6,-2.25,0], radius=0.08)
        titik_B = Dot(point=[6,-2.25,0], radius=0.08)
        titik_C = Dot(point=[0, 0 ,0], radius=0.08)
        garis_AB = Line(titik_A.get_center(), titik_B.get_center(), stroke_color='#f07fac', stroke_width=10)
        
        A = Text("A", font="sans-serif").next_to(titik_A, DOWN)
        B = Text("B", font="sans-serif").next_to(titik_B, DOWN)
        C = Text("C", font="sans-serif").next_to(titik_C, UP)
        
        self.add(titik_A, titik_B)
        self.play(Write(A), Write(B))
        self.play(Create(garis_AB))
        self.wait()
        self.add(titik_C)
        self.play(Write(C))
        self.wait(2)
        
        teks2 = Text("1.) Buat titik D di\n sisi sebalik titik C", should_center=True).move_to([4.7,3,0]).scale(0.45)
        self.play(FadeTransform(teks1, teks2))
        
        titik_D = Dot(point=[1.5,-3.25,0], radius=0.08, color='#8a8889')
        D = Text("D", font="sans-serif", color='#8a8889').next_to(titik_D, RIGHT)
        
        self.add(titik_D)
        self.play(Write(D))
        self.wait(2)
        
        teks3 = Text("2.) Buat lingkaran melewati D\n dan berpusat di C", should_center=True).move_to([4.7,3,0]).scale(0.45)
        self.play(ReplacementTransform(teks2, teks3))
        
        jarijari = np.linalg.norm(titik_D.get_center()-titik_C.get_center())
        lingkaran = Circle(radius=jarijari, color=YELLOW_D).shift(titik_C.get_center())
        
        self.play(Create(lingkaran))
        self.wait(2)
        
        teks4 = Text("3.) Tentukan titik E, F,\n dan titik G", should_center=True).move_to([4.7,3,0]).scale(0.45)
        self.play(FadeTransform(teks3, teks4))
        
        sudut_G = np.arcsin((titik_C.get_y()-titik_A.get_y())/jarijari)
        sudut_E = np.arcsin((titik_C.get_y()-titik_B.get_y())/jarijari)
        pos_Gx = titik_C.get_x()-(jarijari*np.cos(sudut_G))
        pos_Ex = titik_C.get_x()+(jarijari*np.cos(sudut_E))
        titik_G = Dot(point=[pos_Gx,titik_A.get_y(),0], radius=0.08)
        titik_E = Dot(point=[pos_Ex,titik_B.get_y(),0], radius=0.08)
        
        
        E = Text("E", font="sans-serif").next_to(titik_E, DOWN)
        F = Text("F", font="sans-serif").next_to(titik_C.get_center()+[0,jarijari,0], DOWN)
        G = Text("G", font="sans-serif").next_to(titik_G, DOWN)
        
        self.add(titik_G)
        self.wait()
        self.add(titik_E)
        self.play(Write(E), Write(F), Write(G))
        self.wait(2)
        
        teks5 = Text("4.) Buat titik H\n di antara G dan E", should_center=True).move_to([4.7,3,0]).scale(0.45)
        self.play(FadeTransform(teks4, teks5))
        
        titik_H = Dot(point=[np.amin([pos_Gx, pos_Ex]) + abs(pos_Ex - pos_Gx)/2,titik_A.get_y(),0], radius=0.08)
        
        H = Text("H", font="sans-serif").next_to(titik_H.get_center()+[0.3,0,0], DOWN)
        
        self.add(titik_H)
        self.play(Write(H))
        self.wait(2)
        
        teks6 = Text("5.) Panjang CE = CG\n dan ...", should_center=True).move_to([4.7,3,0]).scale(0.45)
        self.play(FadeTransform(teks5, teks6))
        
        garis_CG = DashedLine(titik_C.get_center(), titik_G.get_center(), stroke_color='#6cc908')
        garis_CE = DashedLine(titik_C.get_center(), titik_E.get_center(), stroke_color='#6cc908')
        garis_CH = Line(titik_C.get_center(), titik_H.get_center(), stroke_color='#f07fac', stroke_width=10)
        self.play(Create(garis_CG))
        self.play(Create(garis_CE))
        self.play(Create(garis_CH))
        self.wait(2.0)
        
        self.play(FadeOut(E), FadeOut(F), FadeOut(G), FadeOut(D), FadeOut(titik_E), FadeOut(titik_G), FadeOut(titik_D))
        self.play(FadeOut(lingkaran), FadeOut(garis_CG), FadeOut(garis_CE))
        
        teks7 = Text("6.) Garis CH tegak lurus\n garis AB.", should_center=True).move_to([4.7,3,0]).scale(0.45)
        self.play(FadeTransform(teks6, teks7))
        
        sudutsiku = Square(color='#eda09a', fill_opacity=0.5, side_length=0.5, stroke_width=0).move_to(titik_H.get_center()+[0.25,0.25,0])
        self.play(Create(sudutsiku))
        self.wait(5.0)
