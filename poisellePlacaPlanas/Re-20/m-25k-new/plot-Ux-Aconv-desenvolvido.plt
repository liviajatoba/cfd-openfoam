reset

#set terminal postscript eps enhanced color"Times-Roman" 18
set term png

set autoscale
set lmargin 13
set bmargin 4

#set output "Ux-Ax-desenvolvido.eps"
set output "Ux-Ax-desenvolvido.png"


set xlabel"{/*1.5{/Italic Ux ou Ax}" offset 1,0
set ylabel"{/*1.5{/Italic y(m)} }" offset 0,0


set key bottom left
set xrange [-1.5:1.5]

plot "postProcessing/sampleU/1000/linhaE.dat"  using ($2):($1) title "{U_x desen}" with lines lt 1 lw 2.5, \
     "postProcessing/sampleAconv/1000/linhaE.dat"  using ($2):($1) title "{A_x desen}" with lines lt 3 lw 2.5
