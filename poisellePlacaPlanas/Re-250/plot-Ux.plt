reset

#set terminal postscript eps enhanced color"Times-Roman" 18
set term png

set autoscale
set lmargin 13
set bmargin 4

#set output "Ux.eps"
set output "Ux.png"

set key bottom left

h=0.01
hh=h*h
a=1/hh
b=-0.5
mu=0.001
c=b/(2*mu)

f1(x)= c*(x**2) - c*hh
f2(x)= 1 - a*(x**2)

set xlabel"{/*1.5{/Italic y (m) }" offset 1,0
set ylabel"{/*1.5{/Italic U_x (m/s)} }" offset 0,0
#set xrange [0:0.01]
#set yrange [0:1]

plot f1(x) title"{analitico}" with linespoints  lt 1 lw 2.5, \
     "postProcessing/sampleU/500/linhaA.xy"  using ($1):($2) title"{x = 0.005 m}" with lines lt 2 lw 2.5, \
     "postProcessing/sampleU/500/linhaB.xy"  using ($1):($2) title"{x = 0.010 m}" with linespoints lt 3 lw 2.5, \
     "postProcessing/sampleU/500/linhaC.xy"  using ($1):($2) title"{x = 0.015 m}" with linespoints lt 5 lw 2.5
