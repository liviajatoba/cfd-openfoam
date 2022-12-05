reset

#set terminal postscript eps enhanced color"Times-Roman" 18
set term png

set autoscale
set lmargin 13
set bmargin 4

#set output "Ux.eps"
set output "Ux.png"

set ylabel"{/*1.5{/Italic y(m)}" offset 1,0
set xlabel"{/*1.5{/Italic U_x (m/s)} }" offset 0,0

plot "postProcessing/sampleU/10/linhaV_U.xy"  using ($2):($1) notitle"{Linha Vertical}" with lines lt 3 lw 2.5


