reset

#set terminal postscript eps enhanced color"Times-Roman" 18
set term png

set autoscale
set lmargin 13
set bmargin 4

#set output "Ux.eps"
set output "Ux.png"

set key left

set xlabel"{/*1.5{/Italic y(m)}" offset 1,0
set ylabel"{/*1.5{/Italic U_x (m/s)} }" offset 0,0

V = 1
h = 0.1
a = V/h
f(x) = a*x

plot f(x) title "analitico" with linespoints lt 1, \
     "postProcessing/sampleU/0.5/linhaA_U.xy"  using ($1):($2) title"{0.5s}" with lines lt 2 lw 2.5, \
     "postProcessing/sampleU/0.3/linhaA_U.xy"  using ($1):($2) title"{0.3s}" with lines lt 3 lw 2.5, \
     "postProcessing/sampleU/0.2/linhaA_U.xy"  using ($1):($2) title"{0.2s}" with lines lt 4 lw 2.5

