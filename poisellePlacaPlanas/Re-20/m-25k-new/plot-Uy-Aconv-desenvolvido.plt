reset

#set terminal postscript eps enhanced color"Times-Roman" 18
set term png

set autoscale
set lmargin 13
set bmargin 4

#set output "Uy-Ay-desenvolvido.eps"
set output "Uy-Ay-desenvolvido.png"


set xlabel"{/*1.5{/Italic Uy ou Ay}" offset 1,0
set ylabel"{/*1.5{/Italic y(m)} }" offset 0,0


set key bottom left
set xrange [-1.5:1.5]

plot "postProcessing/sampleU/1000/linhaE.dat"  using ($3):($1) title "{U_x desen}" with lines lt 1 lw 2.5, \
     "postProcessing/sampleAconv/1000/linhaE.dat"  using ($3):($1) title "{A_y desen}" with lines lt 3 lw 2.5
